"""
Static Site Generator
Ahmed Adawy Tech Capsules
"""

import shutil

from .config import OUTPUT_DIR, DOCS_DIR


class SiteGenerator:

    def generate(self):

        DOCS_DIR.mkdir(parents=True, exist_ok=True)

        (DOCS_DIR / "library").mkdir(
            exist_ok=True
        )

        (DOCS_DIR / "capsules").mkdir(
            exist_ok=True
        )

        (DOCS_DIR / "pdf").mkdir(
            exist_ok=True
        )

        # Copy Library Index
        library = OUTPUT_DIR / "index.html"

        if library.exists():

            shutil.copy(
                library,
                DOCS_DIR / "library" / "index.html",
            )

        # Copy HTML Capsules
        for html in OUTPUT_DIR.glob("*.html"):

            if html.name == "index.html":
                continue

            shutil.copy(
                html,
                DOCS_DIR / "capsules" / html.name,
            )

        # Copy PDF Capsules
        for pdf in OUTPUT_DIR.glob("*.pdf"):

            shutil.copy(
                pdf,
                DOCS_DIR / "pdf" / pdf.name,
            )

        print(
            "Static website generated successfully."
        )
