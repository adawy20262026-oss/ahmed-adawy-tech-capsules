"""
HTML Renderer
Ahmed Adawy Tech Capsules
"""

from styles import get_styles
from cover import CoverRenderer
from content_renderer import ContentRenderer
from footer import FooterRenderer


class HTMLRenderer:

    def render(self, document, metadata):

        html = []

        html.append(self.header())

        html.append(
            CoverRenderer().render(metadata)
        )

        html.append(
            ContentRenderer().render(document)
        )

        html.append(
            FooterRenderer().render()
        )

        return "\n".join(html)

    def header(self):

        return f"""<!DOCTYPE html>
<html>

<head>

<meta charset="utf-8">

<title>Tech Capsule</title>

<style>

{get_styles()}

</style>

</head>

<body>
"""
