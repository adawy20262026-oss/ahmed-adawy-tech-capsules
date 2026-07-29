"""
Tech Capsules Markdown Parser
Author: Ahmed Adawy
"""

from dataclasses import dataclass


@dataclass
class Heading:
    level: int
    text: str


@dataclass
class Paragraph:
    text: str


@dataclass
class BulletList:
    items: list[str]


class MarkdownParser:
    def parse(self, text: str):
        document = []

        lines = text.splitlines()

        i = 0

        while i < len(lines):

            line = lines[i].strip()

            if not line:
                i += 1
                continue

            # Heading
            if line.startswith("#"):

                level = len(line) - len(line.lstrip("#"))

                text = line[level:].strip()

                document.append(
                    Heading(level, text)
                )

                i += 1
                continue

            # Bullet List
            if line.startswith("- "):

                items = []

                while i < len(lines):

                    current = lines[i].strip()

                    if current.startswith("- "):
                        items.append(current[2:].strip())
                        i += 1
                    else:
                        break

                document.append(
                    BulletList(items)
                )

                continue

            # Paragraph

            paragraph = []

            while i < len(lines):

                current = lines[i].strip()

                if (
                    not current
                    or current.startswith("#")
                    or current.startswith("- ")
                ):
                    break

                paragraph.append(current)

                i += 1

            document.append(
                Paragraph(" ".join(paragraph))
            )

        return document
