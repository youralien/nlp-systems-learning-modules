# Organized Readings: AI, Mental Health, and Human Learning

## Folder Structure & Themes

### 01: AI for Training Human Helpers (Simulation & Practice)
Industry and academic approaches to using AI to train counselors, clinicians, and other human helpers through simulation, role-play, and feedback systems.

**Key questions**: How do we scale training? What makes simulated practice effective? When does AI feedback help vs. hurt skill development?

### 02: Technical Methods for AI Feedback and Learning Systems
Technical approaches: RL methods, feedback generation algorithms, dropout strategies for training, mutual information optimization, MIPO, and related ML/NLP techniques.

**Key questions**: How do we formulate feedback generation as an optimization problem? What's the right way to model p(y|x,c)?

### 03: Persuasion, Behavior Change, and User Acceptance
How AI systems influence human behavior, user acceptance/rejection of AI tools, disengagement patterns, and ethics of deploying AI in learning contexts.

**Key questions**: When should we roll out AI in classrooms? What drives disengagement or nonuse?

### 04: Risks and Dark Sides of AI Interaction (Addiction, Deskilling, Technostress)
Negative consequences of AI interaction: addiction to chatbots, deskilling of professionals, technostress, long-context "psychosis," and LLMs getting lost in multi-turn conversations.

**Key questions**: What are the harms we should be measuring? How do we design for safety?

### 05: Relational Intelligence and Human-Likeness in AI
Concepts of relational intelligence, what makes AI feel "human-like," and the gap between design criteria and user experience.

**Key questions**: What do users actually want from AI relationships? How does human-likeness affect outcomes?

### 06: Accessibility, Inclusion, and Speech Interfaces
Making AI systems accessible across abilities, languages, and contexts. Speech interfaces, inclusive design.

**Key questions**: Who gets left out? How do we design for diverse users?

### 07: AI Therapy Efficacy: Evidence and Skepticism
Critical examination of AI therapy claims, meta-analyses, regression to the mean, repetition in discourse moves.

**Key questions**: Does AI therapy actually work? What evidence do we have?

### 08: AI-Human Division of Labor and Complementarity
How AI and humans can work together, what tasks each is suited for, distinct vs. overlapping roles in support contexts.

**Key questions**: What do people ask AI vs. humans? How do we design for complementarity?

### 09: Personalization, Bias, and Cultural Adaptation in AI
The double-edged sword of personalization: cultural adaptation vs. identity-based biases, caricatured responses, demographic stereotyping in AI outputs.

**Key questions**: When does personalization help vs. harm? How do we adapt AI for diverse cultures?

### 10: Simulated Users and Synthetic Data for AI Training
Using LLMs to simulate users for training other AI systems, synthetic data generation, vague intent modeling.

**Key questions**: Can synthetic users replace real users? What are the limits of simulation?

### 11: Learner Agency, Autonomy, and Metrics
Measuring and supporting learner agency, autonomy in AI-assisted learning, metrics for empowerment.

**Key questions**: How do we measure agency? Does AI increase or decrease learner autonomy?

---

## Files

- `readings.jsonl` - All readings in JSONL format (one JSON object per line)
- `SCHEMA.json` - JSON Schema defining the structure of each reading entry
- `INDEX.md` - This file

## Usage

Load `readings.jsonl` in Python:
```python
import json

readings = []
with open('readings.jsonl', 'r') as f:
    for line in f:
        readings.append(json.loads(line))

# Filter by theme
theme_01 = [r for r in readings if r['theme_folder'].startswith('01_')]
```

Convert to BibTeX (example for one entry):
```python
def to_bibtex(entry):
    bib_type = entry.get('entry_type', 'misc')
    bib_id = entry['id']
    fields = []
    for key in ['author', 'title', 'year', 'booktitle', 'journal', 'url', 'doi', 'publisher', 'abstract']:
        if entry.get(key):
            fields.append(f'  {key} = {{{entry[key]}}}')
    return f"@{bib_type}{{{bib_id},\n" + ",\n".join(fields) + "\n}"
```
