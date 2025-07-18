import streamlit as st
import base64
from PIL import Image

def render_header(active="home"):
    # Load and encode logo
    logo_path = "assets/logo.png"
    try:
        with open(logo_path, "rb") as f:
            logo_data = f.read()
            logo_base64 = base64.b64encode(logo_data).decode()
    except FileNotFoundError:
        st.error("🚫 Logo file not found at: assets/logo.png")
        return

    # Inject CSS and top bar
    st.markdown(f"""
    <style>
    /* Remove original Streamlit toolbar and footer */
    header [data-testid="stToolbar"],
    footer {{
        visibility: hidden;
        height: 0;
        position: absolute;
    }}

    /* Force our own topmost navigation bar */
    .custom-topbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 60px;
        background-color: white;
        border-bottom: 1px solid #e0e0e0;
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }}

    .nav-logo img {{
        height: 40px;
    }}

    .nav-buttons {{
        display: flex;
        gap: 1rem;
    }}

    .nav-button {{
        font-weight: 600;
        font-size: 14px;
        padding: 0.4rem 1rem;
        border-radius: 6px;
        background-color: transparent;
        border: none;
        cursor: pointer;
        color: #333;
        transition: all 0.2s ease;
    }}

    .nav-button:hover {{
        background-color: #f2f2f2;
    }}

    .nav-button.active {{
        background-color: #0072ff;
        color: white;
    }}

    /* Push page content down to avoid overlap */
    .block-container {{
        padding-top: 80px !important;
    }}
    </style>

    <div class="custom-topbar">
        <div class="nav-logo">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        </div>
        <div class="nav-buttons">
            <button class="nav-button {'active' if active=='home' else ''}" onclick="window.location.href='/'">Home</button>
            <button class="nav-button {'active' if active=='service' else ''}" onclick="window.location.href='/?page=service'">Service</button>
            <button class="nav-button {'active' if active=='diagnosis' else ''}" onclick="window.location.href='/?page=diagnosis'">Diagnosis</button>
            <button class="nav-button {'active' if active=='about' else ''}" onclick="window.location.href='/?page=about'">About</button>
            <button class="nav-button {'active' if active=='contact' else ''}" onclick="window.location.href='/?page=contact'">Contact</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
