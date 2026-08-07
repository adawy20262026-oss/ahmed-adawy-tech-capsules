from parser import (
    parse_markdown,
    Heading,
    Paragraph,
    Image,
    Table,
    MarkdownParser,
)


def test_parse_inline_formatting():

    nodes = parse_markdown(
        "This is **bold** and *italic* and `code`."
    )

    assert len(nodes) == 1
    assert isinstance(nodes[0], Paragraph)

    assert "<strong>bold</strong>" in nodes[0].text
    assert "<em>italic</em>" in nodes[0].text
    assert "<code>code</code>" in nodes[0].text


def test_parse_link():

    nodes = parse_markdown(
        "[OpenAI](https://openai.com)"
    )

    assert len(nodes) == 1
    assert isinstance(nodes[0], Paragraph)

    assert (
        '<a href="https://openai.com">OpenAI</a>'
        in nodes[0].text
    )


def test_parse_image():

    nodes = parse_markdown(
        "![Logo](logo.png)"
    )

    assert len(nodes) == 1
    assert isinstance(nodes[0], Image)

    assert nodes[0].src == "logo.png"
    assert nodes[0].alt == "Logo"


def test_parse_table():

    markdown = """
| Name | Age |
|------|-----|
| Alice | 20 |
| Bob | 30 |
"""

    nodes = parse_markdown(markdown)

    tables = [
        node
        for node in nodes
        if isinstance(node, Table)
    ]

    assert len(tables) == 1

    table = tables[0]

    assert table.header == [
        "Name",
        "Age",
    ]

    assert table.rows == [
        [
            "Alice",
            "20",
        ],
        [
            "Bob",
            "30",
        ],
    ]


def test_markdown_parser_parse():

    parser = MarkdownParser()

    nodes = parser.parse("# Title")

    assert len(nodes) == 1
    assert isinstance(nodes[0], Heading)
    assert nodes[0].text == "Title"


def test_markdown_parser_callable():

    parser = MarkdownParser()

    nodes = parser("# Title")

    assert len(nodes) == 1
    assert isinstance(nodes[0], Heading)
    assert nodes[0].text == "Title"
