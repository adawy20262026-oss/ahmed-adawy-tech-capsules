"""
Library Index Generator
Ahmed Adawy Tech Capsules
"""

from pathlib import Path
from pathlib import Path
from config import OUTPUT_DIR, DEFAULT_ENCODING

class IndexGenerator:

        OUTPUT_DIR.mkdir(exist_ok=True)
        total = len(capsules)

        html = []

        html.append(f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<title>Ahmed Adawy Tech Capsules</title>

<style>

body{{
font-family:Arial,sans-serif;
background:#f4f6f9;
margin:40px;
}}

.header{{
text-align:center;
margin-bottom:40px;
}}

h1{{
margin-bottom:10px;
color:#222;
}}

.counter{{
color:#666;
margin-bottom:20px;
}}

#search{{
width:60%;
padding:14px;
font-size:16px;
border-radius:10px;
border:1px solid #ccc;
}}

.library{{
display:grid;
grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
gap:25px;
margin-top:40px;
}}

.card{{
background:white;
border-radius:12px;
padding:22px;
box-shadow:0 5px 15px rgba(0,0,0,.08);
transition:.2s;
}}

.card:hover{{
transform:translateY(-5px);
}}

.title{{
font-size:22px;
font-weight:bold;
margin-bottom:10px;
}}

.badge{{
display:inline-block;
padding:5px 12px;
border-radius:20px;
font-size:12px;
font-weight:bold;
color:white;
margin-bottom:15px;
}}

.version{{
color:#777;
margin-bottom:18px;
}}

.buttons a{{
display:inline-block;
text-decoration:none;
background:#0F62FE;
color:white;
padding:10px 18px;
border-radius:8px;
margin-right:8px;
margin-top:8px;
}}

.buttons a:hover{{
background:#0043ce;
}}

.footer{{
margin-top:60px;
text-align:center;
color:#888;
}}

</style>

</head>

<body>

<div class="header">

<h1>Ahmed Adawy Tech Capsules</h1>

<div class="counter">

📚 Total Capsules: {total}

</div>

<input
id="search"
type="text"
placeholder="🔍 Search Capsules..."
onkeyup="searchCapsules()"
/>

</div>

<div class="library">
""")

        colors = {
            "Linux": "#0F62FE",
            "Python": "#198754",
            "AI": "#6f42c1",
            "DevOps": "#fd7e14",
            "Security": "#dc3545"
        }

        for capsule in capsules:

            title = capsule.get("title", "Untitled Capsule")
            subtitle = capsule.get("subtitle", "")
            category = capsule.get("category", "General")
            difficulty = capsule.get("difficulty", "Beginner")
            language = capsule.get("language", "en")
            version = capsule.get("version", "1.0")
            filename = capsule.get("file", "unknown")
            

            color = colors.get(category, "#444")

            html.append(f"""
<div class="card">

<div class="title">
📘 {title}
</div>

<p style="color:#666;margin-top:8px;margin-bottom:18px;">
{subtitle}
</p>

<div class="badge" style="background:{color};">
{category}
</div>

<p>
⭐ <b>{difficulty}</b>
</p>

<p>
🌍 {language.upper()}
</p>

<div class="version">
Version {version}
</div>

<div class="buttons">

<a href="{filename}.html">
📄 Read Online
</a>

<a href="{filename}.pdf">
⬇ Download PDF
</a>

</div>

</div>
""")

        html.append("""
</div>

<div class="footer">

Ahmed Adawy Tech Capsules

</div>

<script>

function searchCapsules(){

let input=document.getElementById("search").value.toLowerCase();

let cards=document.getElementsByClassName("card");

for(let i=0;i<cards.length;i++){

let title=cards[i].innerText.toLowerCase();

if(title.includes(input))
cards[i].style.display="block";
else
cards[i].style.display="none";

}

}

</script>

</body>

</html>
""")

        (OUTPUT_DIR / "index.html").write_text(
    "\n".join(html),
    encoding=DEFAULT_ENCODING
   )
        print("Library index generated.")
