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

table{
    width:100%;
    border-collapse:collapse;
    background:white;
}

th,td{
    border:1px solid #ddd;
    padding:12px;
}

th{
    background:#0F62FE;
    color:white;
}

a{
    text-decoration:none;
}

</style>

</head>
<body>

<h1>Ahmed Adawy Tech Capsules</h1>

<table>

<tr>

<th>Title</th>

<th>PDF</th>

<th>HTML</th>

</tr>

""")

        for capsule in capsules:

            html.append(f"""
<tr>

<td>{capsule}</td>

<td><a href="{capsule}.pdf">PDF</a></td>

<td><a href="{capsule}.html">HTML</a></td>

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
