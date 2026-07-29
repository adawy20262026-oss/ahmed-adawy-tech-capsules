"""
HTML Generator
"""

from pathlib import Path


def generate_html(markdown_text):
    html = f"""
    <html>

    <body>

    <pre>

{markdown_text}

    </pre>

    </body>

    </html>
    """

    return html


if __name__ == "__main__":

    sample = "# Hello Tech Capsules"

    print(generate_html(sample))
