"""
Table of Contents Renderer
Ahmed Adawy Tech Capsules
"""

from parser import Heading


class TOCRenderer:
    """
    Generates an HTML Table of Contents
    from parsed Heading nodes.
    """

    MAX_LEVEL = 3

    def render(self, document):

        headings = [
            node
            for node in document
            if isinstance(node, Heading)
            and node.level <= self.MAX_LEVEL
        ]

        if not headings:
            return ""

        html = [
            '<div class="toc">',
            "<h2>Table of Contents</h2>",
            "<ul>",
        ]

        for heading in headings:

            html.append(
                f'<li class="level-{heading.level}">'
                f"{heading.text}"
                "</li>"
            )

        html.extend(
            [
                "</ul>",
                "</div>",
            ]
        )

        return "\n".join(html)
