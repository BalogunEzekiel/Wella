import streamlit as st
from streamlit_option_menu import option_menu

# Import pages
import landing
import service
import about
import contact
import diagnosis

# Page config
st.set_page_config(page_title="Wella.AI", layout="wide", initial_sidebar_state="auto")

# Hide default Streamlit menu and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Sticky Top Navigation (CSS)
sticky_menu_style = """
    <style>
    div[data-testid="stHorizontalBlock"] > div:first-child {
        position: sticky;
        top: 0;
        z-index: 999;
        background-color: #fafafa;
        border-bottom: 1px solid #ddd;
        padding-top: 0.5rem;
    }
    </style>
"""
st.markdown(sticky_menu_style, unsafe_allow_html=True)

# Menu bar
selected = option_menu(
    menu_title="",  # No title
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

# Route based on selection
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
