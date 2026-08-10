"""
PDF Generator
Ahmed Adawy Tech Capsules
"""

from io import BytesIO
from pathlib import Path

from weasyprint import HTML


class PDFGenerator:
    """
    Generates PDF documents from HTML.

    If output_file is provided, the PDF is saved
    to that path and the path is returned.

    If output_file is not provided, PDF bytes
    are returned for web applications and APIs.
    """

    def generate(
        self,
        html: str,
        output_file: Path | None = None,
    ):
        if output_file is None:
            pdf = BytesIO()

            HTML(string=html).write_pdf(pdf)

            return pdf.getvalue()

        HTML(string=html).write_pdf(output_file)

        return output_file
