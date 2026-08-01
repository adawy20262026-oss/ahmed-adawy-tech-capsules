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


class ContentRenderer:

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
                    "<pre><code>"
                    f"{escape(node.text)}"
                    "</code></pre>"
                )

            elif isinstance(node, Image):

                html.append(
                    f'<img src="{escape(node.src)}" '
                    f'alt="{escape(node.alt)}" '
                    'style="max-width:100%;height:auto;">'
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
