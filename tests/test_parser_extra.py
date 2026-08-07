from parser import (
    parse_markdown,
    Heading,
    Paragraph,
    BulletList,
    CodeBlock,
    Image,
    Table,
)


def test_parse_inline_formatting():

    nodes = parse_markdown(
        "This is **bold** and *italic* and `code`."
    )

    assert isinstance(nodes[0], Paragraph)

    assert "<strong>bold</strong>" in nodes[0].text

    assert "<em>italic</em>" in nodes[0].text

    assert "<code>code</code>" in nodes[0].text


def test_parse_link():

    nodes = parse_markdown(
        "[OpenAI](https://openai.com)"
    )

    assert isinstance(nodes[0], Paragraph)

    assert "<a href=\"https://openai.com\">OpenAI</a>" in nodes[0].text


def test_parse_image():

    nodes = parse_markdown(
        "![Logo](logo.png)"
    )

    assert isinstance(nodes[0], Image)

    assert nodes[0].src == "logo.png"

    assert nodes[0].alt == "Logo"


def test_parse_table():

    markdown = (
        "| Name | Age |
"
        "|------|-----|
"
        "| Alice | 20 |
"
        "| Bob | 30 |"
    )

    nodes = parse_markdown(markdown)

    table = next(node for node in nodes if isinstance(node, Table))

    assert table.header == ["Name", "Age"]

    assert table.rows == [["Alice", "20"], ["Bob", "30"]]


def test_markdown_parser_wrapper():

    from parser import MarkdownParser

    parser = MarkdownParser()

    nodes = parser.parse("# Title")

    assert isinstance(nodes[0], Heading)


def test_markdown_parser_callable():

    from parser import MarkdownParser

    parser = MarkdownParser()

    nodes = parser("# Title")

    assert isinstance(nodes[0], Heading)
