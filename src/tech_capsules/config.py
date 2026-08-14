"""
Project Configuration
Ahmed Adawy Tech Capsules
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


CAPSULES_DIR = PROJECT_ROOT / "capsules"

OUTPUT_DIR = PROJECT_ROOT / "output"

DOCS_DIR = PROJECT_ROOT / "docs"

ASSETS_DIR = PROJECT_ROOT / "assets"

TEMPLATES_DIR = PROJECT_ROOT / "templates"


DEFAULT_ENCODING = "utf-8"

DEFAULT_LANGUAGE = "English"

DEFAULT_AUTHOR = "Ahmed Adawy"

PROJECT_NAME = "Ahmed Adawy Tech Capsules"

VERSION = "0.7.0"
