import streamlit as st
from PIL import Image

def render_header(active="home"):
    logo = Image.open("assets/logo.png")

    st.markdown("""
    <style>
    .top-nav-wrapper {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #00b894;
        padding: 1.5rem 2rem;
        height: auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        position: sticky;
        top: 0;
        z-index: 999;
        flex-wrap: wrap;
    }

    .logo-container img {
        height: 70px;
        margin-right: 20px;
    }

    .top-nav {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        align-items: center;
    }

    .top-nav a {
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 10px 16px;
        border-radius: 6px;
        transition: background-color 0.2s ease-in-out;
    }

    .top-nav a:hover {
        background-color: #009973;
    }

    .top-nav a.active {
        background-color: #007b5e;
        text-decoration: underline;
    }

    @media (max-width: 768px) {
        .top-nav-wrapper {
            flex-direction: column;
            align-items: flex-start;
        }

        .top-nav {
            margin-top: 10px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Header HTML structure
    st.markdown(f"""
    <div class="top-nav-wrapper">
        <div class="logo-container">
            <img src="data:image/png;base64,{st.image_to_bytes(logo).decode()}" />
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
