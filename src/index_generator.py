"""
Library Index Generator
Ahmed Adawy Tech Capsules
"""

from pathlib import Path


class IndexGenerator:

    def generate(self, capsules):

        output = Path("output")
        output.mkdir(exist_ok=True)

        html = []

        html.append("""
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">

<title>Ahmed Adawy Tech Capsules</title>

<style>

body{

font-family:Arial,sans-serif;

background:#f4f6f9;

margin:40px;

}

h1{

text-align:center;

color:#222;

}

.library{

display:grid;

grid-template-columns:repeat(auto-fill,minmax(320px,1fr));

gap:25px;

margin-top:40px;

}

.card{

background:white;

border-radius:12px;

padding:22px;

box-shadow:0 5px 15px rgba(0,0,0,.08);

transition:.2s;

}

.card:hover{

transform:translateY(-5px);

}

.title{

font-size:22px;

font-weight:bold;

margin-bottom:10px;

}

.badge{

display:inline-block;

background:#0F62FE;

color:white;

padding:4px 10px;

border-radius:20px;

font-size:12px;

margin-right:6px;

margin-bottom:15px;

}

.version{

color:#777;

margin-bottom:18px;

}

.buttons a{

display:inline-block;

text-decoration:none;

background:#0F62FE;

color:white;

padding:10px 18px;

border-radius:8px;

margin-right:8px;

margin-top:8px;

}

.buttons a:hover{

background:#0043ce;

}

.footer{

margin-top:60px;

text-align:center;

color:#888;

}

</style>

</head>

<body>

<h1>Ahmed Adawy Tech Capsules</h1>

<div class="library">
""")

        for capsule in capsules:

            title = capsule["title"]
            category = capsule["category"]
            version = capsule["version"]
            filename = capsule["file"]

            html.append(f"""
<div class="card">

<div class="title">
📘 {title}
</div>

<div class="badge">
{category}
</div>

<div class="version">
Version {version}
</div>

<div class="buttons">

<a href="{filename}.pdf">
PDF
</a>

<a href="{filename}.html">
HTML
</a>

</div>

</div>
""")

        html.append("""
</div>

<div class="footer">

Ahmed Adawy Tech Capsules

</div>

</body>

</html>
""")

        (output / "index.html").write_text(
            "\n".join(html),
            encoding="utf-8"
        )

        print("Library index generated.")
