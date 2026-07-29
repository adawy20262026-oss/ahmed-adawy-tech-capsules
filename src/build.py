from pathlib import Path

from parser import MarkdownParser
from renderer import HTMLRenderer


SOURCE = Path("capsules/example.md")

OUTPUT = Path("output/book.html")


def main():

    markdown = SOURCE.read_text(
        encoding="utf-8"
    )

    parser = MarkdownParser()

    document = parser.parse(markdown)

    renderer = HTMLRenderer()

    html = renderer.render(document)

    OUTPUT.parent.mkdir(
        exist_ok=True
    )

    OUTPUT.write_text(
        html,
        encoding="utf-8"
    )

    print("Book generated successfully.")


if __name__ == "__main__":
    main()
