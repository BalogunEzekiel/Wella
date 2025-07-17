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
    .top-nav-wrapper {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #00b894;
        padding: 1.5rem 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        height: auto;
        flex-wrap: wrap;
    }}

    .logo-container {{
        display: flex;
        align-items: center;
    }}

    .logo-container img {{
        height: 70px;
        margin-right: 20px;
    }}

    .top-nav {{
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }}

    .top-nav button {{
        background-color: transparent;
        border: none;
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 10px 18px;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out;
    }}

    .top-nav button:hover {{
        background-color: #009973;
    }}

    .top-nav button.active {{
        background-color: #007b5e;
        text-decoration: underline;
    }}

    </style>

    <div class="top-nav-wrapper">
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" alt="Wella.AI Logo" />
        </div>
        <div class="top-nav">
            <form action="" method="post">
                <button class="{ 'active' if active == 'home' else '' }" name="nav" value="home">Home</button>
                <button class="{ 'active' if active == 'service' else '' }" name="nav" value="service">Service</button>
                <button class="{ 'active' if active == 'diagnosis' else '' }" name="nav" value="diagnosis">Diagnosis</button>
                <button class="{ 'active' if active == 'about' else '' }" name="nav" value="about">About</button>
                <button class="{ 'active' if active == 'contact' else '' }" name="nav" value="contact">Contact</button>
            </form>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Get navigation result
    nav = st.session_state.get("nav", active)
    if "nav" in st.experimental_get_query_params():
        nav = st.experimental_get_query_params()["nav"][0]
    return nav
