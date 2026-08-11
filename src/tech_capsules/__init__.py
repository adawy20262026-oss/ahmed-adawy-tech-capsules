"""
Ahmed Adawy Tech Capsules

Professional publishing engine for building
technical micro-books from Markdown.
"""

from .builder import CapsuleBuilder
from .parser import MarkdownParser
from .renderer import HTMLRenderer
from .pdf_generator import PDFGenerator


__version__ = "0.7.0"


__all__ = [
    "CapsuleBuilder",
    "MarkdownParser",
    "HTMLRenderer",
    "PDFGenerator",
]
