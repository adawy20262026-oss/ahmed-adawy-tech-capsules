"""
Styles
Ahmed Adawy Tech Capsules
"""

from highlighter import SyntaxHighlighter

from theme import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    BACKGROUND,
    TEXT_COLOR,
    BODY_FONT,
    TITLE_FONT,
    PAGE_MARGIN,
    BORDER_RADIUS,
    COVER_PADDING,
    LINE_HEIGHT,
    CODE_BACKGROUND,
    TABLE_HEADER_BACKGROUND,
    TABLE_HEADER_TEXT,
    TABLE_BORDER,
    IMAGE_MAX_WIDTH,
    PDF_PAGE_SIZE,
    PDF_MARGIN,
    PDF_FOOTER_SIZE,
)


def get_styles():

    pygments_css = SyntaxHighlighter().css()

    return f"""
body{{
font-family:{BODY_FONT},sans-serif;
margin:{PAGE_MARGIN};
line-height:{LINE_HEIGHT};
background:{BACKGROUND};
color:{TEXT_COLOR};
}}

h1,h2,h3,h4,h5,h6{{
font-family:{TITLE_FONT},sans-serif;
color:{PRIMARY_COLOR};
margin-top:28px;
margin-bottom:14px;
}}

p{{
text-align:justify;
margin-bottom:16px;
}}

.cover{{
text-align:center;
padding:{COVER_PADDING};
page-break-after:always;
background:{PRIMARY_COLOR};
color:white;
border-radius:{BORDER_RADIUS};
}}

.cover h1{{
font-family:{TITLE_FONT},sans-serif;
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
}}

pre{{
background:{CODE_BACKGROUND};
padding:15px;
border-radius:{BORDER_RADIUS};
overflow:auto;
white-space:pre-wrap;
}}

code{{
font-family:monospace;
}}

.highlight{{
margin:20px 0;
border-radius:{BORDER_RADIUS};
overflow:auto;
}}

table{{
border-collapse:collapse;
width:100%;
margin:24px 0;
}}

th{{
background:{TABLE_HEADER_BACKGROUND};
color:{TABLE_HEADER_TEXT};
padding:10px;
}}

td{{
border:1px solid {TABLE_BORDER};
padding:10px;
}}

img{{
display:block;
margin:24px auto;
max-width:{IMAGE_MAX_WIDTH};
height:auto;
}}

blockquote{{
border-left:4px solid {PRIMARY_COLOR};
padding-left:16px;
color:#555;
margin:20px 0;
}}

hr{{
border:none;
border-top:1px solid #dddddd;
margin:30px 0;
}}

@page{{
size:{PDF_PAGE_SIZE};
margin:{PDF_MARGIN};

@bottom-center{{
content:"Page " counter(page);
font-size:{PDF_FOOTER_SIZE};
color:#666;
}}
}}

.toc{{
page-break-after:always;
margin:40px 0;
padding:30px;
background:#f8fafc;
border:1px solid #e5e7eb;
border-radius:12px;
}}

.toc h2{{
margin-top:0;
margin-bottom:20px;
color:{PRIMARY_COLOR};
text-align:center;
}}

.toc ul{{
list-style:none;
padding-left:0;
margin:0;
}}

.toc li{{
padding:8px 0;
border-bottom:1px solid #eeeeee;
}}

.toc li:last-child{{
border-bottom:none;
}}

.toc .level-1{{
font-weight:bold;
font-size:18px;
}}

.toc .level-2{{
padding-left:20px;
}}

.toc .level-3{{
padding-left:40px;
font-size:14px;
color:#666;
}}

/* ===== Pygments Theme ===== */

{pygments_css}

"""
