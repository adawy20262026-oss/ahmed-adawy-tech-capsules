from pathlib import Path

from tech_capsules.publisher import Publisher

def test_publisher_creation():

    publisher = Publisher()

    assert publisher is not None


def test_html_returns_string():

    publisher = Publisher()

    html = publisher.html([])

    assert isinstance(html, str)
    assert "<html" in html


def test_pdf_bytes_returns_bytes():

    publisher = Publisher()

    pdf = publisher.pdf_bytes([])

    assert isinstance(pdf, bytes)


def test_pdf_file_returns_path(tmp_path):

    publisher = Publisher()

    output = tmp_path / "sample.pdf"

    result = publisher.pdf_file(
        [],
        output
    )

    assert result == output


def test_renderer_exists():

    publisher = Publisher()

    assert publisher.renderer is not None


def test_pdf_generator_exists():

    publisher = Publisher()

    assert publisher.pdf is not None
