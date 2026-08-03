from pathlib import Path

from site_generator import SiteGenerator


def test_generate_site(tmp_path, monkeypatch):

    output = tmp_path / "output"
    docs = tmp_path / "docs"

    output.mkdir()

    (output / "index.html").write_text("index")
    (output / "capsule1.html").write_text("html")
    (output / "capsule1.pdf").write_text("pdf")

    monkeypatch.setattr(
        "site_generator.OUTPUT_DIR",
        output,
    )

    monkeypatch.setattr(
        "site_generator.DOCS_DIR",
        docs,
    )

    SiteGenerator().generate()

    assert (docs / "library" / "index.html").exists()

    assert (
        docs / "capsules" / "capsule1.html"
    ).exists()

    assert (
        docs / "pdf" / "capsule1.pdf"
    ).exists()


def test_generate_without_library_index(
    tmp_path,
    monkeypatch,
):

    output = tmp_path / "output"
    docs = tmp_path / "docs"

    output.mkdir()

    (output / "only.html").write_text("html")
    (output / "only.pdf").write_text("pdf")

    monkeypatch.setattr(
        "site_generator.OUTPUT_DIR",
        output,
    )

    monkeypatch.setattr(
        "site_generator.DOCS_DIR",
        docs,
    )

    SiteGenerator().generate()

    assert (
        docs / "capsules" / "only.html"
    ).exists()

    assert (
        docs / "pdf" / "only.pdf"
    ).exists()

    assert not (
        docs / "library" / "index.html"
    ).exists()
