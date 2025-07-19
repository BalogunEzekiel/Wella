import streamlit as st
from langdetect import detect as detect_language

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

    # ✅ Safe language detection with fallback
    try:
        detected = detect_language()
        lang = detected[:2] if detected else "en"
    except Exception as e:
        print(f"Language detection failed: {e}")
        lang = "en"
    
    # 🌍 Multilingual greetings
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

    # Shared styles for content
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

    # Section 1
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

    # Section 2
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

    # Section 3
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

    # Additional Sections
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

    st.header("🎥 See Wella.AI in Action")
    st.video("assets/video/video01.mp4")

    st.header("🗣️ What People Are Saying")
    st.markdown("Read firsthand feedback from the field. Our partners love the impact.")
    st.image("assets/AI_Me.png", use_container_width=True)

    testimonials_html = """
    <style>
        .testimonial-carousel {
            max-width: 100%;
            margin: auto;
            overflow: hidden;
            position: relative;
            padding: 10px;
        }
        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            align-items: stretch;
            transition: transform 0.5s ease-in-out;
        }
        .testimonial-card {
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 20px;
            border-radius: 16px;
            background: linear-gradient(135deg, #e0f7fa, #fce4ec);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            min-height: 260px;
        }
        .testimonial-card img {
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 50%;
            margin-right: 20px;
            border: 4px solid #fff;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .testimonial-text {
            font-size: 1rem;
            font-style: italic;
            color: #333;
        }
        .testimonial-name {
            margin-top: 10px;
            font-weight: bold;
            font-size: 1.1rem;
            color: #0077b6;
        }
        .stars {
            color: #ffa500;
            margin-bottom: 6px;
            font-size: 1.05rem;
        }
        .dot-container {
            text-align: center;
            margin-top: 10px;
        }
        .dot {
            height: 12px;
            width: 12px;
            margin: 4px 6px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.3s ease;
        }
        .active-dot {
            background-color: #0077b6;
        }
        @media (max-width: 768px) {
            .testimonial-card {
                flex-direction: column;
                text-align: center;
            }
            .testimonial-card img {
                margin-right: 0;
                margin-bottom: 12px;
            }
        }
    </style>

    <div class="testimonial-carousel">
        <div id="testimonial-slides">
            <!-- Slide 1 -->
            <div class="testimonial-grid" style="display: grid;">
                <div class="testimonial-card">
                    <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/image.jpg">
                    <div>
                        <div class="testimonial-text">“Wella.AI is a game-changer for rural healthcare. We diagnose faster and more accurately, even offline.”</div>
                        <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
                        <div class="testimonial-name">Dr. Amina Yusuf</div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/nurse.png">
                    <div>
                        <div class="testimonial-text">“We no longer panic during network outages—Wella.AI is always ready.”</div>
                        <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
                        <div class="testimonial-name">Nurse Michael Yusuf</div>
                    </div>
                </div>
            </div>

            <!-- Slide 2 -->
            <div class="testimonial-grid" style="display: none;">
                <div class="testimonial-card">
                    <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/offline.png">
                    <div>
                        <div class="testimonial-text">“Thanks to Wella.AI, I can now confidently assist in patient triage even without a doctor around.”</div>
                        <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
                        <div class="testimonial-name">Amaka Udo, Community Health Worker</div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/ngo.png">
                    <div>
                        <div class="testimonial-text">“Wella.AI aligns perfectly with our mission to reduce healthcare disparities in underserved regions.”</div>
                        <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
                        <div class="testimonial-name">John Mensah, MedServe Africa</div>
                    </div>
                </div>
            </div>

            <!-- Slide 3 -->
            <div class="testimonial-grid" style="display: none;">
                <div class="testimonial-card">
                    <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/commission.png">
                    <div>
                        <div class="testimonial-text">“We’ve seen a significant improvement in diagnosis speed in our primary healthcare centers.”</div>
                        <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
                        <div class="testimonial-name">Hon. Aisha Bello, Health Commissioner</div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/image.jpg">
                    <div>
                        <div class="testimonial-text">“Wella.AI has revolutionized how we handle patients in our village clinic.”</div>
                        <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
                        <div class="testimonial-name">Dr. Grace Okoro</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="dot-container">
            <span class="dot active-dot"></span>
            <span class="dot"></span>
            <span class="dot"></span>
        </div>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.testimonial-grid');
        const dots = document.querySelectorAll('.dot');

        function showSlide(index) {
            slides.forEach((s, i) => s.style.display = i === index ? 'grid' : 'none');
            dots.forEach((d, i) => d.className = i === index ? 'dot active-dot' : 'dot');
        }

        function nextSlide() {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        }

        dots.forEach((dot, index) => {
            dot.onclick = () => {
                currentSlide = index;
                showSlide(index);
            };
        });

        showSlide(currentSlide);
        setInterval(nextSlide, 6000);
    </script>
    """

    import streamlit.components.v1 as components
    components.html(testimonials_html, height=540)

    st.markdown('<div class="footer">&copy; 2025 Wella.AI. Built for rural health. All rights reserved.</div>', unsafe_allow_html=True)
    
# Run the landing page if this file is executed directly
landing_page()
