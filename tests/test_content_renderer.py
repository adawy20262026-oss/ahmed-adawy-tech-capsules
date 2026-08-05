from content_renderer import ContentRenderer
from parser import (
    Heading,
    Paragraph,
    BulletList,
    CodeBlock,
    Image,
    Table,
)


def test_renderer_creation():

    renderer = ContentRenderer()

    assert renderer is not None


def test_render_heading():

    renderer = ContentRenderer()

    html = renderer.render([
        Heading(1, "Hello")
    ])

    assert '<h1 id="hello">Hello</h1>' in html


def test_render_paragraph():

    renderer = ContentRenderer()

    html = renderer.render([
        Paragraph("Hello World")
    ])

    assert "<p>Hello World</p>" in html


def test_render_bullet_list():

    renderer = ContentRenderer()

    html = renderer.render([
        BulletList(["One", "Two"])
    ])

    assert "<ul>" in html
    assert "<li>One</li>" in html
    assert "<li>Two</li>" in html
    assert "</ul>" in html


def test_render_image():

    renderer = ContentRenderer()

    html = renderer.render([
        Image("image.png", "Logo")
    ])

    assert 'src="image.png"' in html
    assert 'alt="Logo"' in html


def test_render_table():

    renderer = ContentRenderer()

    html = renderer.render([
        Table(
            ["A", "B"],
            [["1", "2"]]
        )
    ])

    assert "<table>" in html
    assert "<th>A</th>" in html
    assert "<td>1</td>" in html
    assert "</table>" in html


def test_render_code_block():

    renderer = ContentRenderer()

    html = renderer.render([
        CodeBlock(
            "print('Hello')",
            "python",
        )
    ])

    assert isinstance(html, str)
