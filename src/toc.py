"""
Table of Contents Generator
Ahmed Adawy Tech Capsules
"""

from parser import Heading


class TOCGenerator:

    def render(self, document):

        headings = []

        for node in document:

            if isinstance(node, Heading):

                headings.append(
                    (node.level, node.text)
                )

        if not headings:
            return ""

        html = []

        html.append('<div class="toc">')
        html.append("<h2>Table of Contents</h2>")
        html.append("<ul>")

        for level, text in headings:

            indent = (level - 1) * 20

            html.append(
                f'<li style="margin-left:{indent}px;">{text}</li>'
            )

        html.append("</ul>")
        html.append("</div>")

        return "\n".join(html)
