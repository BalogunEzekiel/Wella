import streamlit as st

def render_header(active="home"):
    st.markdown(f"""
    <style>
    .top-nav-wrapper {{
        position: fixed;
        top: 0;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #00b894;
        padding: 0.5rem 1rem;
        z-index: 9999;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}

    .top-nav-wrapper img {{
        height: 45px;
    }}

    .top-nav {{
        display: flex;
        gap: 18px;
        flex-wrap: wrap;
    }}

    .top-nav a {{
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 8px 14px;
        border-radius: 6px;
        transition: background-color 0.2s ease-in-out;
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
            padding: 0.8rem 1rem;
        }}
        .top-nav {{
            justify-content: center;
            margin-top: 0.4rem;
        }}
    }}

    /* Add body padding to avoid header overlap */
    .block-container {{
        padding-top: 80px !important;
    }}
    </style>

    <div class="top-nav-wrapper">
        <img src="assets/logo.png" alt="Logo">
        <div class="top-nav">
            <a href="/?page=home" class="{ 'active' if active == 'home' else '' }">Home</a>
            <a href="/?page=home#services" class="{ 'active' if active == 'service' else '' }">Service</a>
            <a href="/?page=login" class="{ 'active' if active == 'diagnosis' else '' }">Diagnosis</a>
            <a href="/?page=home#about" class="{ 'active' if active == 'about' else '' }">About Us</a>
            <a href="/?page=home#contact" class="{ 'active' if active == 'contact' else '' }">Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
