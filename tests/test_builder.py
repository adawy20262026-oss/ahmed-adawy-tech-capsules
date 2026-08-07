from pathlib import Path

import pytest

import builder
from builder import CapsuleBuilder


def test_builder_creation():

    obj = CapsuleBuilder()

    assert obj is not None


def test_builder_has_publisher():

    obj = CapsuleBuilder()

    assert obj.publisher is not None


def test_build_missing_file():

    obj = CapsuleBuilder()

    with pytest.raises(RuntimeError):

        obj.build(
            Path("file_that_does_not_exist.md")
        )


def test_build_returns_dictionary(tmp_path):

    obj = CapsuleBuilder()

    capsule = tmp_path / "demo.md"

    capsule.write_text(
        "---\n"
        "title: Demo\n"
        "---\n"
        "# Hello",
        encoding="utf-8",
    )

    builder.OUTPUT_DIR = tmp_path

    result = obj.build(capsule)

    assert isinstance(result, dict)

    assert result["title"] == "Demo"

    assert result["file"] == "demo"


