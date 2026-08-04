from highlighter import SyntaxHighlighter


def test_highlight_plain_text():

    highlighter = SyntaxHighlighter()

    html = highlighter.highlight(
        "hello world"
    )

    assert "hello world" in html


def test_highlight_python():

    highlighter = SyntaxHighlighter()

    html = highlighter.highlight(
        "print('Hello')",
        "python",
    )

    assert "print" in html
    assert "highlight" in html


def test_highlight_unknown_language():

    highlighter = SyntaxHighlighter()

    html = highlighter.highlight(
        "hello",
        "this_language_does_not_exist",
    )

    assert "hello" in html


def test_css():

    highlighter = SyntaxHighlighter()

    css = highlighter.css()

    assert ".highlight" in css
