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
        padding: 1.2rem 2rem;
        height: 100px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        position: sticky;
        top: 0;
        z-index: 999;
    }

    .top-nav {
        display: flex;
        gap: 24px;
        flex-wrap: wrap;
        align-items: center;
    }

    .top-nav a {
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 8px 18px;
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
            height: auto;
        }

        .top-nav {
            justify-content: flex-start;
            margin-top: 10px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        cols = st.columns([1, 5])
        with cols[0]:
            st.image(logo, width=70)
        with cols[1]:
            st.markdown(f"""
            <div class="top-nav">
                <a href="/?page=home" class="{ 'active' if active == 'home' else '' }">Home</a>
                <a href="/?page=service" class="{ 'active' if active == 'service' else '' }">Service</a>
                <a href="/?page=login" class="{ 'active' if active == 'diagnosis' else '' }">Diagnosis</a>
                <a href="/?page=about" class="{ 'active' if active == 'about' else '' }">About</a>
                <a href="/?page=contact" class="{ 'active' if active == 'contact' else '' }">Contact</a>
            </div>
            """, unsafe_allow_html=True)
