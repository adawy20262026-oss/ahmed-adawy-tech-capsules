# Ahmed Adawy Tech Capsules Architecture

> Write Once. Publish Everywhere.

---

# Vision

Ahmed Adawy Tech Capsules is an open-source publishing engine that transforms Markdown documents into professional technical publications.

The long-term vision is to allow developers and technical writers to write content once and publish it in multiple formats with a single command.

---

# Goals

- Generate beautiful PDF books.
- Generate HTML versions.
- Keep content separate from presentation.
- Automate the publishing process.
- Make the project extensible.
- Keep the developer experience simple.

---

# High-Level Pipeline

```text
Markdown
      │
      ▼
Parser
      │
      ▼
Document Model
      │
      ▼
Renderer
      │
      ▼
HTML
      │
      ▼
PDF Generator
      │
      ▼
Output
```

---

# Project Structure

```text
ahmed-adawy-tech-capsules/

capsules/
    Technical books written in Markdown.

docs/
    Project documentation.

output/
    Generated HTML and PDF files.

src/
    Source code.

templates/
    HTML templates.

themes/
    CSS themes.

.github/
    GitHub Actions workflows.
```

---

# Core Components

## Parser

Responsible for reading Markdown files and extracting structured content.

---

## Renderer

Converts structured content into HTML.

---

## Theme Engine

Controls fonts, colors, spacing, and layout.

---

## PDF Generator

Converts HTML into high-quality PDF documents.

---

## Build System

Coordinates the entire build process.

---

# Future Components

- CLI Tool
- Plugin System
- EPUB Generator
- GitHub Pages Publisher
- AI Writing Assistant
- Multi-language Support

---

# Design Principles

- Simplicity first.
- Separation of concerns.
- Reusable components.
- Automation by default.
- Open-source friendly.
- Clean project structure.

---

# Long-Term Vision

The final goal is not simply generating PDFs.

The goal is building a complete technical publishing engine capable of producing professional books, technical capsules, documentation, and educational material from Markdown sources.

Write once.

Publish everywhere.
