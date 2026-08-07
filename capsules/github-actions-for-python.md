
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

# Testing with Pytest

Automated testing is one of the main reasons developers use GitHub Actions.

Instead of manually running tests before every commit, GitHub Actions can execute the test suite automatically whenever new code is pushed.

A common workflow step looks like this:

```yaml
- name: Run Tests
  run: |
    pytest --cov=src --cov-report=term-missing
```

Let's understand this command.

| Option | Description |
|---------|-------------|
| pytest | Executes all project tests |
| --cov=src | Measures code coverage for the `src` package |
| --cov-report=term-missing | Displays missing lines directly in the terminal |

Running tests automatically provides several advantages:

- Detects bugs early.
- Prevents broken code from reaching the main branch.
- Increases confidence before releases.
- Ensures consistent quality across contributors.

## Real Project Example

The **Ahmed Adawy Tech Capsules** project uses the following command inside its GitHub Actions workflow:

```yaml
- name: Run Tests with Coverage
  run: |
    pytest --cov=src --cov-report=term-missing
```

A successful execution produces output similar to:

```text
============================ test session starts ============================

collected 54 items

54 passed

Coverage Report

TOTAL............................94%
```

This means:

- All automated tests completed successfully.
- No failing test cases were found.
- Approximately 94% of the source code is covered by automated tests.

High code coverage does not guarantee bug-free software, but it significantly improves confidence in the stability of a project.

> **Key Takeaway**

> Automating tests with GitHub Actions ensures that every code change is validated before becoming part of the project.

# Uploading Build Artifacts

After a successful build, GitHub Actions can store generated files as artifacts.

Artifacts allow developers to download build outputs directly from the workflow page.

Typical artifacts include:

- PDF files
- Documentation
- Test reports
- Coverage reports
- Executable binaries

Example:

```yaml
- name: Upload PDF
  uses: actions/upload-artifact@v4
  with:
    name: tech-capsules
    path: output/
```

Once the workflow finishes successfully, GitHub stores the generated files for later download.

This feature is particularly useful for documentation projects where every commit automatically produces updated PDF versions.

In the Ahmed Adawy Tech Capsules project, artifacts are used to archive generated technical capsules after every successful build.

> **Key Takeaway**

> Artifacts make it easy to distribute generated files without committing them to the repository.

# Best Practices

Writing a workflow is easy.

Writing a maintainable workflow is the real challenge.

The following practices are recommended for professional Python projects.

## 1. Keep Workflows Small

Instead of creating one huge workflow, split responsibilities into multiple jobs or separate workflow files.

This improves readability and makes debugging much easier.

---

## 2. Pin Action Versions

Avoid using floating versions whenever possible.

Good:

```yaml
uses: actions/checkout@v4
```

Better than:

```yaml
uses: actions/checkout@main
```

Pinning versions ensures predictable behavior over time.

---

## 3. Test Every Push

Never wait until release day to discover problems.

Run automated tests on every push and every pull request.

---

## 4. Use Secrets Correctly

Never hardcode passwords, API keys, or tokens.

Instead, store sensitive information inside GitHub Secrets.

Example:

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

---

## 5. Cache Dependencies

Large projects spend significant time reinstalling packages.

GitHub Actions caching can dramatically reduce build time.

---

## 6. Read Workflow Logs

Every workflow execution produces detailed logs.

Learning to read these logs makes debugging much faster.

> **Key Takeaway**

> Simple workflows are easier to maintain, easier to debug, and more reliable over time.

# Common Mistakes

Even experienced developers occasionally make mistakes when writing GitHub Actions workflows.

Here are some of the most common ones.

## Incorrect YAML Indentation

YAML depends entirely on indentation.

Even a single misplaced space can prevent the workflow from running.

---

## Forgetting Checkout

Without:

```yaml
uses: actions/checkout@v4
```

GitHub Actions does not download your repository.

---

## Missing Dependencies

Running tests before installing project requirements usually results in import errors.

Always install dependencies first.

---

## Wrong Python Version

Projects should explicitly define the Python version.

Example:

```yaml
python-version: "3.12"
```

This guarantees consistent execution across environments.

---

## Ignoring Failed Tests

Never ignore failing tests.

A failing workflow should stop deployment until the problem is fixed.

---

## Hardcoding Secrets

Sensitive credentials should never appear inside workflow files.

Always use GitHub Secrets.

> **Key Takeaway**

> Most GitHub Actions problems are caused by small configuration mistakes rather than complex programming errors.

# GitHub Actions Cheat Sheet

The following reference summarizes the most commonly used GitHub Actions concepts.

## Workflow Location

```text
.github/workflows/
```

---

## Common Events

| Event | Purpose |
|--------|---------|
| push | Trigger after pushing commits |
| pull_request | Trigger for Pull Requests |
| workflow_dispatch | Manual execution |
| release | Trigger when publishing a release |
| schedule | Execute on a schedule |

---

## Common Runners

| Runner | Operating System |
|---------|------------------|
| ubuntu-latest | Ubuntu Linux |
| windows-latest | Microsoft Windows |
| macos-latest | Apple macOS |

---

## Frequently Used Actions

```yaml
actions/checkout@v4
actions/setup-python@v5
actions/upload-artifact@v4
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests

```bash
pytest
```

---

## Run Tests with Coverage

```bash
pytest --cov=src --cov-report=term-missing
```

---

## Build Documentation

```bash
python src/build.py
```

---

## Upload Artifacts

```yaml
uses: actions/upload-artifact@v4
```

---

## Recommended Workflow Order

Repository Event

↓

Checkout Repository

↓

Setup Python

↓

Install Dependencies

↓

Run Tests

↓

Build Project

↓

Upload Artifacts

↓

Workflow Finished

> **Quick Tip**

> Keep this page as a quick reference whenever creating a new GitHub Actions workflow.

# Summary

GitHub Actions has become one of the most important tools in modern software development.

Throughout this capsule, you learned how to:

- Understand workflows.
- Configure workflow events.
- Organize jobs and steps.
- Install Python dependencies.
- Execute automated tests.
- Measure code coverage.
- Upload generated artifacts.
- Apply professional workflow practices.
- Avoid common configuration mistakes.

Most importantly, you saw these concepts applied in a real-world project rather than isolated examples.

Automation is not just about saving time.

It improves reliability, consistency, collaboration, and software quality.

Once a workflow is written correctly, every future commit benefits from the same automated process.

---

# Further Reading

- GitHub Actions Documentation
- Pytest Documentation
- Coverage.py Documentation
- Python Official Documentation

---

# About This Capsule

**Ahmed Adawy Tech Capsules**

Professional technical micro-books designed for developers who prefer practical knowledge over lengthy theory.

Each capsule focuses on one topic, providing concise explanations, real-world examples, and immediately applicable best practices.

---

Thank you for reading.

Happy Coding!
