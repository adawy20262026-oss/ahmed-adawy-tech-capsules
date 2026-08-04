from pathlib import Path
from unittest.mock import patch

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


def test_build_all():

    builder = CapsuleBuilder()

    fake_result = {
        "file": "demo",
        "title": "Demo",
        "subtitle": "",
        "category": "Python",
        "difficulty": "Beginner",
        "language": "en",
        "version": "1.0",
    }

    with patch.object(
        CapsuleBuilder,
        "build",
        return_value=fake_result,
    ) as build_mock:

        with patch(
            "builder.CAPSULES_DIR.glob",
            return_value=[
                Path("one.md"),
                Path("two.md"),
            ],
        ):

            with patch(
                "builder.IndexGenerator.generate"
            ) as generate_mock:

                builder.build_all()

                assert build_mock.call_count == 2

                generate_mock.assert_called_once_with(
                    [fake_result, fake_result]
                )
