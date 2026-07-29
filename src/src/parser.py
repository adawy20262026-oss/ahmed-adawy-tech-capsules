"""
Markdown Parser
"""

from pathlib import Path


def read_capsule(path):
    """Read markdown capsule."""

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":

    capsule = Path("../capsules/linux-cli.md")

    print(read_capsule(capsule))
