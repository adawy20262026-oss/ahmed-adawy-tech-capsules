"""
HTML Renderer
Ahmed Adawy Tech Capsules
"""

from styles import get_styles
from cover import CoverRenderer
from toc import TOCRenderer
from content_renderer import ContentRenderer
from footer import FooterRenderer


class HTMLRenderer:
    """
    Main HTML renderer.

    Supports both:

    renderer.render(document)

    and

    renderer.render(document, metadata)

    so Streamlit and Builder use the same engine.
    """

    def render(self, document, metadata=None):

        if metadata is None:
            metadata = {}

        html = []

        html.append(self.header())

        # Cover Page
        if metadata:
            html.append(
                CoverRenderer().render(metadata)
            )

        # Table of Contents
        toc_html = TOCRenderer().render(document)

        if toc_html:
            html.append(toc_html)

        # Main Content
        html.append(
            ContentRenderer().render(document)
        )

        # Footer
        html.append(
            FooterRenderer().render()
        )

        html.append("</body>")
        html.append("</html>")

        return "\n".join(html)

    def header(self):

        return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="utf-8">

<title>Tech Capsule</title>

<style>

{get_styles()}

</style>

</head>

<body>
"""
