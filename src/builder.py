"""
Capsule Builder
Ahmed Adawy Tech Capsules
"""

from pathlib import Path

from parser import MarkdownParser
from renderer import HTMLRenderer
from pdf_generator import PDFGenerator
from metadata import MetadataParser
from index_generator import IndexGenerator


class CapsuleBuilder:

    def build(self, source: Path):

        text = source.read_text(encoding="utf-8")

        metadata_parser = MetadataParser()
        metadata, markdown = metadata_parser.parse(text)

        parser = MarkdownParser()
        document = parser.parse(markdown)

        renderer = HTMLRenderer()

        html = renderer.render(
            document,
            metadata
        )

        print(html[:500])
        
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

        return {
    "file": capsule_name,
    "title": metadata.get("title", capsule_name),
    "subtitle": metadata.get("subtitle", ""),
    "category": metadata.get("category", "-"),
    "difficulty": metadata.get("difficulty", "Beginner"),
    "language": metadata.get("language", "en"),
    "version": metadata.get("version", "-")
        }

    def build_all(self):

        capsules_dir = Path("capsules")

        library = []

        for source in sorted(capsules_dir.glob("*.md")):

            print(f"Building {source.name}")

            library.append(
                self.build(source)
            )

        IndexGenerator().generate(
            library
        )

        print("All capsules generated successfully.")
