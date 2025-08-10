import streamlit as st
from langdetect import detect, LangDetectException
from components import render_header
import streamlit.components.v1 as components
from PIL import Image
import time
import random
import base64
from streamlit_extras.switch_page_button import switch_page

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
    # ===================== Hero Flag ========================
    def image_to_base64(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Convert image
    encoded_img = image_to_base64("assets/illustration.jpg")
    
    # Hero section with red-colored text
    hero_html = f"""
    <div style="
        background-image: url('data:image/png;base64,{encoded_img}');
        background-size: cover;
        background-position: center;
        height: 420px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        text-align: center;
        color: red;
        padding: 20px;
        ">
        <h1><b>Wella.AI Diagnostic Assistant</b></h1>
        <p><b>Revolutionizing healthtech with an AI-Powered solution.</b></p>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)
    
    st.markdown("---")

    # ========== Hero Banner ==========
    st.markdown("""
    <div class="hero">
        <h1><b>Smart Diagnosis Anytime, Anywhere</b></h1>
        <p><b>Empowering rural clinics with AI-powered medical diagnosis – even offline.</b></p>
        <a href="/?page=diagnosis" target="_self">
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # ========== Footer ==========
    st.markdown("""
    <div class="footer">
        Built with ❤️ for smarter, accessible healthcare.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    #=====================================================
        
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
    video_path = "assets/video/toedit.mp4"
    st.video(video_path)

    # Testimonials    
    st.subheader("🗣️ What People Are Saying")

    def image_to_base64(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    testimonial1_img = image_to_base64("assets/image.jpg")
    testimonial2_img = image_to_base64("assets/nurse.png")
    testimonial3_img = image_to_base64("assets/commissioner.jpg")
    testimonial4_img = image_to_base64("assets/john.jpg")
    testimonial5_img = image_to_base64("assets/commission.png")
    testimonial6_img = image_to_base64("assets/commissioner.jpg")

    # Use f-string: escape braces by doubling {{ ... }} everywhere except Python placeholders like {testimonial1_img}
    testimonials_html = f"""
    <style>
    .testimonial-carousel {{
        width: 100%;
        max-width: 1200px;
        margin: auto;
        overflow: hidden;
    }}
    .testimonial-grid {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 20px;
        align-items: stretch;
        width: 100%;
    }}
    .testimonial-card {{
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 20px;
        border-radius: 16px;
        background: linear-gradient(135deg, #e0f7fa, #fce4ec);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        min-height: 260px;
        height: 100%;
    }}
    .testimonial-card img {{
        width: 120px;
        height: 120px;
        object-fit: cover;
        border-radius: 50%;
        margin-right: 20px;
        border: 4px solid #fff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        flex-shrink: 0;
    }}
    .testimonial-text {{
        font-size: 1rem;
        font-style: italic;
        color: #333;
        line-height: 1.4;
    }}
    .testimonial-name {{
        margin-top: 10px;
        font-weight: bold;
        font-size: 1.05rem;
        color: #0077b6;
    }}
    .stars {{
        color: #ffa500;
        margin-bottom: 6px;
        font-size: 1.05rem;
    }}
    .dot-container {{
        text-align: center;
        margin-top: 12px;
    }}
    .dot {{
        height: 12px;
        width: 12px;
        margin: 4px 6px;
        background-color: #bbb;
        border-radius: 50%;
        display: inline-block;
        transition: background-color 0.25s ease;
        cursor: pointer;
    }}
    .active-dot {{
        background-color: #0077b6;
    }}
    .hidden {{
        display: none !important;
    }}
    /* Slightly wider breakpoint so Streamlit iframe won't collapse prematurely */
    @media (max-width: 900px) {{
        .testimonial-grid {{
            grid-template-columns: 1fr;
        }}
        .testimonial-card {{
            flex-direction: column;
            text-align: center;
        }}
        .testimonial-card img {{
            margin-right: 0;
            margin-bottom: 12px;
        }}
    }}
    </style>

    <div class="testimonial-carousel">
      <div id="testimonial-slides">
        <div class="testimonial-grid">
          <div class="testimonial-card">
            <img src="data:image/png;base64,{testimonial1_img}">
            <div>
              <div class="testimonial-text">“Wella.AI is a game-changer for rural healthcare. We diagnose faster and more accurately, even offline.”</div>
              <div class="stars">★★★★★ <span style="font-size: 0.85rem;">5/5</span></div>
              <div class="testimonial-name">Dr. Amina Yusuf</div>
            </div>
          </div>
          <div class="testimonial-card">
            <img src="data:image/png;base64,{testimonial2_img}">
            <div>
              <div class="testimonial-text">“We no longer panic during network outages—Wella.AI is always ready.”</div>
              <div class="stars">★★★★★ <span style="font-size: 0.85rem;">5/5</span></div>
              <div class="testimonial-name">Nurse Michael Todo</div>
            </div>
          </div>
        </div>

        <div class="testimonial-grid hidden">
          <div class="testimonial-card">
            <img src="data:image/png;base64,{testimonial3_img}">
            <div>
              <div class="testimonial-text">“Thanks to Wella.AI, I can now confidently assist in patient triage even without a doctor around.”</div>
              <div class="stars">★★★★★ <span style="font-size: 0.85rem;">5/5</span></div>
              <div class="testimonial-name">Amaka Udo, Community Health Worker</div>
            </div>
          </div>
          <div class="testimonial-card">
            <img src="data:image/png;base64,{testimonial4_img}">
            <div>
              <div class="testimonial-text">“Wella.AI aligns perfectly with our mission to reduce healthcare disparities in underserved regions.”</div>
              <div class="stars">★★★★★ <span style="font-size: 0.85rem;">5/5</span></div>
              <div class="testimonial-name">John Mensah, MedServe Africa</div>
            </div>
          </div>
        </div>

        <div class="testimonial-grid hidden">
          <div class="testimonial-card">
            <img src="data:image/png;base64,{testimonial5_img}">
            <div>
              <div class="testimonial-text">“We’ve seen a significant improvement in diagnosis speed in our primary healthcare centers.”</div>
              <div class="stars">★★★★★ <span style="font-size: 0.85rem;">5/5</span></div>
              <div class="testimonial-name">Hon. Aisha Bello, Health Commissioner</div>
            </div>
          </div>
          <div class="testimonial-card">
            <img src="data:image/png;base64,{testimonial6_img}">
            <div>
              <div class="testimonial-text">“Wella.AI has revolutionized how we handle patients in our village clinic.”</div>
              <div class="stars">★★★★★ <span style="font-size: 0.85rem;">5/5</span></div>
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

    function showSlide(index) {{
        slides.forEach((s, i) => {{
            s.classList.toggle('hidden', i !== index);
        }});
        dots.forEach((d, i) => d.className = i === index ? 'dot active-dot' : 'dot');
    }}

    function nextSlide() {{
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }}

    dots.forEach((dot, index) => {{
        dot.onclick = () => {{
            currentSlide = index;
            showSlide(index);
        }};
    }});

    showSlide(currentSlide);
    setInterval(nextSlide, 6000);
    </script>
    """

    # Suggest a reasonable iframe width to help keep two columns on desktop in Streamlit
    components.html(testimonials_html, height=750, width=700)

    # small footer area
    st.markdown('<div class="footer" style="text-align:center; margin-top:12px;">&copy; 2025 Wella.AI. All rights reserved.</div>', unsafe_allow_html=True)
