import streamlit as st
from langdetect import detect, LangDetectException
import streamlit.components.v1 as components

def detect_language():
    try:
        lang = detect(st.session_state.get("text_input", "Wella.AI empowers healthcare anywhere."))
        return lang
    except (LangDetectException, Exception):
        return "en"

def landing_page():
    st.set_page_config(page_title="Wella.AI – Smart Diagnosis", layout="wide")

    # Hide sidebar permanently
    hide_sidebar = """
        <style>
            [data-testid="stSidebar"] {
                display: none !important;
            }
            [data-testid="collapsedControl"] {
                display: none !important;
            }
        </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

    st.session_state["text_input"] = st.text_input("✍️ Say something:", "")

    lang = detect_language()[:2]
    greetings = {
        "en": "Welcome to Wella.AI",
        "fr": "Bienvenue sur Wella.AI",
        "sw": "Karibu Wella.AI",
        "yo": "Kaabo si Wella.AI",
        "ha": "Barka da zuwa Wella.AI",
        "ig": "Nnọọ na Wella.AI",
        "es": "Bienvenido a Wella.AI"
    }
    welcome = greetings.get(lang, greetings["en"])
    st.success(welcome)

    # Responsive layout styles
    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(to right, #00b894, #00cec9);
        color: white;
        padding: 3rem 1.5rem;
        text-align: center;
        border-radius: 1rem;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 2.2rem;
    }
    .hero p {
        font-size: 1.2rem;
        margin-top: 1rem;
    }
    .launch-button {
        background-color: white;
        color: #00b894;
        font-weight: bold;
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        border: none;
        margin-top: 1.5rem;
        cursor: pointer;
    }
    .footer {
        text-align: center;
        font-size: 0.85rem;
        color: #777;
        margin-top: 3rem;
        padding: 1rem 0;
    }
    @media screen and (max-width: 768px) {
        .hero h1 {
            font-size: 1.5rem;
        }
        .hero p, .launch-button {
            font-size: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="hero">
        <h1>Wella.AI – Smart Diagnosis Anytime, Anywhere</h1>
        <p>Empowering rural clinics with AI-powered medical diagnosis – even offline.</p>
        <a href="/?page=login" target="_self">
            <button class="launch-button">🚀 Launch Wella.AI</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Content Blocks
    st.header("🌍 Supporting Underserved Communities")
    st.image("assets/robot.png", use_container_width=True)
    st.markdown("""
    **Rural clinics often lack access to specialists.**<br><br>
    Wella.AI empowers frontline healthcare workers with intelligent diagnostic tools to ensure no patient is left behind.
    """, unsafe_allow_html=True)

    st.header("⚙️ Seamless Workflow Integration")
    st.image("assets/cloud.png", use_container_width=True)
    st.markdown("""
    - Works **online and offline**.
    - Syncs to the cloud when connected.
    - Runs diagnoses offline.
    - Designed with doctors and nurses in mind.
    """, unsafe_allow_html=True)

    st.header("🔐 Secure and Role-Based Access")
    st.image("assets/roles.png", use_container_width=True)
    st.markdown("""
    Wella.AI supports **Admins**, **Doctors**, and **Nurses**, each with their own access level.
    Role-based logs ensure patient data integrity and security.
    """, unsafe_allow_html=True)

    # New Content Section
    st.header("📈 Why Choose Wella.AI")
    st.markdown("""
    - 🧠 **AI-powered diagnostics** trained on thousands of real cases
    - 🚑 **Offline-first design** built for low-connectivity zones
    - 📋 **Comprehensive patient records**
    - 🧩 **Modular design** to suit different clinical workflows
    - 🔍 **Analytics dashboard** for health trends and resource management
    """)

    st.header("🧪 Compatible With Existing Infrastructure")
    st.markdown("""
    Our tools are designed to integrate smoothly with your clinic’s existing systems.
    Wella.AI doesn’t replace healthcare professionals—it supercharges them.
    """)

    # Demo Video
    st.header("🎥 See Wella.AI in Action")
    st.video("assets/video/video01.mp4")

    # Testimonials Placeholder
    st.header("🗣️ What People Are Saying")
    st.markdown("Read firsthand feedback from the field. Our partners love the impact.")
    st.image("assets/testimonials.jpg", use_container_width=True)

    # Footer
    st.markdown('<div class="footer">&copy; 2025 Wella.AI. Built for rural health. All rights reserved.</div>', unsafe_allow_html=True)

# Uncomment the following line to run it in Streamlit
# landing_page()
