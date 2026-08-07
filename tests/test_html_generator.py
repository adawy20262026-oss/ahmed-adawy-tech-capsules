from html_generator import generate_html


def test_generate_html_contains_body():

    html = generate_html("# Hello")

    assert "<body>" in html
    assert "</body>" in html


def test_generate_html_contains_markdown():

    text = "# Ahmed Adawy"

    html = generate_html(text)

    assert text in html


def test_generate_html_returns_string():

    html = generate_html("Test")

    assert isinstance(html, str)
