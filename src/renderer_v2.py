"""
HTML Renderer V2
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

from theme import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    BACKGROUND,
    TEXT_COLOR,
    TITLE_FONT,
    BODY_FONT,
)


class HTMLRenderer:

    def render(self, document, metadata):

        html = []

        html.append(self.header())

        html.append(self.cover(metadata))

        html.append(self.content(document))

        html.append(self.footer())

        return "\n".join(html)

    def header(self):

        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Tech Capsule</title>

<style>

body{{
font-family:{BODY_FONT},sans-serif;
margin:40px;
line-height:1.7;
color:{TEXT_COLOR};
background:{BACKGROUND};
}}

.cover{{
text-align:center;
padding:120px 40px;
page-break-after:always;
background:{PRIMARY_COLOR};
color:white;
}}

.cover h1{{
font-size:42px;
margin-bottom:20px;
color:white;
}}

.cover h2{{
font-size:22px;
font-weight:normal;
color:#e5e7eb;
}}

.cover p{{
margin-top:40px;
font-size:18px;
color:white;
}}

pre{{
background:{SECONDARY_COLOR};
color:white;
padding:15px;
border-radius:8px;
overflow:auto;
}}

code{{
background:#f5f5f5;
padding:2px 6px;
}}

table{{
border-collapse:collapse;
width:100%;
}}

th,td{{
border:1px solid #ddd;
padding:8px;
}}

img{{
max-width:100%;
}}

</style>

</head>

<body>
"""
font-family:Arial,sans-serif;
margin:40px;
line-height:1.7;
color:#222;
}

.cover{
text-align:center;
padding:120px 40px;
page-break-after:always;
background:#0F62FE;
color:white;
border-radius:12px;
}

.cover h1{
font-size:42px;
margin-bottom:20px;
color:white;
}

.cover h2{
font-size:22px;
font-weight:normal;
color:#E0E0E0;
}

.cover p{
margin-top:45px;
font-size:18px;
color:white;
}

pre{
background:#1E1E1E;
color:white;
padding:15px;
border-radius:8px;
overflow:auto;
}

code{
background:#f5f5f5;
padding:2px 6px;
}

table{
border-collapse:collapse;
width:100%;
}

th,td{
border:1px solid #ddd;
padding:8px;
}

img{
max-width:100%;
}

</style>

</head>

<body>
"""

    def cover(self, metadata):

        title = metadata.get(
            "title",
            "Ahmed Adawy Tech Capsules"
        )

        subtitle = metadata.get(
            "subtitle",
            ""
        )

        author = metadata.get(
            "author",
            "Ahmed Adawy"
        )

        version = metadata.get(
            "version",
            "1.0"
        )

        return f"""
        
<div class="cover">

<p>Ahmed Adawy Tech Capsules</p>

<h1>{title}</h1>

<h2>{subtitle}</h2>

<p>

<b>Author</b><br>

{author}

</p>

<p>

Version {version}

</p>

</div>
"""

    def content(self, document):

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

    def footer(self):

        return """

</body>

</html>

"""
