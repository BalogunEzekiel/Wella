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
    logo_base64 = get_base64_image("assets/logo.png")

    st.markdown(f"""
    <style>
    /* Override Streamlit top bar (3 dots) */
    [data-testid="stDecoration"] {{
        z-index: -1 !important;
        opacity: 0 !important;
        visibility: hidden !important;
        height: 0px !important;
    }}

    header {{
        z-index: -1 !important;
    }}

    /* Force nav to topmost layer */
    .top-nav-wrapper {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.5rem 2rem;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 9999999 !important;
        background-color: white;
        border-bottom: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        flex-wrap: wrap;
    }}

    .logo-container {{
        display: flex;
        align-items: center;
    }}

    .logo-container img {{
        height: 80px;
        display: block;
        margin-right: 20px;
    }}

    .top-nav {{
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex: 1;
    }}

    .top-nav a {{
        color: #333;
        text-decoration: none;
        font-weight: bold;
        font-size: 1rem;
        padding: 8px 16px;
        border-radius: 30px;
        background-color: #f5f5f5;
        transition: background-color 0.3s ease;
        border: 1px solid transparent;
    }}

    .top-nav a:hover {{
        background-color: #e0e0e0;
    }}

    .top-nav a.active {{
        background-color: #d1e3ff;
        border-color: #90c2ff;
    }}

    /* Adjust body to not hide behind nav */
    body, .main {{
        padding-top: 110px !important;
        margin-top: 0 !important;
    }}

    @media (max-width: 768px) {{
        .top-nav-wrapper {{
            flex-direction: column;
            align-items: flex-start;
        }}
        .top-nav {{
            margin-top: 10px;
            flex-wrap: wrap;
            justify-content: flex-start;
            width: 100%;
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
