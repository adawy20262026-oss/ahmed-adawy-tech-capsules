
from builder import CapsuleBuilder


def test_builder_creation():
    builder = CapsuleBuilder()

    assert builder is not None


def test_builder_has_build():
    builder = CapsuleBuilder()

    assert hasattr(builder, "build")


def test_builder_has_build_all():
    builder = CapsuleBuilder()

    assert hasattr(builder, "build_all")
