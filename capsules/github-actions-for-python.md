---
title: GitHub Actions for Python Projects
subtitle: Automating Testing, Building & Deployment
author: Ahmed Adawy
category: DevOps
difficulty: Intermediate
language: English
version: 1.0
tags:
  - GitHub Actions
  - Python
  - CI/CD
  - Automation
  - DevOps
---

# GitHub Actions for Python Projects

> A practical guide to automating testing, building, and deployment using GitHub Actions.

# Introduction

Modern software development is no longer just about writing code.

Every professional project requires automation to ensure that code is tested, built, and deployed consistently. Performing these tasks manually quickly becomes repetitive, error-prone, and difficult to maintain.

GitHub Actions is GitHub's built-in Continuous Integration and Continuous Deployment (CI/CD) platform. It allows developers to automate workflows directly inside their repositories without relying on external services.

With only a few configuration files, developers can automatically:

- Run unit tests.
- Check code quality.
- Build applications.
- Generate documentation.
- Publish releases.
- Deploy applications.

In this capsule, you will learn how GitHub Actions works from the ground up through practical Python examples and real-world workflows.

# Why GitHub Actions?

Before automation, developers often performed the same repetitive tasks every time they pushed new code.

Typical manual workflow:

1. Run unit tests.
2. Build the project.
3. Check formatting.
4. Generate documentation.
5. Deploy the application.

Repeating these steps manually wastes time and increases the chance of human error.

GitHub Actions automates the entire process.

Instead of remembering every step, developers define a workflow once. Every future push automatically executes the same process.

This approach improves:

- Reliability
- Productivity
- Code quality
- Team collaboration
- Release confidence

# Jobs

A workflow is divided into one or more jobs.

Each job runs inside its own virtual environment.

By default, jobs execute in parallel.

However, jobs can also depend on each other.

For example:

Build Job

↓

Test Job

↓

Deploy Job

This dependency chain guarantees that deployment only occurs after successful testing.

Each job defines:

- A runner
- One or more steps
- Optional dependencies
- Environment variables

Example:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
```

The `runs-on` key specifies the virtual machine that GitHub will use to execute the job.

GitHub currently provides runners for:

- Ubuntu
- Windows
- macOS

Ubuntu is the most commonly used runner for Python projects because it is fast, reliable, and free for public repositories.

> **Key Takeaway**

> A workflow can contain multiple jobs, and each job executes independently unless dependencies are explicitly defined.

# Steps

Every job consists of a sequence of steps.

A step represents a single action.

Typical steps include:

- Checking out the repository.
- Installing Python.
- Installing dependencies.
- Running tests.
- Building the project.
- Uploading artifacts.

Example:

```yaml
steps:
  - uses: actions/checkout@v4

  - uses: actions/setup-python@v5

  - run: pip install -r requirements.txt

  - run: pytest
```

GitHub executes the steps in order.

If one step fails, the remaining steps are skipped unless explicitly configured otherwise.

This behavior prevents invalid builds from continuing.

> **Key Takeaway**

> Steps are the smallest executable units inside a GitHub Actions job.

# Your First Workflow

A GitHub Actions workflow is defined inside a YAML file.

The file must be placed inside:

```text
.github/workflows/
```

A minimal workflow looks like this:

```yaml
name: Python CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: python --version
```

Let's understand each part.

| Section | Purpose |
|---------|---------|
| name | Workflow name displayed in GitHub |
| on | Defines the trigger event |
| jobs | Collection of jobs |
| runs-on | Operating system used |
| steps | Individual tasks |

This workflow simply starts a Linux virtual machine, downloads the repository, installs Python, and prints the Python version.

> **Key Takeaway**

> Every GitHub Actions workflow starts with a trigger, then executes one or more jobs composed of sequential steps.

# Installing Project Dependencies

Most Python projects rely on external packages.

Before running tests or building the project, these packages must be installed.

The standard approach is:

```yaml
- run: pip install -r requirements.txt
```

The `requirements.txt` file contains all project dependencies.

Example:

```text
markdown
weasyprint
pytest
pytest-cov
pygments
mistletoe
```

Installing dependencies guarantees that every workflow runs in a clean and reproducible environment.

Without this step, many builds would fail because required libraries would not be available.

> **Key Takeaway**

> Always install project dependencies before executing tests or build commands.
