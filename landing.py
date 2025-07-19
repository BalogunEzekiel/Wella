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
    st.markdown("""
        <style>
        .section-title {
            font-size: 26px;
            font-weight: bold;
            color: #1f77b4;
            margin-bottom: 0.5rem;
        }
        .highlight-text {
            font-size: 18px;
            color: #444;
            font-weight: 600;
            line-height: 1.6;
        }
        .bullet-points {
            font-size: 17px;
            color: #333;
            font-weight: 500;
            line-height: 1.7;
            margin-top: 10px;
        }
        .stColumn {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        hr {
            border: none;
            height: 1px;
            background: #ddd;
            margin: 2rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # ---------- Section 1 ----------
    st.markdown('<div class="section-title">🌍 Supporting Underserved Communities</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/robot.png", use_container_width=True)
    with col2:
        st.markdown("""
        <div class="highlight-text">
            Many rural clinics lack access to <strong>medical specialists</strong>.<br><br>
            <span style='color:#1f77b4;'>Wella.AI</span> equips frontline healthcare workers with smart diagnostic tools, 
            ensuring that <strong>no patient is left behind</strong>.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ---------- Section 2 ----------
    st.markdown('<div class="section-title">⚙️ Seamless Workflow Integration</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.image("assets/cloud.png", use_container_width=True)
    with col4:
        st.markdown("""
        <div class="bullet-points">
            ✅ <strong>Works both online and offline</strong><br>
            🔄 <strong>Syncs to the cloud</strong> automatically when connected<br>
            ⚡ <strong>Runs diagnoses instantly</strong> — even without internet<br>
            👨‍⚕️ <strong>Intuitively designed</strong> for doctors and nurses
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ---------- Section 3 ----------
    st.markdown('<div class="section-title">🔐 Secure and Role-Based Access</div>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        st.image("assets/roles.png", use_container_width=True)
    with col6:
        st.markdown("""
        <div class="highlight-text">
            <span style='color:#1f77b4;'>Wella.AI</span> supports <strong>Admins</strong>, <strong>Doctors</strong>, and <strong>Nurses</strong> — each with secure, role-specific access.<br><br>
            Activity logs ensure <strong>data privacy</strong> and <strong>integrity</strong> across the system.
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
    
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
landing_page()
