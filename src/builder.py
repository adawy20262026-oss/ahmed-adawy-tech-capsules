"""
Capsule Builder
Ahmed Adawy Tech Capsules
"""

from pathlib import Path

from parser import MarkdownParser
from renderer_v2 import HTMLRenderer
from pdf_generator import PDFGenerator
from metadata import MetadataParser
from index_generator import IndexGenerator


class CapsuleBuilder:

    def build(self, source: Path):

        text = source.read_text(encoding="utf-8")

        metadata_parser = MetadataParser()
        metadata, markdown = metadata_parser.parse(text)

        print("Metadata:", metadata)

        parser = MarkdownParser()
        document = parser.parse(markdown)

        renderer = HTMLRenderer()

        html = renderer.render(
            document,
            metadata
        )

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

        return capsule_name

    def build_all(self):

        capsules_dir = Path("capsules")

        built_capsules = []

        for source in sorted(capsules_dir.glob("*.md")):

            print(f"Building {source.name}")

            capsule_name = self.build(source)

            built_capsules.append(capsule_name)

        IndexGenerator().generate(
            built_capsules
        )

        print("All capsules generated successfully.")
