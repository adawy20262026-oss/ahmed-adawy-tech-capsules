import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import streamlit as st
import os
import tempfile
from src.parser import parse_markdown
from src.renderer import HTMLRenderer
from src.pdf_generator import PDFGenerator

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="مُحول الكبسولات التقنية لـ PDF",
    page_icon="📚",
    layout="centered"
)

st.title("📚 محول الكبسولات التقنية إلى PDF")
st.write("قم برفع ملف الماركداون (.md) وسيتم تحويله فوراً إلى كتاب PDF احترافي يدعم اللغة العربية.")

# رفع الملف
uploaded_file = st.file_uploader("اختر ملف Markdown", type=["md"])

if uploaded_file is not None:
    # قراءة المحتوى
    markdown_content = uploaded_file.read().decode("utf-8")
    
    st.success("تم رفع الملف بنجاح!")
    
    # معاينة سريعة للمحتوى
    with st.expander("معاينة النص"):
        st.code(markdown_content, language="markdown")

    if st.button("🚀 تحويل إلى PDF"):
        with st.spinner("جاري معالجة الكبسولة وبناء الـ PDF..."):
            try:
                # 1. Parsing
                nodes = parse_markdown(markdown_content)
                
                # 2. Rendering HTML
                renderer = HTMLRenderer()
                html_code = renderer.render(nodes)
                
                # 3. Generating PDF via WeasyPrint
                pdf_bytes = PDFGenerator().generate(html_code)
                
                st.balloons()
                st.success("تم إنشاء الـ PDF بنجاح!")
                
                # زِر تحميل الـ PDF
                st.download_button(
                    label="📥 تحميل ملف الـ PDF",
                    data=pdf_bytes,
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"حدث خطأ أثناء المعالجة: {str(e)}")
