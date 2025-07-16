import streamlit as st

def render_header(active="home"):
    st.markdown(f"""
    <style>
    .top-nav {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 16px;
        padding: 0.5rem 1rem;
        background-color: #00b894;
        position: sticky;
        top: 0;
        z-index: 999;
    }}
    .top-nav a {{
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 6px 12px;
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

    @media (max-width: 600px) {{
        .top-nav {{
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }}
        .top-nav a {{
            font-size: 0.95rem;
            padding: 8px;
        }}
    }}
    </style>

    <div class="top-nav">
        <a href="/?page=home" class="{ 'active' if active == 'home' else '' }">Home</a>
        <a href="/?page=home" class="{ 'active' if active == 'service' else '' }">Service</a>
        <a href="/?page=login" class="{ 'active' if active == 'diagnosis' else '' }">Diagnosis</a>
        <a href="/?page=home" class="{ 'active' if active == 'about' else '' }">About Us</a>
        <a href="/?page=home" class="{ 'active' if active == 'contact' else '' }">Contact</a>
    </div>
    """, unsafe_allow_html=True)
