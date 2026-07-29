
"""
Tech Capsules HTML Renderer
Author: Ahmed Adawy
"""

from parser import Heading, Paragraph, BulletList


class HTMLRenderer:

    def render(self, document):

        html = []

        html.append("""
<!DOCTYPE html>
<html>
<head>

<meta charset="utf-8">

<title>Tech Capsule</title>

<style>

body{
    font-family:Arial,sans-serif;
    max-width:900px;
    margin:auto;
    padding:40px;
    line-height:1.8;
}

h1,h2,h3,h4,h5,h6{
    color:#222;
}

code{
    background:#eeeeee;
    padding:2px 5px;
}

pre{
    background:#f6f6f6;
    padding:15px;
    overflow:auto;
}

</style>

</head>

<body>
""")

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

        html.append("""

</body>

</html>

""")

        return "\n".join(html)
