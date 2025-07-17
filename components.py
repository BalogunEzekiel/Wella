from PIL import Image
import streamlit as st



try:
    img = Image.open("assets/logo.png")
    st.image(img, caption="If you see this, logo path is OK")
except FileNotFoundError:
    st.error("🚫 Logo file not found at: assets/logo.png")

def render_header(active="home"):
    # your function body here
