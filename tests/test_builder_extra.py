from pathlib import Path

from builder import CapsuleBuilder


def test_build_all_empty(monkeypatch, tmp_path):

    import builder

    monkeypatch.setattr(builder, "CAPSULES_DIR", tmp_path)

    called = {"value": False}

    class FakeIndex:

        def generate(self, library):
            called["value"] = True
            assert library == []

    monkeypatch.setattr(builder, "IndexGenerator", FakeIndex)

    CapsuleBuilder().build_all()

    assert called["value"]


def test_build_returns_dictionary(monkeypatch, tmp_path):

    import builder

    md = tmp_path / "demo.md"

    md.write_text("# Demo")

    monkeypatch.setattr(builder.MetadataParser, "parse",
                        lambda self, text: ({}, text))

    monkeypatch.setattr(builder.MarkdownParser, "parse",
                        lambda self, text: [])

    monkeypatch.setattr(builder.OUTPUT_DIR, "mkdir",
                        lambda exist_ok=True: None)

    class FakePublisher:

        def html(self, document, metadata):
            return "<html></html>"

        def pdf_file(self, document, output, metadata):
            pass

    b = CapsuleBuilder()
    b.publisher = FakePublisher()

    result = b.build(md)

    assert isinstance(result, dict)

    assert result["file"] == "demo"
