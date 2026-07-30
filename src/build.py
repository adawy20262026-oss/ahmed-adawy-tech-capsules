import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from renderer import HTMLRenderer
from pathlib import Path
from parser import MarkdownParser
from renderer import HTMLRenderer
from pdf_generator import PDFGenerator

SOURCE = Path("capsules/linux-cli-essentials.md")
OUTPUT_HTML = Path("output/book.html")
OUTPUT_PDF = Path("output/book.pdf")


def main():
    if not SOURCE.exists():
        print(f"Error: Source file {SOURCE} does not exist.")
        return

    markdown = SOURCE.read_text(encoding="utf-8")

    parser = MarkdownParser()
    document = parser.parse(markdown)

    renderer = HTMLRenderer()
    html = renderer.render(document)

    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(html, encoding="utf-8")
    print("HTML generated successfully.")

    try:
        pdf = PDFGenerator()
        pdf.generate(html, OUTPUT_PDF)
        print("PDF generated successfully.")
    except Exception as e:
        print(f"Failed to generate PDF: {e}")
        raise e


if __name__ == "__main__":
    main()
