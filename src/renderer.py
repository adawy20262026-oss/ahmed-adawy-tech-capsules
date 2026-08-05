"""
HTML Renderer
Ahmed Adawy Tech Capsules
"""

try:
    from .styles import get_styles
    from .cover import CoverRenderer
    from .toc import TOCRenderer
    from .content_renderer import ContentRenderer
    from .footer import FooterRenderer

except ModuleNotFoundError:
    from styles import get_styles
    from cover import CoverRenderer
    from toc import TOCRenderer
    from content_renderer import ContentRenderer
    from footer import FooterRenderer


class HTMLRenderer:
    """
    Main HTML renderer.

    Responsible for converting a parsed document
    into a complete HTML page.
    """

    def render(self, document, metadata=None):

        metadata = metadata or {}

        template = metadata.get(
            "template",
            "default"
        )

        html = [

            self.header(template)

        ]

        if metadata:

            html.append(
                CoverRenderer().render(metadata)
            )

        toc = TOCRenderer().render(
            document
        )

        if toc:

            html.append(toc)

        html.append(

            ContentRenderer().render(
                document
            )

        )

        html.append(

            FooterRenderer().render()

        )

        html.append("</body>")
        html.append("</html>")

        return "\n".join(html)

    def header(self, template="default"):

        return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="utf-8">

<title>Tech Capsule</title>

<style>

{get_styles(template)}

</style>

</head>

<body>
"""
