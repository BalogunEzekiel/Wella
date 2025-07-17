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
    st.set_page_config(page_title="Wella.AI – Smart Diagnosis", layout="wide", initial_sidebar_state="collapsed")

    # Hide sidebar and Streamlit default elements
    st.markdown("""
    <style>
    [data-testid="stSidebar"], .css-1lcbmhc, .css-ng1t4o, [data-testid="collapsedControl"] {
        display: none !important;
    }

    .hero-wrapper {
        position: relative;
        width: 100%;
        height: 85vh;
        overflow: hidden;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 3rem;
    }

    .hero-slides {
        display: flex;
        width: 400%;
        height: 100%;
        animation: slideX 28s infinite ease-in-out;
    }

    .hero-slides img {
        width: 100vw;
        height: 85vh;
        object-fit: cover;
    }

    @keyframes slideX {
        0%   { transform: translateX(0%); }
        20%  { transform: translateX(0%); }
        25%  { transform: translateX(-100%); }
        45%  { transform: translateX(-100%); }
        50%  { transform: translateX(-200%); }
        70%  { transform: translateX(-200%); }
        75%  { transform: translateX(-300%); }
        95%  { transform: translateX(-300%); }
        100% { transform: translateX(0%); }
    }

    .hero-overlay {
        position: absolute;
        top: 0; left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(to top, rgba(0,0,0,0.6), rgba(0,0,0,0.2));
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: #fff;
        text-align: center;
        padding: 3rem 2rem;
        z-index: 10;
    }

    .hero-overlay h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
    }

    .hero-overlay p {
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 2rem;
        max-width: 700px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.4);
    }

    .launch-button {
        background: linear-gradient(135deg, #00b894, #00cec9);
        padding: 0.85rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        color: white;
        border: none;
        border-radius: 40px;
        cursor: pointer;
        transition: background 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    .launch-button:hover {
        background: linear-gradient(135deg, #009e82, #00bfa5);
    }

    @media (max-width: 768px) {
        .hero-overlay h1 {
            font-size: 2rem;
        }
        .hero-overlay p {
            font-size: 1rem;
        }
        .hero-wrapper {
            height: 70vh;
        }
        .hero-slides img {
            height: 70vh;
        }
    }
    </style>

    <div class="hero-wrapper">
        <div class="hero-slides">
            <img src="assets/wella.jpg" alt="Wella Image 1">
            <img src="assets/illustration.jpg" alt="Wella Image 2">
            <img src="assets/logo.png" alt="Wella Image 3">
            <img src="assets/raspberry.avif" alt="Wella Image 4">
        </div>
        <div class="hero-overlay">
            <h1>Wella.AI – Smart Diagnosis Anytime, Anywhere</h1>
            <p>Empowering rural clinics with AI-powered medical diagnosis – even offline, even on low-resource devices.</p>
            <a href="/?page=login"><button class="launch-button">🚀 Launch Wella.AI</button></a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
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
        st.image("assets/roles.png", use_container_width=True)

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
    
    # Footer
    st.markdown('<div class="footer">&copy; 2025 Wella.AI. All rights reserved.</div>', unsafe_allow_html=True)
