import streamlit as st
from langdetect import detect, LangDetectException
from components import render_header
import streamlit.components.v1 as components

def detect_language():
    try:
        lang = detect(st.session_state.get("text_input", "Wella.AI empowers healthcare anywhere."))
        return lang
    except (LangDetectException, Exception):
        return "en"

def landing_page():
    st.set_page_config(page_title="Wella.AI – Smart Diagnosis", layout="wide")
    
    # 🔒 Static Header
    render_header(active="home")

    # Input field at the top
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
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Logo
    st.image("assets/logo.png", width=150)

    # Hero section
    st.markdown(
        """
        <style>
            .hero-carousel {
                position: relative;
                width: 100%;
                height: 400px;
                overflow: hidden;
                border-radius: 20px;
                margin-bottom: 2rem;
                box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            }
    
            .hero-carousel-slide {
                position: absolute;
                width: 100%;
                height: 100%;
                opacity: 0;
                transition: opacity 1s ease-in-out;
                background-size: cover;
                background-position: center;
            }
    
            .hero-carousel-slide.active {
                opacity: 1;
            }
    
            .hero-overlay {
                position: absolute;
                bottom: 30px;
                left: 30px;
                color: white;
                background-color: rgba(0,0,0,0.6);
                padding: 20px;
                border-radius: 12px;
            }
    
            .launch-button {
                margin-top: 10px;
                background-color: #00c78c;
                border: none;
                padding: 10px 20px;
                border-radius: 25px;
                color: white;
                font-size: 1.1rem;
                cursor: pointer;
                box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);
            }
    
            @keyframes heroSlider {
                0% { opacity: 1; }
                25% { opacity: 0; }
                50% { opacity: 1; }
                75% { opacity: 0; }
                100% { opacity: 1; }
            }
    
            .hero-carousel-slide:nth-child(1) {
                animation: heroSlider 20s infinite;
                animation-delay: 0s;
            }
            .hero-carousel-slide:nth-child(2) {
                animation: heroSlider 20s infinite;
                animation-delay: 5s;
            }
            .hero-carousel-slide:nth-child(3) {
                animation: heroSlider 20s infinite;
                animation-delay: 10s;
            }
            .hero-carousel-slide:nth-child(4) {
                animation: heroSlider 20s infinite;
                animation-delay: 15s;
            }
    
        </style>
    
        <div class="hero-carousel">
            <div class="hero-carousel-slide" style="background-image: url('assets/wella.jpg');">
                <div class="hero-overlay">
                    <h1>Wella.AI – Smart Diagnosis Anytime, Anywhere</h1>
                    <p>Empowering rural clinics with AI-powered medical diagnosis – even offline.</p>
                    <a href="/?page=login"><button class="launch-button">🚀 Launch Wella.AI</button></a>
                </div>
            </div>
            <div class="hero-carousel-slide" style="background-image: url('assets/illustration.jpg');">
                <div class="hero-overlay">
                    <h1>Transforming Healthcare Access</h1>
                    <p>AI-powered tools designed to work even without internet.</p>
                    <a href="/?page=login"><button class="launch-button">🚀 Try Wella.AI</button></a>
                </div>
            </div>
            <div class="hero-carousel-slide" style="background-image: url('assets/logo.png');">
                <div class="hero-overlay">
                    <h1>Seamless Offline Diagnosis</h1>
                    <p>Helping frontline workers make faster, smarter decisions.</p>
                    <a href="/?page=login"><button class="launch-button">🚀 Explore Wella.AI</button></a>
                </div>
            </div>
            <div class="hero-carousel-slide" style="background-image: url('assets/raspberry.avif');">
                <div class="hero-overlay">
                    <h1>Low-Cost Hardware Integration</h1>
                    <p>Optimized for Raspberry Pi & other low-resource devices.</p>
                    <a href="/?page=login"><button class="launch-button">🚀 Learn More</button></a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Two columns (Image | Text)
    st.subheader("🌍 Supporting Underserved Communities")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/robot.png", use_container_width=True)
    with col2:
        st.markdown("""
        **Rural clinics often lack access to specialists.**
        <br><br>
        Wella.AI provides frontline healthcare workers with intelligent diagnostic tools to ensure no patient is left behind.
        """, unsafe_allow_html=True)

    # Three columns (Image | Text | Image)
    st.subheader("⚙️ Seamless Workflow Integration")
    col3, col4, col5 = st.columns([1.2, 1.6, 1.2])
    with col3:
        st.image("assets/cloud.png", use_container_width=True)
    with col4:
        st.markdown("""
        **Works online and offline**<br>
        Syncs to the cloud when connected and runs diagnoses offline when not.<br><br>
        **Built for simplicity**<br>
        Designed with input from actual field nurses and doctors.
        """, unsafe_allow_html=True)
    with col5:
        st.image("assets/Ezekiel.jpg", use_container_width=True)

    # Two columns (Text | Image)
    st.subheader("🔐 Secure and Role-Based Access")
    col6, col7 = st.columns([2, 1])
    with col6:
        st.markdown("""
        **Multiple user roles.**<br><br>
        Wella.AI supports Admins, Doctors and Nurses, each with unique access rights and logs to ensure proper patient handling.
        """, unsafe_allow_html=True)
    with col7:
        st.image("assets/Ezekiel.jpg", use_container_width=True)

    # Video section
    st.subheader("🎥 See Wella.AI in Action")
    video_path = "assets/video/video01.mp4"
    st.video(video_path)

    # Testimonials    
    st.subheader("🗣️ What People Are Saying")
    
    testimonials_html = """
    <style>
    .testimonial-carousel {
        max-width: 100%;
        margin: auto;
        overflow: hidden;
        position: relative;
        padding: 10px;
    }
    .testimonial-card {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 20px;
        border-radius: 16px;
        background: linear-gradient(135deg, #e0f7fa, #fce4ec);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        transition: transform 0.5s ease;
        min-height: 260px;
    }
    .testimonial-card img {
        width: 160px;
        height: 160px;
        object-fit: cover;
        border-radius: 50%;
        margin-right: 25px;
        border: 4px solid #fff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .testimonial-text {
        font-size: 1.1rem;
        font-style: italic;
        color: #333;
    }
    .testimonial-name {
        margin-top: 10px;
        font-weight: bold;
        font-size: 1.2rem;
        color: #0077b6;
    }
    .stars {
        color: #ffa500;
        margin-bottom: 8px;
        font-size: 1.1rem;
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
    </style>
    
    <div class="testimonial-carousel" id="carousel">
      <div class="testimonial-card" id="slide">
        <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/image.jpg">
        <div>
          <div class="testimonial-text">“Wella.AI has revolutionized how we handle patients in our village clinic.”</div>
          <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
          <div class="testimonial-name">Dr. Grace Okoro</div>
        </div>
      </div>
      <div class="testimonial-card" style="display: none;">
        <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/nurse.png">
        <div>
          <div class="testimonial-text">“We no longer panic during network outages—Wella.AI is always ready.”</div>
          <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
          <div class="testimonial-name">Nurse Michael Yusuf</div>
        </div>
      </div>
      <div class="testimonial-card" style="display: none;">
        <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/offline.png">
        <div>
          <div class="testimonial-text">“Thanks to Wella.AI, I can now confidently assist in patient triage even without a doctor around.”</div>
          <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
          <div class="testimonial-name">Amaka Udo, Community Health Worker</div>
        </div>
      </div>
      <div class="testimonial-card" style="display: none;">
        <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/ngo.png">
        <div>
          <div class="testimonial-text">“Wella.AI aligns perfectly with our mission to reduce healthcare disparities in underserved regions.”</div>
          <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
          <div class="testimonial-name">John Mensah, MedServe Africa</div>
        </div>
      </div>
      <div class="testimonial-card" style="display: none;">
        <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/commission.png">
        <div>
          <div class="testimonial-text">“We’ve seen a significant improvement in diagnosis speed in our primary healthcare centers.”</div>
          <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
          <div class="testimonial-name">Hon. Aisha Bello, Health Commissioner</div>
        </div>
      </div>
      <div class="dot-container">
        <span class="dot active-dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
      </div>
    </div>
    
    <script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.testimonial-card');
    const dots = document.querySelectorAll('.dot');
    
    function showSlide(index) {
        slides.forEach((s, i) => s.style.display = i === index ? 'flex' : 'none');
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
    
    setInterval(nextSlide, 5000);
    </script>
    """
    
    components.html(testimonials_html, height=420)

    # Footer
    st.markdown('<div class="footer">&copy; 2025 Wella.AI. All rights reserved.</div>', unsafe_allow_html=True)
