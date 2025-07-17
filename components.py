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
    logo_base64 = get_base64_image("assets/logo.png")  # Ensure the logo path is correct

    st.markdown(f"""
    <style>
    .top-nav-wrapper {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 9999;
        background-color: rgba(255, 255, 255, 0.95); /* Transparent white background */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        padding: 0.75rem 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        font-family: 'Segoe UI', sans-serif;
    }}

    .logo-container {{
        display: flex;
        align-items: center;
    }}

    .logo-container img {{
        height: 55px;
    }}

    .top-nav {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1.5rem;
        flex-grow: 1;
    }}

    .top-nav a {{
        text-decoration: none;
        color: #333;
        font-weight: 500;
        font-size: 1rem;
        position: relative;
        padding: 8px 5px;
        transition: color 0.3s ease-in-out;
    }}

    .top-nav a:hover {{
        color: #00b894;
    }}

    .top-nav a.active::after {{
        content: '';
        position: absolute;
        bottom: -6px;
        left: 0;
        width: 100%;
        height: 3px;
        background-color: #00b894;
        border-radius: 10px;
    }}

    /* Responsive adjustment */
    @media (max-width: 768px) {{
        .top-nav {{
            flex-direction: column;
            gap: 1rem;
            margin-top: 10px;
        }}
    }}

    .spacer {{
        height: 80px;  /* Spacer to offset fixed nav height */
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

    <div class="spacer"></div>
    """, unsafe_allow_html=True)
