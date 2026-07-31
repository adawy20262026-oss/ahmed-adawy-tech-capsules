
"""
Content Renderer
Ahmed Adawy Tech Capsules
"""

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
                    f"<pre><code>{node.text}</code></pre>"
                )

            elif isinstance(node, Image):

                html.append(
                    f'<img src="{node.src}" alt="{node.alt}">'
                )

            elif isinstance(node, Table):

                table = ["<table>"]

                if node.header:

                    table.append("<tr>")

                    for h in node.header:

                        table.append(
                            f"<th>{h}</th>"
                        )

                    table.append("</tr>")

                for row in node.rows:

                    table.append("<tr>")

                    for cell in row:

                        table.append(
                            f"<td>{cell}</td>"
                        )

                    table.append("</tr>")

                table.append("</table>")

                html.append(
                    "\n".join(table)
                )

        return "\n".join(html)
