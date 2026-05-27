# Process: From Unstructured Research Scratchpad to Organized Readings

This document describes the interactive synthesis process used to transform `unorganized_capture/research_scratchpad.md` into the structured `organized_readings/` system.

## Overview

The goal is to take a running stream-of-consciousness research scratchpad (links, notes, reflections, technical ideas) and synthesize it into:
1. **Thematic folders** representing high-level research interests
2. **JSONL entries** with bibliographic fields for each reading/resource
3. **Personal annotations** preserving your original insights

## The Three-Level Synthesis Process

### Level (a): Based on Notes You Took
- Read the scratchpad in batches (~30-40 lines at a time)
- Extract the *why* behind each link from your annotations
- Identify patterns: What are you repeatedly interested in?

### Level (b): Based on Abstracts/Key Blurbs
- For papers: fetch abstracts from arXiv, ACM DL, etc.
- For industry/social: capture the core claim or value proposition
- Enrich the `abstract` field in JSONL entries

### Level (c): Schema of Contribution
For each reading, ask:
- **What did they do?** (method, study, product)
- **Why did they do it?** (motivation, gap addressed)
- **What's their contribution?** (to the broader field)

This maps to the `user_notes` and `abstract` fields.

## Step-by-Step Process

### 1. Batch Reading
```
Read lines 1-30, then 30-70, then 70-110, etc.
```
Don't try to read everything at once. Work in digestible batches.

### 2. Theme Identification
After each batch, identify emerging themes. Start broad, then:
- **Expand**: Split themes that are too diverse
- **Consolidate**: Merge themes that overlap significantly

Example evolution:
- Initial: "AI for mental health"
- Split into: "AI for training helpers" + "AI therapy efficacy" + "Risks of AI interaction"

### 3. Create Folder Structure
Use numbered, descriptive folder names:
```
01_ai_for_training_human_helpers_simulation_and_practice/
02_technical_methods_for_ai_feedback_and_learning_systems/
...
```
Numbers allow for logical ordering (like weeks in a course).

### 4. Create JSONL Entries
For each link/reading in the scratchpad, create a JSON entry with:

**Required fields:**
- `id`: Unique identifier (author_year_keyword format)
- `entry_type`: BibTeX type (article, inproceedings, misc, industry, etc.)
- `title`: Title of the work
- `theme_folder`: Which folder this belongs to
- `source_type`: paper, preprint, blog_post, social_media, industry_product, etc.
- `status`: to_read, reading, read, synthesized, noted

**Standard bib fields:**
- `author`, `year`, `url`, `doi`, `abstract`, `booktitle`, `journal`, etc.

**Custom fields:**
- `user_notes`: Your personal annotations from the scratchpad
- `social_url`: Where you found it (Twitter, LinkedIn link)
- `scratchpad_line`: Line number in original file for reference
- `date_captured`: When you added it

### 5. Iterate and Refine
As you process more batches:
- New themes may emerge → create new folders
- Existing themes may split → rename and redistribute
- Some readings may fit multiple themes → pick primary, note secondary

## File Structure

```
organized_readings/
├── CLAUDE.md          # This process document
├── INDEX.md           # Theme descriptions + usage examples
├── SCHEMA.json        # JSON Schema for validation
├── readings.jsonl     # All entries (one JSON per line)
└── [theme_folders]/   # Empty folders for future PDFs, notes, etc.
```

## Continuing the Process

To add more readings from the scratchpad:

1. **Resume scanning**: Pick up where you left off (check `scratchpad_line` of last entry)
2. **Run the prompt**: "Continue scanning lines X-Y and add to the JSONL"
3. **Review themes**: After each batch, ask "Do existing themes still work?"

### Example Prompt for Continuation
```
Read lines 110-150 of unorganized_capture/research_scratchpad.md.
Continue identifying themes and adding JSONL entries to readings.jsonl.
Consolidate or expand themes as needed.
```

## Converting to Other Formats

### To BibTeX
```python
import json

def to_bibtex(entry):
    bib_type = entry.get('entry_type', 'misc')
    bib_id = entry['id']
    fields = []
    for key in ['author', 'title', 'year', 'booktitle', 'journal',
                'url', 'doi', 'publisher', 'abstract', 'pages']:
        if entry.get(key):
            val = entry[key]
            if isinstance(val, list):
                val = ', '.join(val)
            fields.append(f'  {key} = {{{val}}}')
    return f"@{bib_type}{{{bib_id},\n" + ",\n".join(fields) + "\n}"

with open('readings.jsonl') as f:
    for line in f:
        entry = json.loads(line)
        print(to_bibtex(entry))
        print()
```

### To HTML (expandable cards)
```python
import json

html = ['<div class="readings">']
with open('readings.jsonl') as f:
    for line in f:
        e = json.loads(line)
        html.append(f'''
        <details class="reading-card" data-theme="{e['theme_folder']}">
          <summary>{e['title']} ({e.get('year', 'n.d.')})</summary>
          <p><strong>Author:</strong> {e.get('author', 'Unknown')}</p>
          <p><strong>Notes:</strong> {e.get('user_notes', '')}</p>
          <p><a href="{e.get('url', '#')}">Link</a></p>
        </details>
        ''')
html.append('</div>')
```

## Current Themes (as of initial synthesis)

| # | Theme | Key Question |
|---|-------|--------------|
| 01 | AI for Training Human Helpers | How do we scale counselor/clinician training? |
| 02 | Technical Methods for AI Feedback | How do we formulate feedback as optimization? |
| 03 | Persuasion & Behavior Change | When should we deploy AI in learning contexts? |
| 04 | Risks of AI Interaction | What harms should we measure? |
| 05 | Relational Intelligence & Human-Likeness | What do users want from AI relationships? |
| 06 | Accessibility & Inclusion | Who gets left out? |
| 07 | AI Therapy Efficacy & Skepticism | Does AI therapy actually work? |
| 08 | AI-Human Division of Labor | What tasks suit AI vs. humans? |
| 09 | Personalization vs. Bias | When does personalization help vs. harm? |
| 10 | Simulated Users & Synthetic Data | Can synthetic users replace real ones? |
| 11 | Learner Agency & Metrics | Does AI increase or decrease learner autonomy? |

---

*Last updated: 2026-05-27*
*Lines processed: 1-609 of research_scratchpad.md (complete)*
