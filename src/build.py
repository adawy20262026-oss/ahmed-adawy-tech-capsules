"""
Build Entry Point
Ahmed Adawy Tech Capsules
"""

from pathlib import Path
import sys

from builder import CapsuleBuilder
from index_generator import IndexGenerator
from site_generator import SiteGenerator
from metadata import MetadataParser


def main():

    builder = CapsuleBuilder()

    capsules = []

    capsule_dir = Path("capsules")

    if len(sys.argv) > 1:

        builder.build(Path(sys.argv[1]))

    else:

        builder.build_all()

        parser = MetadataParser()

        for file in sorted(capsule_dir.glob("*.md")):

            text = file.read_text(encoding="utf-8")

            metadata, _ = parser.parse(text)

            metadata["file"] = file.stem

            capsules.append(metadata)

        IndexGenerator().generate(capsules)

        SiteGenerator().generate()

    print("Build completed successfully.")


if __name__ == "__main__":
    main()
