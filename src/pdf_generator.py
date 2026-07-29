"""
PDF Generator
Ahmed Adawy Tech Capsules
"""

from pathlib import Path
from weasyprint import HTML


class PDFGenerator:

    def generate(self, html: str, output_file: Path):

        HTML(string=html).write_pdf(output_file)

        return output_file
