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

    def render(self, document):

        headings = []

        for node in document:

            if isinstance(node, Heading):

                if node.level <= 3:

                    headings.append(node)

        if not headings:
            return ""

        html = []

        html.append('<div class="toc">')

        html.append("<h2>Table of Contents</h2>")

        html.append("<ul>")

        for heading in headings:

            html.append(
                f'<li class="level-{heading.level}">'
                f'{heading.text}'
                "</li>"
            )

        html.append("</ul>")

        html.append("</div>")

        return "\n".join(html)
