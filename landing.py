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
    st.set_page_config(page_title="Wella.AI", layout="wide")

    st.markdown("""
    <style>
    .hero-section {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: stretch;
        margin-top: 6rem;
        padding: 2rem;
        background: linear-gradient(to right, #f0f8ff, #ffffff);
    }

    .hero-left, .hero-carousel {
        flex: 1 1 48%;
        min-height: 420px;
        position: relative;
        margin: 1rem;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }

    .hero-left {
        display: flex;
        flex-direction: column;
        justify-content: center;
        background: url('assets/wella.jpg');
        background-size: cover;
        background-position: center;
        padding: 2rem;
        color: #fff;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.7);
    }

    .hero-left h1 {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }

    .hero-left p {
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
    }

    .launch-button {
        background-color: #ff5722;
        border: none;
        color: white;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .launch-button:hover {
        background-color: #e64a19;
    }

    .hero-carousel-slide {
        display: none;
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background-size: cover;
        background-position: center;
        z-index: 0;
        opacity: 0;
        transition: opacity 1s ease-in-out;
    }

    .hero-carousel-slide.active {
        display: block;
        z-index: 1;
        opacity: 1;
    }

    .hero-overlay {
        position: absolute;
        bottom: 0;
        background: rgba(0,0,0,0.5);
        color: white;
        width: 100%;
        padding: 1.5rem;
        text-align: center;
    }

    .hero-overlay h1 {
        margin-bottom: 0.5rem;
        font-size: 1.6rem;
    }

    .hero-overlay p {
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }

    @keyframes fadein {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @media (max-width: 768px) {
        .hero-left, .hero-carousel {
            flex: 1 1 100%;
        }

        .hero-left h1 {
            font-size: 2rem;
        }

        .hero-left p,
        .hero-overlay p {
            font-size: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Layout with Hero Flag and Carousel
    st.markdown("""
    <div class="hero-section">
        <div class="hero-left">
            <h1>Wella.AI – Smart Diagnosis Anytime, Anywhere</h1>
            <p>Empowering rural clinics with AI-powered medical diagnosis – even offline.</p>
            <a href="/?page=login" target="_self">
                <button class="launch-button">🚀 Launch Wella.AI</button>
            </a>
        </div>

        <div class="hero-carousel">
            <div class="hero-carousel-slide active" style="background-image: url('assets/wella.jpg');">
                <div class="hero-overlay">
                    <h1>Smart & Reliable</h1>
                    <p>Seamless AI diagnosis in seconds.</p>
                    <a href="/?page=login"><button class="launch-button">Get Started</button></a>
                </div>
            </div>
            <div class="hero-carousel-slide" style="background-image: url('assets/illustration.jpg');">
                <div class="hero-overlay">
                    <h1>Rural-Ready</h1>
                    <p>Works perfectly with no internet.</p>
                    <a href="/?page=login"><button class="launch-button">Try Offline</button></a>
                </div>
            </div>
            <div class="hero-carousel-slide" style="background-image: url('assets/logo.png');">
                <div class="hero-overlay">
                    <h1>Lightweight & Secure</h1>
                    <p>Optimized for Raspberry Pi and edge devices.</p>
                    <a href="/?page=login"><button class="launch-button">Learn More</button></a>
                </div>
            </div>
            <div class="hero-carousel-slide" style="background-image: url('assets/raspberry.avif');">
                <div class="hero-overlay">
                    <h1>Low-Cost Innovation</h1>
                    <p>Access care without infrastructure barriers.</p>
                    <a href="/?page=login"><button class="launch-button">Explore Now</button></a>
                </div>
            </div>
        </div>
    </div>

    <script>
        let slideIndex = 0;
        const slides = document.getElementsByClassName("hero-carousel-slide");
        function showNextSlide() {
            for (let i = 0; i < slides.length; i++) {
                slides[i].classList.remove("active");
            }
            slideIndex = (slideIndex + 1) % slides.length;
            slides[slideIndex].classList.add("active");
        }
        setInterval(showNextSlide, 5000);
    </script>
    """, unsafe_allow_html=True)
        
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
