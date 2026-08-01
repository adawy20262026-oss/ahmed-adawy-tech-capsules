"""
Ahmed Adawy Tech Capsules
Streamlit Application
"""

import os
import sys

# Allow running from project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from src.parser import MarkdownParser
from src.renderer import HTMLRenderer
from src.pdf_generator import PDFGenerator


def build_html(markdown_text: str) -> str:
    """
    Convert Markdown to HTML.
    """

    parser = MarkdownParser()
    document = parser.parse(markdown_text)

    renderer = HTMLRenderer()

    return renderer.render(document)


def build_pdf(html: str) -> bytes:
    """
    Convert HTML to PDF.
    """

    return PDFGenerator().generate(html)


st.set_page_config(
    page_title="Ahmed Adawy Tech Capsules",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Ahmed Adawy Tech Capsules")
st.caption("Write once in Markdown. Generate professional technical publications.")

uploaded_file = st.file_uploader(
    "Choose a Markdown file",
    type=["md"],
)

if uploaded_file is not None:

    try:

        markdown_content = uploaded_file.read().decode("utf-8")

    except UnicodeDecodeError:

        st.error("The uploaded file is not UTF-8 encoded.")
        st.stop()

    st.success("Markdown file loaded successfully.")

    html = build_html(markdown_content)

    tab1, tab2 = st.tabs(
        [
            "📝 Markdown",
            "🌐 HTML Preview",
        ]
    )

    with tab1:

        st.code(
            markdown_content,
            language="markdown",
        )

    with tab2:

        st.components.v1.html(
            html,
            height=700,
            scrolling=True,
        )

    st.divider()

    if st.button(
        "🚀 Generate PDF",
        use_container_width=True,
    ):

        with st.spinner("Generating PDF..."):

            try:

                pdf = build_pdf(html)

                st.success("PDF generated successfully.")

                st.download_button(
                    "📥 Download PDF",
                    pdf,
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

            except Exception as exc:

                st.exception(exc)
