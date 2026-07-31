"""
Static Site Generator
Ahmed Adawy Tech Capsules
"""

from pathlib import Path
import shutil


class SiteGenerator:

    def generate(self):

        output = Path("output")
        docs = Path("docs")

        docs.mkdir(exist_ok=True)

        # إنشاء المجلدات المطلوبة
        (docs / "library").mkdir(exist_ok=True)
        (docs / "capsules").mkdir(exist_ok=True)
        (docs / "pdf").mkdir(exist_ok=True)

        # نسخ صفحة المكتبة
        library = output / "index.html"

        if library.exists():
            shutil.copy(
                library,
                docs / "library" / "index.html"
            )

        # نسخ ملفات HTML
        for html in output.glob("*.html"):

            if html.name == "index.html":
                continue

            shutil.copy(
                html,
                docs / "capsules" / html.name
            )

        # نسخ ملفات PDF
        for pdf in output.glob("*.pdf"):

            shutil.copy(
                pdf,
                docs / "pdf" / pdf.name
            )

        print("Static website generated successfully.")
