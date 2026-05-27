#!/usr/bin/env python3
"""
Lightweight Citation Manager Server
A barebones Zotero/Mendeley alternative for managing research readings.
"""

import json
import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__, static_folder='static')
CORS(app)

# Path to the JSONL file
READINGS_FILE = Path(__file__).parent / 'readings.jsonl'
SCHEMA_FILE = Path(__file__).parent / 'SCHEMA.json'

def load_readings():
    """Load all readings from JSONL file."""
    readings = []
    if READINGS_FILE.exists():
        with open(READINGS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    readings.append(json.loads(line))
    return readings

def save_readings(readings):
    """Save all readings to JSONL file."""
    with open(READINGS_FILE, 'w') as f:
        for reading in readings:
            f.write(json.dumps(reading) + '\n')

def load_schema():
    """Load the JSON schema."""
    if SCHEMA_FILE.exists():
        with open(SCHEMA_FILE, 'r') as f:
            return json.load(f)
    return {}

# API Routes

@app.route('/')
def index():
    """Serve the main HTML interface."""
    return send_from_directory('static', 'index.html')

@app.route('/api/readings', methods=['GET'])
def get_readings():
    """Get all readings with optional filtering."""
    readings = load_readings()

    # Filter by query params
    theme = request.args.get('theme')
    status = request.args.get('status')
    source_type = request.args.get('source_type')
    search = request.args.get('search', '').lower()

    if theme:
        readings = [r for r in readings if r.get('theme_folder') == theme]
    if status:
        readings = [r for r in readings if r.get('status') == status]
    if source_type:
        readings = [r for r in readings if r.get('source_type') == source_type]
    if search:
        readings = [r for r in readings if
                   search in r.get('title', '').lower() or
                   search in r.get('author', '').lower() or
                   search in r.get('user_notes', '').lower() or
                   search in r.get('abstract', '').lower()]

    return jsonify(readings)

@app.route('/api/readings/<reading_id>', methods=['GET'])
def get_reading(reading_id):
    """Get a single reading by ID."""
    readings = load_readings()
    for r in readings:
        if r.get('id') == reading_id:
            return jsonify(r)
    return jsonify({'error': 'Reading not found'}), 404

@app.route('/api/readings/<reading_id>', methods=['PUT'])
def update_reading(reading_id):
    """Update a reading by ID."""
    readings = load_readings()
    updated_data = request.json

    for i, r in enumerate(readings):
        if r.get('id') == reading_id:
            # Merge updates
            readings[i] = {**r, **updated_data}
            save_readings(readings)
            return jsonify(readings[i])

    return jsonify({'error': 'Reading not found'}), 404

@app.route('/api/readings', methods=['POST'])
def create_reading():
    """Create a new reading."""
    readings = load_readings()
    new_reading = request.json

    # Check for duplicate ID
    if any(r.get('id') == new_reading.get('id') for r in readings):
        return jsonify({'error': 'Reading with this ID already exists'}), 400

    readings.append(new_reading)
    save_readings(readings)
    return jsonify(new_reading), 201

@app.route('/api/readings/<reading_id>', methods=['DELETE'])
def delete_reading(reading_id):
    """Delete a reading by ID."""
    readings = load_readings()
    original_len = len(readings)
    readings = [r for r in readings if r.get('id') != reading_id]

    if len(readings) == original_len:
        return jsonify({'error': 'Reading not found'}), 404

    save_readings(readings)
    return jsonify({'success': True})

@app.route('/api/readings/<reading_id>/move', methods=['POST'])
def move_reading(reading_id):
    """Move a reading to a different theme folder."""
    readings = load_readings()
    new_theme = request.json.get('theme_folder')

    for i, r in enumerate(readings):
        if r.get('id') == reading_id:
            readings[i]['theme_folder'] = new_theme
            save_readings(readings)
            return jsonify(readings[i])

    return jsonify({'error': 'Reading not found'}), 404

@app.route('/api/schema', methods=['GET'])
def get_schema():
    """Get the JSON schema for readings."""
    return jsonify(load_schema())

@app.route('/api/themes', methods=['GET'])
def get_themes():
    """Get list of all theme folders."""
    schema = load_schema()
    themes = schema.get('properties', {}).get('theme_folder', {}).get('enum', [])
    return jsonify(themes)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics about the readings."""
    readings = load_readings()

    stats = {
        'total': len(readings),
        'by_theme': {},
        'by_status': {},
        'by_source_type': {}
    }

    for r in readings:
        theme = r.get('theme_folder', 'unknown')
        status = r.get('status', 'unknown')
        source = r.get('source_type', 'unknown')

        stats['by_theme'][theme] = stats['by_theme'].get(theme, 0) + 1
        stats['by_status'][status] = stats['by_status'].get(status, 0) + 1
        stats['by_source_type'][source] = stats['by_source_type'].get(source, 0) + 1

    return jsonify(stats)

@app.route('/api/export/bibtex', methods=['GET'])
def export_bibtex():
    """Export all readings as BibTeX."""
    readings = load_readings()
    bibtex_entries = []

    for r in readings:
        entry_type = r.get('entry_type', 'misc')
        entry_id = r.get('id', 'unknown')

        fields = []
        field_mapping = [
            ('author', 'author'),
            ('title', 'title'),
            ('year', 'year'),
            ('booktitle', 'booktitle'),
            ('journal', 'journal'),
            ('url', 'url'),
            ('doi', 'doi'),
            ('publisher', 'publisher'),
            ('abstract', 'abstract'),
            ('volume', 'volume'),
            ('number', 'number'),
            ('pages', 'pages'),
            ('isbn', 'isbn'),
            ('series', 'series'),
        ]

        for json_key, bib_key in field_mapping:
            if r.get(json_key):
                value = r[json_key].replace('{', '\\{').replace('}', '\\}')
                fields.append(f'  {bib_key} = {{{value}}}')

        if r.get('keywords'):
            kw = ', '.join(r['keywords'])
            fields.append(f'  keywords = {{{kw}}}')

        entry = f"@{entry_type}{{{entry_id},\n" + ",\n".join(fields) + "\n}"
        bibtex_entries.append(entry)

    return '\n\n'.join(bibtex_entries), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    # Create static folder if it doesn't exist
    static_dir = Path(__file__).parent / 'static'
    static_dir.mkdir(exist_ok=True)

    print("Starting Citation Manager Server...")
    print("Open http://localhost:5111 in your browser")
    app.run(host='0.0.0.0', port=5111, debug=True)
