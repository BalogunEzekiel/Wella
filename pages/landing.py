import streamlit as st
from langdetect import detect, LangDetectException
from components import render_header
import streamlit.components.v1 as components
from PIL import Image
import time

def detect_language():
    try:
        lang = detect(st.session_state.get("text_input", "Wella.AI empowers healthcare anywhere."))
        return lang
    except (LangDetectException, Exception):
        return "en"

def landing_page():
    st.set_page_config(page_title="Wella.AI – Smart Diagnosis", layout="wide", initial_sidebar_state="collapsed")

    # Force sidebar to be closed
    hide_sidebar = """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
            [data-testid="collapsedControl"] {
                display: none;
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
            text-decoration: none;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: gray;
            margin-top: 3rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # ========== Hero Banner ==========
    st.markdown("""
    <div class="hero">
        <h1><b>Wella.AI – Smart Diagnosis Anytime, Anywhere</b></h1>
        <p><b>Empowering rural clinics with AI-powered medical diagnosis – even offline.</b></p>
        <a href="/?page=diagnosis" target="_self">
            <button class="launch-button">🚀 Launch Wella.AI</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # ========== Auto-Rotating Images ==========
    image_files = ["assets/AI_Me.png", "assets/AI_Me.png", "assets/AI_Me.png"]
    images = [Image.open(img) for img in image_files]
    caption = ["AI-powered Health", "Wella.AI in Action", "Smart Medical Future"]

    for i in range(len(images)):
        st.image(images[i], caption=caption[i], use_container_width=True)
        time.sleep(1.5)
        st.empty()

    # ===================== Hero Flag ========================
    # ✅ Hero images list
    hero_images = [
        "assets/Image_2.png",
        "assets/AI_Me.png",
        "assets/analytics.jpg",
        "assets/logo.png",
        "assets/raspberry.avif",
        "assets/wella.jpg"
    ]

    # ✅ Pick a random image at each page load (refresh)
    selected_image = random.choice(hero_images)

    # ✅ Render hero and full story + CTA section
    st.markdown(f"""
    <style>
    .hero-container {{
        position: relative;
        width: 100%;
        height: 420px;
        background-image: url('{selected_image}');
        background-size: cover;
        background-position: center;
        border-radius: 10px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 3rem;
    }}
    .hero-overlay {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 40px;
        color: white;
        text-align: center;
        border-radius: 10px;
        max-width: 80%;
    }}
    .hero-buttons a {{
        margin: 5px 10px;
        padding: 10px 20px;
        background-color: #4B8BBE;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
    }}
    .hero-buttons a:hover {{
        background-color: #366fa1;
    }}
    .story-container {{
        display: flex;
        gap: 20px;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-top: 2rem;
    }}
    .story-box {{
        flex: 1;
        min-width: 300px;
        background-color: #f5f9ff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }}
    .cta-box {{
        background-color: #e0f7ea;
        border-radius: 10px;
        padding: 30px;
        margin-top: 3rem;
        text-align: center;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }}
    </style>

    <div class="hero-container">
      <div class="hero-overlay">
        <h1>Mentorship that Moves Mountains</h1>
        <p>From non-tech to tech. From doubt to destiny. MentorLink is where stories begin.</p>
        <div class="hero-buttons">
            <a href="https://mentorlink.streamlit.app/" target="_blank">🚀 Join as a Fellow</a>
            <a href="https://mentorlink.streamlit.app/" target="_blank">✨ Become a Mentor</a>
        </div>
      </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)
    
    # ========== Footer ==========
    st.markdown("""
    <div class="footer">
        Built with ❤️ for smarter, accessible healthcare.
    </div>
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
        st.image("assets/Image_2.png", use_container_width=True)

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
            <img src="assets/offline.png" style="width: 100%; border-radius: 10px;">
#            <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/offline.png">
            <div>
              <div class="testimonial-text">“Thanks to Wella.AI, I can now confidently assist in patient triage even without a doctor around.”</div>
              <div class="stars">★★★★★ <span style="font-size: 0.9rem;">5/5</span></div>
              <div class="testimonial-name">Amaka Udo, Community Health Worker</div>
            </div>
          </div>
          <div class="testimonial-card">
            <img src="assets/ngo.png" style="width: 100%; border-radius: 10px;">
#            <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/ngo.png">
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
            <img src="assets/commission.png" style="width: 100%; border-radius: 10px;">
#            <img src="https://raw.githubusercontent.com/yourusername/wellaai-assets/main/assets/commission.png">
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
