from renderer import HTMLRenderer


def test_renderer_returns_html():

    renderer = HTMLRenderer()

    html = renderer.render([])

    assert "<html" in html
    assert "</html>" in html


def test_renderer_contains_body():

    renderer = HTMLRenderer()

    html = renderer.render([])

    assert "<body>" in html
    assert "</body>" in html


def test_renderer_contains_title():

    renderer = HTMLRenderer()

    html = renderer.render([])

    assert "<title>" in html
    assert "Tech Capsule" in html
