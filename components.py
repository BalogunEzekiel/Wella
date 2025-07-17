import streamlit as st

def render_header(active="home"):
    st.markdown(f"""
    <style>
    .top-nav-wrapper {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #00b894;
        padding: 1rem 1.5rem;
        height: 80px;
        position: sticky;
        top: 0;
        z-index: 999;
    }}

    .logo {{
        height: 60px;
    }}

    .top-nav {{
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }}

    .top-nav a {{
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 8px 16px;
        border-radius: 6px;
        transition: background-color 0.2s;
    }}

    .top-nav a:hover {{
        background-color: #00a383;
    }}

    .top-nav a.active {{
        text-decoration: underline;
        background-color: #009d7a;
    }}

    @media (max-width: 768px) {{
        .top-nav-wrapper {{
            flex-direction: column;
            align-items: center;
            height: auto;
            padding: 1rem;
        }}

        .top-nav {{
            justify-content: center;
            margin-top: 0.5rem;
        }}

        .logo {{
            height: 50px;
        }}
    }}
    </style>

    <div class="top-nav-wrapper">
        <img src="assets/logo.png" class="logo" alt="Logo">
        <div class="top-nav">
            <a href="/?page=home" class="{ 'active' if active == 'home' else '' }">Home</a>
            <a href="/?page=home" class="{ 'active' if active == 'service' else '' }">Service</a>
            <a href="/?page=login" class="{ 'active' if active == 'diagnosis' else '' }">Diagnosis</a>
            <a href="/?page=home" class="{ 'active' if active == 'about' else '' }">About Us</a>
            <a href="/?page=home" class="{ 'active' if active == 'contact' else '' }">Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
