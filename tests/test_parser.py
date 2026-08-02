
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from parser import (
    MarkdownParser,
    Heading,
    Paragraph,
    BulletList,
    CodeBlock,
)


def test_parse_heading():
    parser = MarkdownParser()

    document = parser.parse("# Hello")

    assert len(document) == 1
    assert isinstance(document[0], Heading)
    assert document[0].text == "Hello"
    assert document[0].level == 1


def test_parse_paragraph():
    parser = MarkdownParser()

    document = parser.parse("This is a paragraph.")

    assert len(document) == 1
    assert isinstance(document[0], Paragraph)
    assert "This is a paragraph." in document[0].text


def test_parse_list():
    parser = MarkdownParser()

    document = parser.parse(
        "- Apple\n"
        "- Banana\n"
        "- Orange"
    )

    assert len(document) == 1
    assert isinstance(document[0], BulletList)
    assert len(document[0].items) == 3


def test_parse_code_block():
    parser = MarkdownParser()

    markdown = (
        "```python\n"
        "print('Hello')\n"
        "```"
    )

    document = parser.parse(markdown)

    assert len(document) == 1
    assert isinstance(document[0], CodeBlock)
    assert "print" in document[0].text


def test_empty_document():
    parser = MarkdownParser()

    document = parser.parse("")

    assert isinstance(document, list)
