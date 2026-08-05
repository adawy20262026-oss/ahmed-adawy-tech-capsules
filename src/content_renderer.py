"""
Content Renderer
Ahmed Adawy Tech Capsules
"""

from html import escape

from highlighter import SyntaxHighlighter
from parser import (
    BulletList,
    CodeBlock,
    Heading,
    Image,
    Paragraph,
    Table,
)


class ContentRenderer:

    def __init__(self):

        self.highlighter = SyntaxHighlighter()

    def render(self, document):

        html = []

        for node in document:

            if isinstance(node, Heading):

                heading_id = (
                    node.text.lower()
                    .replace(" ", "-")
                    .replace(".", "")
                    .replace(",", "")
                    .replace(":", "")
                    .replace("/", "-")
                )

                html.append(
                    f'<h{node.level} id="{heading_id}">'
                    f'{escape(node.text)}'
                    f'</h{node.level}>'
                )

            elif isinstance(node, Paragraph):

                html.append(
                    f"<p>{escape(node.text)}</p>"
                )

            elif isinstance(node, BulletList):

                html.append("<ul>")

                for item in node.items:

                    html.append(
                        f"<li>{escape(item)}</li>"
                    )

                html.append("</ul>")

            elif isinstance(node, CodeBlock):

                html.append(

                    self.highlighter.highlight(
                        node.text,
                        node.language,
                    )

                )

            elif isinstance(node, Image):

                html.append(

                    f'<img src="{escape(node.src)}" '
                    f'alt="{escape(node.alt)}">'

                )

            elif isinstance(node, Table):

                table = ["<table>"]

                if node.header:

                    table.extend(
                        [
                            "<thead>",
                            "<tr>",
                        ]
                    )

                    for header in node.header:

                        table.append(
                            f"<th>{escape(header)}</th>"
                        )

                    table.extend(
                        [
                            "</tr>",
                            "</thead>",
                        ]
                    )

                table.append("<tbody>")

                for row in node.rows:

                    table.append("<tr>")

                    for cell in row:

                        table.append(
                            f"<td>{escape(cell)}</td>"
                        )

                    table.append("</tr>")

                table.extend(
                    [
                        "</tbody>",
                        "</table>",
                    ]
                )

                html.append(
                    "\n".join(table)
                )

            else:

                print(
                    "Warning: Unsupported node "
                    f"{type(node).__name__}"
                )

        return "\n".join(html)
