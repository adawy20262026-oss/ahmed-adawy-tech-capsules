"""
Publishing Engine
Ahmed Adawy Tech Capsules
"""

from pathlib import Path

from .renderer import HTMLRenderer
from .pdf_generator import PDFGenerator


class Publisher:
    """
    Central publishing engine.

    Responsible for exporting a document
    into one or more output formats.
    """

    def __init__(self):
        self.renderer = HTMLRenderer()
        self.pdf = PDFGenerator()

    def html(self, document, metadata=None):
        return self.renderer.render(
            document,
            metadata,
        )

    def pdf_bytes(self, document, metadata=None):
        html = self.html(
            document,
            metadata,
        )

        return self.pdf.generate(html)

    def pdf_file(
        self,
        document,
        output_file: Path,
        metadata=None,
    ):
        html = self.html(
            document,
            metadata,
        )

        self.pdf.generate(
            html,
            output_file,
        )

        return output_file
