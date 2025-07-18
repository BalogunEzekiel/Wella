import streamlit as st
import base64
from PIL import Image

def render_header(active="home"):
    # Load logo and convert to base64
    logo_path = "assets/logo.png"
    try:
        with open(logo_path, "rb") as f:
            logo_data = f.read()
            logo_base64 = base64.b64encode(logo_data).decode()
    except FileNotFoundError:
        st.error("🚫 Logo file not found at: assets/logo.png")
        return

    # Inject CSS
    st.markdown(f"""
    <style>
    /* Make nav bar fixed at the top */
    .navbar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: white;
        z-index: 1000;
        padding: 0.5rem 2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}

    .nav-left {{
        display: flex;
        align-items: center;
    }}

    .nav-left img {{
        height: 45px;
    }}

    .nav-center {{
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        flex-grow: 1;
    }}

    .nav-button {{
        font-weight: 600;
        padding: 0.3rem 0.8rem;
        border-radius: 6px;
        text-decoration: none;
        color: black;
        background-color: transparent;
        border: none;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }}

    .nav-button:hover {{
        background-color: #f0f0f0;
    }}

    .nav-button.active {{
        background-color: #0072ff;
        color: white;
    }}

    /* Push page content down so it’s not hidden behind navbar */
    .block-container {{
        padding-top: 90px;
    }}

    /* Hide Streamlit’s 3-dot settings menu */
    header [data-testid="stToolbar"] {{
        visibility: hidden;
    }}

    /* Hide Streamlit footer */
    footer {{
        visibility: hidden;
    }}
    </style>

    <div class="navbar">
        <div class="nav-left">
            <img src="data:image/png;base64,{logo_base64}" alt="Wella.AI Logo">
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
