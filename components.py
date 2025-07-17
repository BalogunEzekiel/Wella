import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def get_base64_image(image_path):
    try:
        img = Image.open(image_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode()
        return img_b64
    except Exception as e:
        return None

def render_header(active="home"):
    logo_base64 = get_base64_image("assets/logo.png")

    if not logo_base64:
        st.error("Logo image not found or failed to load.")
        return

    st.markdown(f"""
    <style>
    /* Clear default Streamlit padding */
    .main > div:first-child {{
        padding-top: 0rem !important;
    }}

    /* Header container */
    .top-nav-wrapper {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #00b894;
        padding: 1.5rem 3rem;
        min-height: 120px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        position: sticky;
        top: 0;
        z-index: 1000;
        flex-wrap: wrap;
        width: 100%;
    }}

    /* Logo styling */
    .logo-container img {{
        height: 90px;
        margin-right: 30px;
    }}

    /* Navigation styling */
    .top-nav {{
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        align-items: center;
    }}

    .top-nav a {{
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 10px 20px;
        border-radius: 6px;
        background-color: transparent;
        transition: background-color 0.3s ease-in-out;
    }}

    .top-nav a:hover {{
        background-color: rgba(255, 255, 255, 0.2);
    }}

    .top-nav a.active {{
        background-color: #007b5e;
        text-decoration: underline;
    }}

    @media (max-width: 768px) {{
        .top-nav-wrapper {{
            flex-direction: column;
            align-items: flex-start;
        }}
        .top-nav {{
            margin-top: 12px;
            flex-direction: column;
            gap: 12px;
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
    """, unsafe_allow_html=True)
