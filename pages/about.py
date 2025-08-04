
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
        st.image("assets/AI_Me.png", caption="Ezekiel BALOGUN – Data Scientist, Software Developer", use_container_width=True)
    with col2:
        st.image("assets/kemi.jpg", caption="Oluwakemi Adesanwo – Data Analyst, AI/ML Engineer", use_container_width=True)
    with col3:
        st.image("assets/kemi.jpg", caption="Sarah Bello – Operations/BI Analyst", use_container_width=True)

    # --- IMPACT STORIES ---
    st.markdown("### User Impact Stories", unsafe_allow_html=True)
    st.write("Here’s how Wella.AI is already changing lives in rural clinics:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.video("assets/video/video04.mp4")  # Local video file
    
    with col2:
        st.write("""
        *“Before Wella.AI, diagnosing patients took hours and paperwork. Now we can confidently make decisions with just a few taps—even without internet!”*  
        — Nurse Grace, Kogi State  
        """)

    # --- GALLERY ---
    st.markdown("### 🖼️ In Pictures", unsafe_allow_html=True)

    # --- CSS for card and hover effect ---
    st.markdown("""
        <style>
            .img-card {
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                transition: transform 0.3s, box-shadow 0.3s;
                margin-bottom: 10px;
            }
    
            .img-card:hover {
                transform: scale(1.02);
                box-shadow: 0 6px 18px rgba(0,0,0,0.2);
            }
    
            .img-caption {
                text-align: center;
                font-weight: 500;
                margin-top: 5px;
            }
    
            .gallery-img {
                width: 100%;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # --- Image paths and captions ---
    image_info = [
        ("assets/AI_Me.png", "AI Avatar"),
        ("assets/homepage.jpg", "Homepage"),
        ("assets/admin dashboard.jpg", "Admin Dashboard"),
        ("assets/nurse dashboard.jpg", "Nurse Dashboard"),
        ("assets/doctor dashboard.jpg", "Doctor Dashboard"),
        ("assets/diagnosis.jpg", "Diagnosis Report"),
        ("assets/treatment.jpg", "Treatment Report")
    ]
    
    # --- Helper function to convert image to base64 ---
    def get_image_base64(image_path):
        if not os.path.isfile(image_path):
            return ""
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            ext = os.path.splitext(image_path)[1][1:]  # get extension like 'png'
            return f"data:image/{ext};base64,{encoded}"
    
    # --- Display images in rows ---
    cols_per_row = 4
    for i in range(0, len(image_info), cols_per_row):
        row = image_info[i:i + cols_per_row]
        cols = st.columns(len(row))
        for col, (path, caption) in zip(cols, row):
            with col:
                img_data = get_image_base64(path)
                if img_data:
                    st.markdown(f"""
                        <div class="img-card">
                            <a href="{img_data}" target="_blank">
                                <img src="{img_data}" class="gallery-img"/>
                            </a>
                            <div class="img-caption">{caption}</div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.warning(f"Image not found: {caption}")
                
            
#######################
    st.markdown("### 🖼️ In Pictures", unsafe_allow_html=True)

    # Role-based grouped images with paths, captions, and URLs
    grouped_images = {
        "General": [
            ("assets/AI_Me.png", "The Visionary", "#"),
            ("assets/homepage.jpg", "Homepage", "#"),
        ],
        "Admin": [
            ("assets/admin dashboard.jpg", "Admin Dashboard", "#"),
        ],
        "Nurse": [
            ("assets/nurse dashboard.jpg", "Nurse Dashboard", "#"),
            ("assets/diagnosis.jpg", "Diagnosis Report", "#"),
        ],
        "Doctor": [
            ("assets/doctor dashboard.jpg", "Doctor Dashboard", "#"),
            ("assets/treatment.jpg", "Treatment Report", "#"),
        ]
    }
    
    cols_per_row = 4
    
    for role, image_list in grouped_images.items():
        st.markdown(f"#### 👤 {role} View", unsafe_allow_html=True)
        for i in range(0, len(image_list), cols_per_row):
            row = image_list[i:i+cols_per_row]
            cols = st.columns(len(row))
            for col, (path, caption, url) in zip(cols, row):
                with col:
                    # Wrap image in a link
                    st.markdown(f'<a href="{url}" target="_blank">', unsafe_allow_html=True)
                    st.image(path, caption=caption, use_container_width=True)
                    st.markdown('</a>', unsafe_allow_html=True)
                
    # --- CALL TO ACTION ---
    st.markdown("### Join Us in Transforming Healthcare", unsafe_allow_html=True)
    
    st.markdown("""
    We’re on a mission to revolutionize healthcare with AI-powered solutions.  
    Whether you're a hospital, clinic, healthtech innovator, or investor — **let’s partner** to make healthcare smarter, faster, and more accessible.
    
    _We welcome collaborations, pilot programs and strategic partnerships._
    """, unsafe_allow_html=True)
