import streamlit as st
from PIL import Image
import numpy as np
import easyocr

st.set_page_config(page_title="Urdu OCR — Code Saviours SI-26", page_icon="📝", layout="centered")

@st.cache_resource(show_spinner=False)
def load_easyocr():
    # Load EasyOCR Urdu Engine
    return easyocr.Reader(['ur', 'en'], gpu=False)

st.title("Urdu Optical Character Recognition (OCR) 📝")
st.caption("Deep Learning Pipeline — Code Saviours ML/AI Internship, Batch SI-26")

try:
    with st.spinner("Initializing OCR Engine..."):
        reader = load_easyocr()
except Exception as e:
    st.error(f"Failed to load OCR engine: {e}")
    st.stop()

uploaded = st.file_uploader("Upload an Urdu image to extract text.", type=["png", "jpg", "jpeg"])

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded Image", width=500)

    with st.spinner("Extracting Urdu Text..."):
        img_np = np.array(image)
        results = reader.readtext(img_np, detail=0)
        final_text = " ".join(results).strip()

    st.subheader("Extracted Text")
    if final_text:
        st.markdown(
            f'<div dir="rtl" lang="ur" style="font-size:1.6rem; line-height:2.2; '
            f'padding:1rem 1.25rem; border:1px solid #444; border-radius:8px; background-color:#1e1e1e; color:#fff; text-align:right;">{final_text}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning("Could not extract text from this image.")
else:
    st.info("Please upload a JPG or PNG image containing Urdu text.")

st.divider()
st.caption("Built during Code Saviours ML/AI Internship — Batch SI-26")