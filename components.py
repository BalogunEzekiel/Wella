import streamlit as st

def render_header():
    st.markdown("""
        <style>
        .top-nav {
            display: flex;
            justify-content: center;
            gap: 30px;
            padding: 0.5rem 0;
            margin-bottom: 1rem;
            background-color: #00b894;
            position: sticky;
            top: 0;
            z-index: 999;
        }
        .top-nav a {
            color: white;
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            padding: 6px 12px;
            border-radius: 6px;
            transition: background-color 0.2s;
        }
        .top-nav a:hover {
            background-color: #00a383;
        }
        </style>
        <div class="top-nav">
            <a href="/?page=home">Home</a>
            <a href="/?page=home">Service</a>
            <a href="/?page=home">About Us</a>
            <a href="/?page=home">Contact</a>
        </div>
    """, unsafe_allow_html=True)
