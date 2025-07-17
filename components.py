import streamlit as st

def render_header(active="home"):
    st.markdown("""
    <style>
    /* Fix Streamlit default margin issues */
    .css-18e3th9 {
        padding-top: 0 !important;
    }

    .top-nav-wrapper {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #00b894;
        padding: 1.2rem 2rem;
        height: 90px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        position: sticky;
        top: 0;
        z-index: 999;
    }

    .logo {
        height: 70px;
        margin-right: 30px;
    }

    .top-nav {
        display: flex;
        gap: 24px;
        flex-wrap: wrap;
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

        .logo {
            height: 60px;
            margin-bottom: 12px;
        }

        .top-nav {
            justify-content: flex-start;
        }
    }
    </style>

    <div class="top-nav-wrapper">
        <img src="assets/logo.png" class="logo" alt="Wella.AI Logo">
        <div class="top-nav">
            <a href="/?page=home" class="%s">Home</a>
            <a href="/?page=home" class="%s">Service</a>
            <a href="/?page=login" class="%s">Diagnosis</a>
            <a href="/?page=home" class="%s">About</a>
            <a href="/?page=home" class="%s">Contact</a>
        </div>
    </div>
    """ % (
        "active" if active == "home" else "",
        "active" if active == "service" else "",
        "active" if active == "diagnosis" else "",
        "active" if active == "about" else "",
        "active" if active == "contact" else ""
    ), unsafe_allow_html=True)
