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
    logo_base64 = get_base64_image("assets/logo.png")  # Confirm path is correct

    st.markdown(f"""
    <style>
    .top-nav-wrapper {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.5rem 2rem;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 9999;
        background-color: transparent;  /* Removed background color */
        backdrop-filter: blur(5px);  /* Optional subtle blur */
        border-bottom: 1px solid #e0e0e0;  /* Optional bottom border */
        flex-wrap: wrap;
    }}

    .logo-container {{
        display: flex;
        align-items: center;
    }}

    .logo-container img {{
        height: 60px;
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
        font-weight: 600;
        font-size: 1.05rem;
        padding: 10px 16px;
        border-radius: 8px;
        transition: background-color 0.3s ease-in-out;
    }}

    .top-nav a:hover {{
        background-color: rgba(0,0,0,0.05);
    }}

    .top-nav a.active {{
        background-color: rgba(0,0,0,0.1);
        text-decoration: underline;
    }}

    /* Responsive Design */
    @media (max-width: 768px) {{
        .top-nav-wrapper {{
            flex-direction: column;
            align-items: flex-start;
        }}
        .top-nav {{
            margin-top: 12px;
            justify-content: flex-start;
            width: 100%;
        }}
    }}

    body {{
        padding-top: 100px;  /* Prevent content from hiding behind fixed nav */
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
