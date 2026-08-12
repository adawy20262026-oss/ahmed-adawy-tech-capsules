"""
Build Entry Point
Ahmed Adawy Tech Capsules
"""

import sys
from pathlib import Path

from config import (
    CAPSULES_DIR,
    DEFAULT_ENCODING,
)

from builder import CapsuleBuilder
from metadata import MetadataParser
from index_generator import IndexGenerator
from site_generator import SiteGenerator


def main():

    builder = CapsuleBuilder()

    if len(sys.argv) > 1:

        builder.build(
            Path(sys.argv[1])
        )

        print(
            "Build completed successfully."
        )

        return

    builder.build_all()

    parser = MetadataParser()

    capsules = []

    for file in sorted(
        CAPSULES_DIR.glob("*.md")
    ):

        metadata, _ = parser.parse(

            file.read_text(
                encoding=DEFAULT_ENCODING
            )

        )

        metadata["file"] = file.stem

        capsules.append(
            metadata
        )

    IndexGenerator().generate(
        capsules
    )

    SiteGenerator().generate()

    print(
        "Build completed successfully."
    )


if __name__ == "__main__":

    main()
