"""
Theme Configuration
Ahmed Adawy Tech Capsules
"""

# ==========================================
# Project Information
# ==========================================

PROJECT_NAME = "Ahmed Adawy Tech Capsules"
AUTHOR = "Ahmed Adawy"

# ==========================================
# Color Palette
# ==========================================

PRIMARY_COLOR = "#2563EB"
SECONDARY_COLOR = "#1E293B"
ACCENT_COLOR = "#0F62FE"

BACKGROUND = "#FFFFFF"
SURFACE_COLOR = "#F8FAFC"

TEXT_COLOR = "#111827"
MUTED_TEXT_COLOR = "#6B7280"

BORDER_COLOR = "#D1D5DB"

SUCCESS_COLOR = "#198754"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#DC3545"

# ==========================================
# Typography
# ==========================================

TITLE_FONT = "Arial"
BODY_FONT = "Arial"
CODE_FONT = "Courier New"

TITLE_SIZE = "42px"
SUBTITLE_SIZE = "22px"
BODY_SIZE = "16px"
CODE_SIZE = "14px"

LINE_HEIGHT = "1.7"

# ==========================================
# Layout
# ==========================================

CONTENT_WIDTH = "100%"

PAGE_MARGIN = "40px"
CONTENT_PADDING = "20px"

SECTION_SPACING = "28px"

BORDER_RADIUS = "10px"

COVER_PADDING = "120px 40px"

# ==========================================
# Code Blocks
# ==========================================

CODE_BACKGROUND = SECONDARY_COLOR
CODE_TEXT = "#FFFFFF"

CODE_BORDER_RADIUS = "8px"
CODE_PADDING = "16px"

# ==========================================
# Tables
# ==========================================

TABLE_HEADER_BACKGROUND = PRIMARY_COLOR
TABLE_HEADER_TEXT = "#FFFFFF"

TABLE_BORDER = BORDER_COLOR

TABLE_CELL_PADDING = "10px"

# ==========================================
# Images
# ==========================================

IMAGE_MAX_WIDTH = "100%"
IMAGE_BORDER_RADIUS = "8px"

# ==========================================
# PDF
# ==========================================

PDF_PAGE_SIZE = "A4"
PDF_MARGIN = "25mm 20mm 25mm 20mm"
PDF_FOOTER_SIZE = "11px"

# ==========================================
# Table of Contents
# ==========================================

TOC_BACKGROUND = "#F8FAFC"
TOC_BORDER = "#E5E7EB"
TOC_TITLE_COLOR = PRIMARY_COLOR

# ==========================================
# Future Theme Support
# ==========================================

THEME = {
    "project": PROJECT_NAME,
    "author": AUTHOR,
    "colors": {
        "primary": PRIMARY_COLOR,
        "secondary": SECONDARY_COLOR,
        "accent": ACCENT_COLOR,
        "background": BACKGROUND,
        "surface": SURFACE_COLOR,
        "text": TEXT_COLOR,
        "muted": MUTED_TEXT_COLOR,
        "border": BORDER_COLOR,
    },
    "fonts": {
        "title": TITLE_FONT,
        "body": BODY_FONT,
        "code": CODE_FONT,
    },
}
