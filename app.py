import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from utils.db import init_db
from pytz import timezone

# Import pages
from pages import landing
from pages import service
from pages import about
from pages import contact
from pages import diagnosis

# Page config
st.set_page_config(page_title="Wella.AI", layout="wide", initial_sidebar_state="auto")

# Initialize users table
init_db()

# Hide Streamlit's default menu and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Sticky top navigation styling
sticky_menu_style = """
    <style>
    .sticky-nav {
        position: sticky;
        top: 0;
        z-index: 999;
        background-color: #fafafa;
        border-bottom: 1px solid #ddd;
        padding: 10px 0 5px 0;
    }
    .nav-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .logo {
        height: 50px;
        margin-left: 20px;
    }
    </style>
"""
st.markdown(sticky_menu_style, unsafe_allow_html=True)

# Render sticky menu container
with st.container():
    st.markdown('<div class="sticky-nav"><div class="nav-container">', unsafe_allow_html=True)
    
    # Left-aligned logo
    col1, col2 = st.columns([1, 8])
    with col1:
        try:
            logo = Image.open("assets/logo.png")
            st.image(logo, use_container_width=False, width=100)
        except:
            st.write("Logo not found")

    # Right-aligned menu
    with col2:
        selected = option_menu(
            menu_title="",
            options=["Home", "Service", "Diagnosis", "About", "Contact"],
            icons=["house", "briefcase", "activity", "info-circle", "envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#fafafa",
                },
                "icon": {"color": "black", "font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#5c9ead"},
            },
            key="main_menu"
        )
    
    st.markdown('</div></div>', unsafe_allow_html=True)  # Close divs

# Route pages
if selected == "Home":
    landing.landing_page()
elif selected == "Service":
    service.show_service()
elif selected == "Diagnosis":
    diagnosis.show_diagnosis()
elif selected == "About":
    about.show_about()
elif selected == "Contact":
    contact.show_contact()
