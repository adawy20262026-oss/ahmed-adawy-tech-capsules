"""
Capsule Builder
Ahmed Adawy Tech Capsules
"""

from pathlib import Path

from config import (
    OUTPUT_DIR,
    CAPSULES_DIR,
    DEFAULT_ENCODING,
)

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
                encoding=DEFAULT_ENCODING
            )

            metadata, markdown = (
                MetadataParser().parse(text)
            )

            document = MarkdownParser().parse(
                markdown
            )

            OUTPUT_DIR.mkdir(
                exist_ok=True
            )

            capsule_name = source.stem

            html = self.publisher.html(
                document,
                metadata
            )

            html_file = (
                OUTPUT_DIR / f"{capsule_name}.html"
            )

            pdf_file = (
                OUTPUT_DIR / f"{capsule_name}.pdf"
            )

            html_file.write_text(
                html,
                encoding=DEFAULT_ENCODING
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
                "title": metadata.get(
                    "title",
                    capsule_name,
                ),
                "subtitle": metadata.get(
                    "subtitle",
                    "",
                ),
                "category": metadata.get(
                    "category",
                    "-",
                ),
                "difficulty": metadata.get(
                    "difficulty",
                    "Beginner",
                ),
                "language": metadata.get(
                    "language",
                    "en",
                ),
                "version": metadata.get(
                    "version",
                    "1.0",
                ),
            }

        except Exception as exc:

            print(
                f"✗ Failed to build {source.name}"
            )

            raise RuntimeError(
                f"Error while building "
                f"'{source.name}': {exc}"
            ) from exc

    def build_all(self):

        library = []

        for source in sorted(
            CAPSULES_DIR.glob("*.md")
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
