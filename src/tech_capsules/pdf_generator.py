from io import BytesIO
from pathlib import Path
from weasyprint import HTML


class PDFGenerator:

    def generate(self, html: str, output_file: Path | None = None):
        """
        إذا تم تمرير output_file:
            يحفظ الملف ويرجع المسار.

        إذا لم يتم تمرير output_file:
            يرجع PDF Bytes (لاستخدام Streamlit).
        """

        if output_file is None:
            pdf = BytesIO()
            HTML(string=html).write_pdf(pdf)
            return pdf.getvalue()

        HTML(string=html).write_pdf(output_file)
        return output_file
