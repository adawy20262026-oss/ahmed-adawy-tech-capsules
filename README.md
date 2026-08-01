# Ahmed Adawy Tech Capsules

> **Write once in Markdown. Generate beautiful technical publications everywhere.**

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Status](https://img.shields.io/badge/Status-Stable-success)
![Build](https://img.shields.io/github/actions/workflow/status/adawy20262026-oss/ahmed-adawy-tech-capsules/build.yml?branch=main)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub last commit](https://img.shields.io/github/last-commit/adawy20262026-oss/ahmed-adawy-tech-capsules)

---

# Overview

**Ahmed Adawy Tech Capsules** is an open-source publishing engine for creating professional technical micro-books from Markdown.

Instead of maintaining separate versions for PDF, HTML, and online articles, this project follows a simple philosophy:

> **One Markdown file → Multiple professional outputs.**

The project automatically transforms Markdown into beautifully formatted publications with a clean architecture designed for scalability and future publishing automation.

---

# Features

## Core Engine

- Markdown Parsing Engine
- HTML Rendering Engine
- Professional PDF Generation
- Modular Architecture
- Metadata Support
- Automatic Cover Pages
- Automatic Table of Contents
- Professional Typography
- Responsive Images
- Styled Tables
- Code Block Rendering
- HTML Escaping
- Library Index Generator

---

## User Interface

- Streamlit Interface
- Markdown Upload
- Live PDF Generation
- Instant PDF Download

---

## Developer Experience

- GitHub Actions CI
- Automatic Capsule Builds
- Modular Components
- Clean Project Structure
- Easily Extendable Architecture

---

# Architecture

```text
                 Markdown
                     │
                     ▼
             Markdown Parser
                     │
                     ▼
              Internal Document
                     │
                     ▼
              HTML Renderer
      ┌──────────┬────────────┐
      ▼          ▼            ▼
   Cover      TOC         Content
                     │
                     ▼
               HTML Document
                     │
                     ▼
              PDF Generator
                     │
                     ▼
            Professional PDF
```

---

# Project Structure

```text
ahmed-adawy-tech-capsules/

├── app.py
├── capsules/
├── assets/
├── output/
├── templates/
│
├── src/
│   ├── builder.py
│   ├── parser.py
│   ├── renderer.py
│   ├── content_renderer.py
│   ├── cover.py
│   ├── toc.py
│   ├── footer.py
│   ├── pdf_generator.py
│   ├── metadata.py
│   ├── styles.py
│   ├── theme.py
│   └── ...
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# Quick Start

Clone the repository

```bash
git clone https://github.com/adawy20262026-oss/ahmed-adawy-tech-capsules.git
```

Enter the project

```bash
cd ahmed-adawy-tech-capsules
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# How It Works

```
Write Markdown

        │

        ▼

Upload to Streamlit

        │

        ▼

Generate HTML

        │

        ▼

Generate PDF

        │

        ▼

Download Your Capsule
```

---

# Current Capabilities

- Professional PDF Layout
- Cover Pages
- Automatic Table of Contents
- Styled Code Blocks
- Styled Tables
- Metadata Parsing
- Multi-Capsule Build
- Library Index Generation
- GitHub Actions Automation
- Streamlit Interface

---

# Roadmap

## Version 0.5

- Syntax Highlighting (Pygments)
- Better Code Formatting
- Page Numbers
- Cover Images
- HTML Preview
- ZIP Export

---

## Version 0.6

- HTML Export
- EPUB Export
- DOCX Export
- Theme Selector
- Custom Templates

---

## Version 1.0

**One Markdown → Publish Everywhere**

Future publishing targets include:

- Medium
- Hashnode
- Dev.to
- Substack
- Static HTML
- GitHub Pages

---

# Why This Project?

Writing technical content should not require maintaining multiple versions of the same document.

This project allows technical authors to focus on writing once while automatically producing professional publications with a consistent design and scalable architecture.

---

# Technologies

- Python
- Markdown
- HTML
- CSS
- WeasyPrint
- Streamlit
- GitHub Actions

---

# Contributing

Contributions are welcome.

Whether you're fixing bugs, improving documentation, or adding new publishing capabilities, every contribution helps make the project better.

Feel free to open an Issue or submit a Pull Request.

---

# Author

## Ahmed Adawy

AI Technical Author • Python Developer • Open Source Enthusiast

GitHub

https://github.com/adawy20262026-oss

LinkedIn

https://www.linkedin.com/in/ahmed-adawy

---

# License

Released under the MIT License.

---

## Vision

The long-term vision is to transform this project into a complete technical publishing platform capable of producing and distributing professional publications from a single Markdown source.

**Write Once. Publish Everywhere.**
