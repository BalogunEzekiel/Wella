import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def get_base64_image(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()
    return img_b64

def render_header(active="home"):
    logo_base64 = get_base64_image("assets/logo.png")  # Ensure correct logo path

    st.markdown(f"""
    <style>
    .top-nav-wrapper {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 80px;
        z-index: 9999;
        background-color: #ffffff;  /* White for visibility */
        border-bottom: 1px solid #e0e0e0;
        padding: 0 2rem;
        box-shadow: 0 1px 5px rgba(0,0,0,0.05);
    }}

    .logo-container {{
        display: flex;
        align-items: center;
        flex-shrink: 0;
    }}

    .logo-container img {{
        height: 55px;
    }}

    .top-nav {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1.5rem;
        flex: 1;
        margin-left: 2rem;
    }}

    .top-nav a {{
        text-decoration: none;
        font-weight: bold;
        font-size: 1rem;
        padding: 10px 18px;
        border-radius: 6px;
        color: #333;
        border: 1px solid transparent;
        transition: all 0.3s ease-in-out;
    }}

    .top-nav a:hover {{
        background-color: #f0f0f0;
        border: 1px solid #ddd;
    }}

    .top-nav a.active {{
        background-color: #333;
        color: #fff;
        border: 1px solid #333;
    }}

    /* Make space for fixed navbar */
    .main {{
        padding-top: 100px;
    }}

    @media (max-width: 768px) {{
        .top-nav-wrapper {{
            flex-direction: column;
            height: auto;
            align-items: flex-start;
            padding: 1rem;
        }}

        .top-nav {{
            margin-left: 0;
            flex-direction: column;
            align-items: flex-start;
        }}

        .top-nav a {{
            width: 100%;
            padding: 10px;
        }}
    }}
    </style>

    <div class="top-nav-wrapper">
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" alt="Wella.AI Logo" />
        </div>
        <div class="top-nav">
            <a href="/?page=home" class="{ 'active' if active == 'home' else '' }">Home</a>
            <a href="/?page=service" class="{ 'active' if active == 'service' else '' }">Service</a>
            <a href="/?page=login" class="{ 'active' if active == 'diagnosis' else '' }">Diagnosis</a>
            <a href="/?page=about" class="{ 'active' if active == 'about' else '' }">About</a>
            <a href="/?page=contact" class="{ 'active' if active == 'contact' else '' }">Contact</a>
        </div>
    </div>

    <div class="main"></div>  <!-- spacer to prevent nav overlap -->
    """, unsafe_allow_html=True)
