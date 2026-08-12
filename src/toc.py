"""
Table of Contents Renderer
Ahmed Adawy Tech Capsules
"""

from .parser import Heading

class TOCRenderer:
    """
    Generates an HTML Table of Contents
    from parsed Heading nodes.
    """

    def render(self, document):

        # Collect all heading nodes
        headings = [
            node
            for node in document
            if isinstance(node, Heading)
        ]

        if not headings:
            return ""

        # The first H1 is the capsule title.
        # It should not appear in the Table of Contents.
        title_heading = headings[0]

        toc_headings = [
            node
            for node in headings[1:]
            if node.level == 1
        ]

        if not toc_headings:
            return ""

        html = [
            '<div class="toc">',
            "<h2>Table of Contents</h2>",
            "<ul>",
        ]

        for heading in toc_headings:
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
