import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Load Lottie animation JSON
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def landing_page():
    st.set_page_config(page_title="Wella.AI – Smart Diagnosis", layout="wide")

    # Custom Styles
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .hero h1 { font-size: 2rem !important; }
        .hero p { font-size: 1rem !important; }
        .feature-box h4 { font-size: 1rem; }
    }

    .hero {
        background: linear-gradient(to right, #00b894, #00cec9);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 1rem;
        margin-bottom: 3rem;
    }

    .launch-button {
        background-color: white;
        color: #00b894;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        border: none;
        cursor: pointer;
        margin-top: 2rem;
    }

    .features-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
        justify-content: center;
    }

    .feature-box {
        background: #f9f9f9;
        padding: 1.5rem;
        border-radius: 1rem;
        width: 260px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .testimonial-card {
        background-color: #ffffff;
        border-radius: 1rem;
        padding: 1rem;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        gap: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    .testimonial-card img {
        border-radius: 50%;
        width: 60px;
        height: 60px;
        object-fit: cover;
    }

    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: gray;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Logo
    st.image("assets/logo.png", width=150)

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

    # Lottie Animation
    lottie_url = "https://lottie.host/7e56cd0e-4cf6-46e4-9df7-44c23db0de64/vnmWBYb7Hq.json"
    lottie_json = load_lottie_url(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=300, speed=1)
    else:
        st.warning("⚠️ Lottie animation failed to load.")

    # Feature Highlights
    st.subheader("💡 Key Features")
    st.markdown('<div class="features-grid">', unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-box">
            <h4>🧠 AI-Powered Diagnosis</h4>
            <p>Instant suggestions based on symptoms.</p>
        </div>
        <div class="feature-box">
            <h4>📴 Offline Mode</h4>
            <p>Designed for areas without stable internet.</p>
        </div>
        <div class="feature-box">
            <h4>👥 Role-Based Access</h4>
            <p>Admins, Doctors, Nurses with restricted views.</p>
        </div>
        <div class="feature-box">
            <h4>☁️ Cloud Sync</h4>
            <p>Auto sync with Supabase when online.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Testimonials
    st.subheader("🗣️ What People Are Saying")

    testimonials = [
        {
            "img": "assets/Ezekiel Balogun.jpg",
            "quote": "Wella.AI has revolutionized how we handle patients in our village clinic.",
            "name": "Dr. Grace Okoro"
        },
        {
            "img": "assets/picturepucture0001.jpg",
            "quote": "We no longer panic during network outages—Wella.AI is always ready.",
            "name": "Nurse Michael Yusuf"
        }
    ]

    for t in testimonials:
        st.markdown(f"""
        <div class="testimonial-card">
            <img src="{t['img']}" alt="avatar" />
            <div>
                <p><strong>{t['name']}</strong></p>
                <p style="font-style:italic;">“{t['quote']}”</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">&copy; © 2025 Wella.AI. All rights reserved.</div>', unsafe_allow_html=True)
