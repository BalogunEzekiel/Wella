import streamlit as st
import base64
from PIL import Image
from io import BytesIO

def get_base64_image(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

logo_base64 = get_base64_image("assets/logo.png")

st.markdown(
    f'<img src="data:image/png;base64,{logo_base64}" width="200"/>',
    unsafe_allow_html=True
)
