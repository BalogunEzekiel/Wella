import streamlit as st
from langdetect import detect, LangDetectException

def detect_language():
    try:
        lang = detect(st.session_state.get("text_input", "Wella.AI empowers healthcare anywhere."))
        return lang
    except (LangDetectException, Exception):
        return "en"

def landing_page():
    st.set_page_config(page_title="Wella.AI – Smart Diagnosis", layout="wide")

    # ✅ Place the input at the top (MAIN page)
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

    # Custom CSS
    st.markdown("""
    <style>
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

    # Hero section
    st.markdown("""
    <div class="hero">
        <h1>Wella.AI – Smart Diagnosis Anytime, Anywhere</h1>
        <p>Empowering rural clinics with AI-powered medical diagnosis – even offline.</p>
        <a href="/?page=login" target="_self">
            <button class="launch-button">🚀 Launch Wella.AI</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Section: Two columns (Image | Text)
    st.subheader("🌍 Supporting Underserved Communities")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/Ezekiel.jpg", use_container_width=True)
    with col2:
        st.markdown("""
        **Rural clinics often lack access to specialists.**
        <br><br>
        Wella.AI provides frontline healthcare workers with intelligent diagnostic tools to ensure no patient is left behind.
        """, unsafe_allow_html=True)

    # Section: Three columns (Image | Text | Image)
    st.subheader("⚙️ Seamless Workflow Integration")
    col3, col4, col5 = st.columns([1.2, 1.6, 1.2])
    with col3:
        st.image("assets/Ezekiel.jpg", use_container_width=True)
    with col4:
        st.markdown("""
        **Works online and offline**<br>
        Syncs to the cloud when connected and runs diagnoses offline when not.<br><br>
        **Built for simplicity**<br>
        Designed with input from actual field nurses and doctors.
        """, unsafe_allow_html=True)
    with col5:
        st.image("assets/Ezekiel.jpg", use_container_width=True)

    # Section: Two columns (Text | Image)
    st.subheader("🔐 Secure and Role-Based Access")
    col6, col7 = st.columns([2, 1])
    with col6:
        st.markdown("""
        **Multiple user roles.**<br><br>
        Wella.AI supports Admins, Doctors, and Nurses, each with unique access rights and logs to ensure proper patient handling.
        """, unsafe_allow_html=True)
    with col7:
        st.image("assets/Ezekiel.jpg", use_container_width=True)

    # Embedded video section
    st.subheader("🎥 See Wella.AI in Action")
    video_path = "assets/video/video01.mp4"
    st.video(video_path)

    # Testimonials
    st.subheader("🗣️ What People Are Saying")

    testimonials = [
        {
            "img": "assets/image.jpg",
            "quote": "Wella.AI has revolutionized how we handle patients in our village clinic.",
            "name": "Dr. Grace Okoro"
        },
        {
            "img": "assets/nurse.png",
            "quote": "We no longer panic during network outages—Wella.AI is always ready.",
            "name": "Nurse Michael Yusuf"
        }
    ]
    
    for t in testimonials:
        with st.container():
            colA, colB = st.columns([1, 4])
            with colA:
                st.image(t["img"], width=200, caption="")
            with colB:
                st.markdown(f"""
                    <div style="
                        background: linear-gradient(to right, #f0f4f8, #e6f7ff);
                        border-radius: 16px;
                        padding: 15px 20px;
                        margin-top: 10px;
                        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                    ">
                        <p style="margin: 0; font-weight: bold; font-size: 1.2rem; color: #003366;">{t['name']}</p>
                        <p style="margin: 4px 0 6px; font-size: 1rem; color: #ffaa00;">★★★★★ <span style="font-size: 0.9rem; color: #444;">5/5</span></p>
                        <p style="margin: 0; font-size: 1.05rem; font-style: italic; color: #333;">“{t['quote']}”</p>
                    </div>
                """, unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">&copy; 2025 Wella.AI. All rights reserved.</div>', unsafe_allow_html=True)
