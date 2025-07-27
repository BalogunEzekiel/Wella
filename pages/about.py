
import streamlit as st

def show_about():
    # Page config
    st.set_page_config(page_title="About Wella.AI", layout="wide")

    # Inject responsive styling
    st.markdown("""
        <style>
        /* Remove sidebar space */
        [data-testid="stSidebar"] {
            display: none;
        }

        /* Full width content for mobile */
        [data-testid="stAppViewContainer"] > .main {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-section {
            text-align: center;
            padding: 2rem 0;
        }

        @media screen and (max-width: 768px) {
            .element-container:has(img), .element-container:has(video) {
                text-align: center !important;
            }
            .block-container {
                padding: 1rem 0.5rem !important;
            }
            h1, h2, h3, h4 {
                font-size: 1.2rem !important;
            }
            p, li {
                font-size: 0.95rem !important;
                line-height: 1.5;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown("## Welcome to Wella.AI")
    st.write("At Wella.AI, we believe in revolutionizing rural healthcare using the power of AI, data, and offline technology.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- WHO WE ARE ---
    st.markdown("### Who We Are", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/offline.png", caption="Our Founding Team", use_container_width=True)
    with col2:
        st.write("""
        Wella.AI was founded with a clear goal – to bridge the healthcare gap in underserved communities using intelligent technology. 
        We focus on developing diagnostic and patient management tools that work **offline**, making them ideal for rural and remote locations.

        From real-time diagnosis to secure data handling, Wella.AI is built for **impact** and **accessibility**.
        """)

    # --- MISSION AND VISION ---
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 Our Mission")
        st.write("To empower frontline health workers with AI-driven tools that enhance diagnosis, treatment, and patient outcomes—regardless of internet access.")
    with col2:
        st.subheader("🌍 Our Vision")
        st.write("A world where every clinic, no matter how remote, can deliver accurate and timely healthcare with the support of intelligent technology.")

    # --- CORE VALUES ---
    st.markdown("### Our Core Values", unsafe_allow_html=True)
    values = {
        "🔒 Privacy First": "We prioritize patient confidentiality and data security.",
        "💡 Innovation": "We build cutting-edge solutions with real-world usability.",
        "🤝 Collaboration": "We work with communities, not just for them.",
        "📶 Offline Access": "Our tools are designed to function without constant internet."
    }
    for icon, desc in values.items():
        st.markdown(f"- **{icon}** {desc}")

    # --- TEAM SECTION ---
    st.markdown("### Meet the Team", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/AI_Me.png", caption="Dr. Ada Okoro – Co-Founder", use_container_width=True)
    with col2:
        st.image("assets/AI_Me.png", caption="Emeka Balogun – CTO", use_container_width=True)
    with col3:
        st.image("assets/AI_Me.png", caption="Sarah Bello – Operations Lead", use_container_width=True)

    # --- IMPACT STORIES ---
    st.markdown("### User Impact Stories", unsafe_allow_html=True)
    st.write("Here’s how Wella.AI is already changing lives in rural clinics:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.video("assets/video/video02.mp4")  # Local video file
    
    with col2:
        st.write("""
        *“Before Wella.AI, diagnosing patients took hours and paperwork. Now we can confidently make decisions with just a few taps—even without internet!”*  
        — Nurse Grace, Kogi State  
        """)

    # --- GALLERY ---
    st.markdown("### In Pictures", unsafe_allow_html=True)
    image_cols = st.columns(4)
    for i in range(4):
        image_cols[i].image(f"assets/AI_Me.png", use_container_width=True)

    # --- CALL TO ACTION ---
    st.markdown("### Join Us in Transforming Healthcare", unsafe_allow_html=True)
    st.markdown("""
    We are open to collaborations, pilots and partnerships. Let’s make healthcare smarter, together.
    """)
