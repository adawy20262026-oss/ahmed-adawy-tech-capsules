"""
Content Renderer
Ahmed Adawy Tech Capsules
"""

from html import escape

from parser import (
    Heading,
    Paragraph,
    BulletList,
    CodeBlock,
    Image,
    Table,
)

from highlighter import SyntaxHighlighter


class ContentRenderer:

    def __init__(self):

        self.highlighter = SyntaxHighlighter()

    def render(self, document):

        html = []

        for node in document:

            if isinstance(node, Heading):

                html.append(
                    f"<h{node.level}>{node.text}</h{node.level}>"
                )

            elif isinstance(node, Paragraph):

                html.append(
                    f"<p>{node.text}</p>"
                )

            elif isinstance(node, BulletList):

                html.append("<ul>")

                for item in node.items:

                    html.append(
                        f"<li>{item}</li>"
                    )

                html.append("</ul>")

            elif isinstance(node, CodeBlock):

                html.append(
                    self.highlighter.highlight(
                        node.text,
                        node.language
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

                    table.append("<thead>")
                    table.append("<tr>")

                    for h in node.header:

                        table.append(
                            f"<th>{h}</th>"
                        )

                    table.append("</tr>")
                    table.append("</thead>")

                table.append("<tbody>")

                for row in node.rows:

                    table.append("<tr>")

                    for cell in row:

                        table.append(
                            f"<td>{cell}</td>"
                        )

                    table.append("</tr>")

                table.append("</tbody>")
                table.append("</table>")

                html.append(
                    "\n".join(table)
                )

            else:

                print(
                    f"Warning: Unsupported node "
                    f"{type(node).__name__}"
                )

        return "\n".join(html)
