"""
Styles
Ahmed Adawy Tech Capsules
"""

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

    return f"""
body{{
font-family:{BODY_FONT},sans-serif;
margin:{PAGE_MARGIN};
line-height:{LINE_HEIGHT};
background:{BACKGROUND};
color:{TEXT_COLOR};
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
color:white;
padding:15px;
border-radius:{BORDER_RADIUS};
overflow:auto;
}}

code{{
background:#f3f4f6;
padding:2px 6px;
border-radius:4px;
}}

table{{
border-collapse:collapse;
width:100%;
margin:20px 0;
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
max-width:{IMAGE_MAX_WIDTH};
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

.toc{
margin:40px 0;
padding:25px;
background:#f8fafc;
border:1px solid #e5e7eb;
border-radius:12px;
page-break-after:always;
}

.toc h2{
margin-top:0;
color:#2563eb;
}

.toc ul{
list-style:none;
padding-left:0;
}

.toc li{
padding:6px 0;
border-bottom:1px solid #eeeeee;
}
"""
