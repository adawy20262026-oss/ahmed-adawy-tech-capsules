from .parser import  Heading, Paragraph, BulletList, CodeBlock, Image, Table

class HTMLRenderer:
    def render(self, document):
        html = []
        
        # 1. HTML Header with RTL & Arabic Fonts
        html.append("""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>Tech Capsule</title>
<style>
/* IMPORT ARABIC FONTS */
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

/* PAGE SETUP & WEASYPRINT PRINT STYLES */
@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @top-left {
        content: "كبسولات أحمد العدوي التقنية";
        font-family: 'Cairo', sans-serif;
        font-size: 8pt;
        color: #888888;
    }
    @bottom-center {
        content: "صفحة " counter(page) " من " counter(pages);
        font-family: 'Cairo', sans-serif;
        font-size: 9pt;
        color: #666666;
    }
}

@page :first {
    margin: 0;
    @top-left { content: normal; }
    @bottom-center { content: normal; }
}

/* GENERAL TYPOGRAPHY & BODY STYLES */
body {
    font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
    color: #2d3748;
    line-height: 1.8;
    font-size: 11pt;
    direction: rtl;
    text-align: right;
}

/* COVER PAGE STYLE */
.cover-page {
    page-break-after: always;
    height: 100vh;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 60mm 20mm 20mm 20mm;
    box-sizing: border-box;
}

.cover-badge {
    display: inline-block;
    background: #38bdf8;
    color: #0f172a;
    padding: 4px 12px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 10pt;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.cover-title {
    font-size: 30pt;
    font-weight: 800;
    line-height: 1.3;
    margin: 0 0 15px 0;
    color: #f8fafc;
}

.cover-subtitle {
    font-size: 14pt;
    color: #94a3b8;
    margin-bottom: 40px;
}

.cover-footer {
    position: absolute;
    bottom: 30mm;
    border-top: 1px solid #334155;
    padding-top: 15px;
    width: 80%;
    color: #cbd5e1;
    font-size: 10pt;
}

/* HEADINGS & CONTENT STYLES */
h1 {
    font-size: 20pt;
    color: #0f172a;
    border-bottom: 2px solid #38bdf8;
    padding-bottom: 6px;
    margin-top: 25px;
    page-break-after: avoid;
}

h2 {
    font-size: 15pt;
    color: #1e293b;
    margin-top: 20px;
    page-break-after: avoid;
}

h3 {
    font-size: 12pt;
    color: #334155;
    page-break-after: avoid;
}

p {
    margin-bottom: 12px;
    text-align: justify;
}

ul {
    margin-top: 5px;
    margin-bottom: 15px;
    padding-right: 20px;
    padding-left: 0;
}

li {
    margin-bottom: 6px;
}

/* INLINE CODE & CODE BLOCKS (Keep LTR for code) */
code {
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9.5pt;
    direction: ltr;
    display: inline-block;
}

pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
    font-family: 'Courier New', Courier, monospace;
    direction: ltr;
    text-align: left;
}

pre code {
    background: none;
    color: inherit;
    padding: 0;
}

/* TABLES STYLING */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 10pt;
}

th, td {
    border: 1px solid #cbd5e1;
    padding: 10px 12px;
    text-align: right;
}

th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

/* IMAGES STYLING */
.img-container {
    text-align: center;
    margin: 20px 0;
}

img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
}
</style>
</head>
<body>
""")

        # 2. Cover Page
        html.append("""
<div class="cover-page">
    <div class="cover-badge">كبسولة تقنية</div>
    <div class="cover-title">كبسولات أحمد العدوي التقنية</div>
    <div class="cover-subtitle">رؤى معمارية وأفضل الممارسات في تطوير الأنظمة</div>
    <div class="cover-footer">
        <strong>الكاتب:</strong> أحمد العدوي<br>
        <strong>تم الإنشاء عبر:</strong> Automated Pipeline
    </div>
</div>
<div class="content">
""")

        # 3. Process Content Nodes
        for node in document:
            if isinstance(node, Heading):
                html.append(f"<h{node.level}>{node.text}</h{node.level}>")
            elif isinstance(node, Paragraph):
                html.append(f"<p>{node.text}</p>")
            elif isinstance(node, BulletList):
                html.append("<ul>")
                for item in node.items:
                    html.append(f"<li>{item}</li>")
                html.append("</ul>")
            elif isinstance(node, CodeBlock):
                html.append(f"<pre><code>{node.text}</code></pre>")
            elif isinstance(node, Image):
                html.append(f'<div class="img-container"><img src="{node.src}" alt="{node.alt}"></div>')
            elif isinstance(node, Table):
                table_html = ["<table>"]
                if node.header:
                    table_html.append("<thead><tr>")
                    for h in node.header:
                        table_html.append(f"<th>{h}</th>")
                    table_html.append("</tr></thead>")
                table_html.append("<tbody>")
                for row in node.rows:
                    table_html.append("<tr>")
                    for cell in row:
                        table_html.append(f"<td>{cell}</td>")
                    table_html.append("</tr>")
                table_html.append("</tbody>")
                table_html.append("</table>")
                html.append("\n".join(table_html))

        # 4. Close Wrappers & Document
        html.append("""
</div>
</body>
</html>
""")

        return "\n".join(html)
