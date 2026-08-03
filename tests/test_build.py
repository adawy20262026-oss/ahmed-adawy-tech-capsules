from pathlib import Path

import build


def test_main_build_all(monkeypatch, tmp_path):

    class FakeBuilder:
        def build_all(self):
            pass

    class FakeParser:
        def parse(self, text):
            return {}, ""

    class FakeIndex:
        def generate(self, capsules):
            pass

    class FakeSite:
        def generate(self):
            pass

    monkeypatch.setattr(build, "CapsuleBuilder", FakeBuilder)
    monkeypatch.setattr(build, "MetadataParser", FakeParser)
    monkeypatch.setattr(build, "IndexGenerator", FakeIndex)
    monkeypatch.setattr(build, "SiteGenerator", FakeSite)

    monkeypatch.setattr(
        build,
        "CAPSULES_DIR",
        tmp_path,
    )

    (tmp_path / "demo.md").write_text(
        "---\ntitle: Demo\n---\nHello",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        build.sys,
        "argv",
        ["build.py"],
    )

    build.main()


def test_main_single_file(monkeypatch):

    called = {}

    class FakeBuilder:
        def build(self, path):
            called["path"] = path

    monkeypatch.setattr(build, "CapsuleBuilder", FakeBuilder)

    monkeypatch.setattr(
        build.sys,
        "argv",
        ["build.py", "demo.md"],
    )

    build.main()

    assert called["path"] == Path("demo.md")
