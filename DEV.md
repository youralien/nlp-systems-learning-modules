# Development Guide

This project uses [slidev-workspace](https://github.com/leochiu-a/slidev-workspace) to manage multiple Slidev presentations with a unified landing page.

## Prerequisites

- Node.js >= 18
- pnpm (`npm install -g pnpm`)

## Setup

```bash
pnpm install
```

## Commands

| Command | Description |
|---------|-------------|
| `pnpm preview` | Start dev server at `http://localhost:3000/nlp-systems-learning-modules` |
| `pnpm build` | Build all presentations for production (outputs to `dist/`) |

## Project Structure

```
├── .github/workflows/deploy.yml   # GitHub Pages deployment
├── package.json
├── pnpm-workspace.yaml            # Defines slides/* as workspace packages
├── slidev-workspace.yaml          # Landing page config + baseUrl
└── slides/
    ├── module-01-intro/
    │   └── slides.md
    └── module-02-tokenization/
        └── slides.md
```

## Adding a New Presentation

1. Create a new folder under `slides/`:
   ```bash
   mkdir -p slides/module-03-embeddings
   ```

2. Create `slides.md` with frontmatter:
   ```markdown
   ---
   theme: default
   title: "Module 3: Embeddings"
   description: "Understanding word embeddings"
   ---

   # Embeddings

   Your content here...

   ---

   ## Next Slide

   More content...
   ```

3. Run `pnpm preview` to see it in the landing page

## Configuration Files

### `slidev-workspace.yaml`

```yaml
hero:
  title: "NLP Systems Learning Modules"
  description: "Browse all available slide decks"

baseUrl: "/nlp-systems-learning-modules"  # Must match repo name for GitHub Pages
```

### `pnpm-workspace.yaml`

```yaml
packages:
  - "slides/*"
```

This tells pnpm to treat each folder in `slides/` as a workspace package.

## Slide Frontmatter

Each `slides.md` should have frontmatter for the landing page:

```yaml
---
theme: default          # Slidev theme
title: "Module Title"   # Shown on landing page
description: "..."      # Shown on landing page
author: "Name"          # Optional
keywords: a,b,c         # Optional, for search
---
```

## Deployment

Deployment is automatic via GitHub Actions on push to `main`.

### Manual Steps (first time only)

1. Go to repo **Settings > Pages**
2. Under "Build and deployment", select **GitHub Actions**

### URLs

- Landing page: `https://<username>.github.io/nlp-systems-learning-modules/`
- Individual deck: `https://<username>.github.io/nlp-systems-learning-modules/<folder-name>/`

## Troubleshooting

### Preview shows blank page

Make sure you're accessing the correct URL with the base path:
```
http://localhost:3000/nlp-systems-learning-modules/
```

### Slides not appearing on landing page

- Check that `slides.md` exists in the folder (not a different filename)
- Ensure frontmatter has `title` field
- Restart the dev server after adding new folders

### Build fails on GitHub Actions

- Verify `baseUrl` in `slidev-workspace.yaml` matches the repo name
- Check that `pnpm-lock.yaml` is committed

## Resources

- [Slidev Documentation](https://sli.dev/)
- [slidev-workspace GitHub](https://github.com/leochiu-a/slidev-workspace)
- [Slidev Themes](https://sli.dev/resources/theme-gallery)
