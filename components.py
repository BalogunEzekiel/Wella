import streamlit as st
import base64
from PIL import Image

def render_header(active="home"):
    # Load and encode the logo
    logo_path = "assets/logo.png"
    try:
        with open(logo_path, "rb") as f:
            logo_data = f.read()
            logo_base64 = base64.b64encode(logo_data).decode()
    except FileNotFoundError:
        st.error("🚫 Logo file not found at: assets/logo.png")
        return

    # Inject CSS and navigation bar HTML
    st.markdown(f"""
    <style>
    /* Permanent top navigation bar */
    .navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 70px;
        background-color: white;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 2rem;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }}

    .nav-left img {{
        height: 45px;
    }}

    .nav-center {{
        display: flex;
        gap: 1rem;
        justify-content: center;
        align-items: center;
        flex-grow: 1;
    }}

    .nav-button {{
        font-weight: 600;
        padding: 0.4rem 1rem;
        border-radius: 8px;
        background-color: transparent;
        color: #000;
        text-decoration: none;
        border: none;
        cursor: pointer;
        transition: all 0.2s ease;
    }}

    .nav-button:hover {{
        background-color: #f0f0f0;
    }}

    .nav-button.active {{
        background-color: #0072ff;
        color: white;
    }}

    /* Push the page content down to avoid overlap */
    .block-container {{
        padding-top: 90px !important;
    }}

    /* Completely hide Streamlit's settings menu (three dots) behind nav bar */
    header [data-testid="stToolbar"] {{
        visibility: hidden;
        height: 0;
        position: absolute;
        top: -9999px;
        z-index: -1;
    }}

    footer {{
        visibility: hidden;
    }}
    </style>

    <div class="navbar">
        <div class="nav-left">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        </div>
        <div class="nav-center">
            <button class="nav-button {'active' if active=='home' else ''}" onclick="window.location.href='/'">Home</button>
            <button class="nav-button {'active' if active=='service' else ''}" onclick="window.location.href='/?page=service'">Service</button>
            <button class="nav-button {'active' if active=='diagnosis' else ''}" onclick="window.location.href='/?page=diagnosis'">Diagnosis</button>
            <button class="nav-button {'active' if active=='about' else ''}" onclick="window.location.href='/?page=about'">About</button>
            <button class="nav-button {'active' if active=='contact' else ''}" onclick="window.location.href='/?page=contact'">Contact</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
