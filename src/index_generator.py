"""
Index Generator
Ahmed Adawy Tech Capsules
"""

from pathlib import Path


class IndexGenerator:

    def generate(self, capsules):

        html = []

        html.append("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">

<title>Ahmed Adawy Tech Capsules</title>

<style>

body{
font-family:Arial,sans-serif;
margin:40px;
background:#f5f5f5;
}

h1{
color:#0F62FE;
}

p{
color:#666;
}

table{
width:100%;
border-collapse:collapse;
background:white;
}

th{
background:#0F62FE;
color:white;
padding:12px;
}

td{
padding:12px;
border:1px solid #ddd;
}

tr:nth-child(even){
background:#fafafa;
}

a{
text-decoration:none;
font-weight:bold;
color:#0F62FE;
}

</style>

</head>

<body>

<h1>Ahmed Adawy Tech Capsules</h1>

<p>
Automatically generated library.
</p>

<table>

<tr>

<th>Title</th>

<th>Category</th>

<th>Version</th>

<th>PDF</th>

<th>HTML</th>

</tr>

""")

        for capsule in capsules:

            html.append(f"""
<tr>

<td>{capsule["title"]}</td>

<td>{capsule["category"]}</td>

<td>{capsule["version"]}</td>

<td>
<a href="{capsule["file"]}.pdf">
PDF
</a>
</td>

<td>
<a href="{capsule["file"]}.html">
HTML
</a>
</td>

</tr>
""")

        html.append("""

</table>

</body>

</html>

""")

        output = Path("output/index.html")

        output.write_text(
            "\n".join(html),
            encoding="utf-8"
        )
