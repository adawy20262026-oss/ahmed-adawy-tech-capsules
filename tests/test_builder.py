from pathlib import Path

import pytest

from builder import CapsuleBuilder


def test_builder_creation():

    builder = CapsuleBuilder()

    assert builder is not None


def test_builder_has_publisher():

    builder = CapsuleBuilder()

    assert builder.publisher is not None


def test_build_missing_file():

    builder = CapsuleBuilder()

    with pytest.raises(RuntimeError):

        builder.build(
            Path("file_that_does_not_exist.md")
        )


def test_build_returns_dictionary(tmp_path):

    builder = CapsuleBuilder()

    capsule = tmp_path / "demo.md"

    capsule.write_text(
        "---\n"
        "title: Demo\n"
        "---\n"
        "# Hello",
        encoding="utf-8",
    )

    result = builder.build(capsule)

    assert isinstance(result, dict)

    assert result["title"] == "Demo"

    assert result["file"] == "demo"
