
"""
Tech Capsules HTML Renderer
Author: Ahmed Adawy
"""

from parser import Heading, Paragraph, BulletList, CodeBlock


class HTMLRenderer:

    def render(self, document):

        html = []

        html.append("""
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="utf-8">
<title>Tech Capsule</title>

<style>
/* ==========================================
   PAGE SETUP & WEASYPRINT PRINT STYLES
   ========================================== */
@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    
    @top-right {
        content: "Ahmed Adawy Tech Capsules";
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #888888;
    }
    
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 9pt;
        color: #666666;
    }
}

/* الصفحة الأولى: غلاف بدون Header أو Footer */
@page :first {
    margin: 0;
    @top-right { content: normal; }
    @bottom-center { content: normal; }
}

/* ==========================================
   GENERAL TYPOGRAPHY & BODY STYLES
   ========================================== */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #2d3748;
    line-height: 1.7;
    font-size: 11pt;
}

/* ==========================================
   COVER PAGE STYLE
   ========================================== */
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
    text-transform: uppercase;
    margin-bottom: 20px;
}

.cover-title {
    font-size: 32pt;
    font-weight: 800;
    line-height: 1.2;
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

/* ==========================================
   HEADINGS & CONTENT STYLES
   ========================================== */
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
    padding-left: 20px;
}

li {
    margin-bottom: 6px;
}

/* Inline Code & Code Blocks */
code {
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9.5pt;
}

pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
    line-height: 1.5;
    margin: 15px 0;
    page-break-inside: avoid;
}

pre code {
    background: none;
    color: inherit;
    padding: 0;
}
</style>
</head>

<body>

<!-- Automatic Cover Page -->
<div class="cover-page">
    <div class="cover-badge">TECH CAPSULE</div>
    <div class="cover-title">Ahmed Adawy Tech Capsules</div>
    <div class="cover-subtitle">Architectural Insights & Backend Best Practices</div>
    <div class="cover-footer">
        <strong>Author:</strong> Ahmed Adawy<br>
        <strong>Generated via:</strong> Automated Pipeline
    </div>
</div>

<div class="content">
""")

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
        
        html.append("""
</div>
</body>
</html>
""")

        return "\n".join(html)
