"""
Capsule Builder
Ahmed Adawy Tech Capsules
"""

from pathlib import Path

from parser import MarkdownParser
from renderer import HTMLRenderer
from pdf_generator import PDFGenerator


class CapsuleBuilder:

    def build(self, source: Path):

        markdown = source.read_text(encoding="utf-8")

        parser = MarkdownParser()
        document = parser.parse(markdown)

        renderer = HTMLRenderer()
        html = renderer.render(document)

        output = Path("output")
        output.mkdir(exist_ok=True)

        capsule_name = source.stem

        html_file = output / f"{capsule_name}.html"
        pdf_file = output / f"{capsule_name}.pdf"

        html_file.write_text(
            html,
            encoding="utf-8"
        )

        PDFGenerator().generate(
            html,
            pdf_file
        )

        return html_file, pdf_file
