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


st.set_page_config(
    page_title="Ahmed Adawy Tech Capsules",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Ahmed Adawy Tech Capsules")
st.write(
    "Upload a Markdown (.md) file to generate a professional PDF capsule."
)

uploaded_file = st.file_uploader(
    "Choose Markdown file",
    type=["md"]
)

if uploaded_file is not None:

    try:

        markdown_content = uploaded_file.read().decode("utf-8")

    except UnicodeDecodeError:

        st.error(
            "The uploaded file is not UTF-8 encoded."
        )

        st.stop()

    st.success("File uploaded successfully.")

    with st.expander("Preview"):

        st.code(
            markdown_content,
            language="markdown"
        )

    if st.button("🚀 Generate PDF"):

        with st.spinner("Building capsule..."):

            try:

                parser = MarkdownParser()

                document = parser.parse(
                    markdown_content
                )

                renderer = HTMLRenderer()

                html = renderer.render(
                    document
                )

                pdf = PDFGenerator().generate(
                    html
                )

                st.success(
                    "PDF generated successfully."
                )

                st.download_button(
                    label="📥 Download PDF",
                    data=pdf,
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}.pdf",
                    mime="application/pdf"
                )

            except Exception as exc:

                st.exception(exc)
