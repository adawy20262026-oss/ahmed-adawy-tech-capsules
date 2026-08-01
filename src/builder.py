"""
Capsule Builder
Ahmed Adawy Tech Capsules
"""

from pathlib import Path

from parser import MarkdownParser
from metadata import MetadataParser
from publisher import Publisher
from index_generator import IndexGenerator


class CapsuleBuilder:

    def __init__(self):

        self.publisher = Publisher()

    def build(self, source: Path):

        print(f"Building {source.name}")

        try:

            text = source.read_text(
                encoding="utf-8"
            )

            metadata, markdown = (
                MetadataParser().parse(text)
            )

            document = MarkdownParser().parse(
                markdown
            )

            output = Path("output")
            output.mkdir(exist_ok=True)

            capsule_name = source.stem

            html = self.publisher.html(
                document,
                metadata
            )

            html_file = (
                output / f"{capsule_name}.html"
            )

            pdf_file = (
                output / f"{capsule_name}.pdf"
            )

            html_file.write_text(
                html,
                encoding="utf-8"
            )

            self.publisher.pdf_file(
                document,
                pdf_file,
                metadata
            )

            print(
                f"✓ {capsule_name}.pdf generated successfully"
            )

            return {
                "file": capsule_name,
                "title": metadata["title"],
                "subtitle": metadata["subtitle"],
                "category": metadata["category"],
                "difficulty": metadata["difficulty"],
                "language": metadata["language"],
                "version": metadata["version"],
            }

        except Exception as exc:

            print(
                f"✗ Failed to build {source.name}"
            )

            raise RuntimeError(
                f"Error while building '{source.name}': {exc}"
            ) from exc

    def build_all(self):

        capsules_dir = Path("capsules")

        library = []

        for source in sorted(
            capsules_dir.glob("*.md")
        ):

            library.append(
                self.build(source)
            )

        IndexGenerator().generate(
            library
        )

        print(
            "All capsules generated successfully."
        )
