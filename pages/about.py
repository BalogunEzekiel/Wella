import streamlit as st
import os
import base64

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
    st.markdown("## 📸 Gallery", unsafe_allow_html=True)

    image_info = [
        ("assets/AI_Me.png", "AI Avatar"),
        ("assets/homepage.jpg", "Homepage"),
        ("assets/admin dashboard.jpg", "Admin Dashboard"),
        ("assets/nurse dashboard.jpg", "Nurse Dashboard"),
        ("assets/doctor dashboard.jpg", "Doctor Dashboard"),
        ("assets/diagnosis.jpg", "Diagnosis Report"),
        ("assets/treatment.jpg", "Treatment Report")
    ]
    
    def get_base64_img(path):
        if not os.path.exists(path):
            return ""
        with open(path, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()
            ext = path.split('.')[-1]
            return f"data:image/{ext};base64,{encoded}"
    
    # HTML Template
    gallery_html = """
    <style>
    .gallery-container {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
    }
    .gallery-img {
        width: 200px;
        border-radius: 8px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .gallery-img:hover {
        transform: scale(1.05);
    }
    .lightbox-modal {
        display: none;
        position: fixed;
        z-index: 10000;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0,0,0,0.95);
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .lightbox-modal img {
        max-width: 90vw;
        max-height: 90vh;
        border-radius: 8px;
        transition: transform 0.2s ease-in-out;
    }
    .lightbox-modal .caption {
        color: white;
        margin-top: 15px;
        font-size: 18px;
    }
    .close-btn, .nav-btn {
        position: absolute;
        font-size: 40px;
        color: white;
        cursor: pointer;
        z-index: 10001;
    }
    .close-btn { top: 25px; right: 30px; }
    .nav-btn.prev { left: 30px; top: 50%; transform: translateY(-50%); }
    .nav-btn.next { right: 30px; top: 50%; transform: translateY(-50%); }
    </style>
    
    <div class="gallery-container">
    """
    
    # Embed images in gallery
    for idx, (img_path, caption) in enumerate(image_info):
        base64_img = get_base64_img(img_path)
        if base64_img:
            gallery_html += f"""
            <img src="{base64_img}" class="gallery-img" onclick="openLightbox({idx})">
            """
    
    gallery_html += """
    </div>
    
    <div id="lightboxModal" class="lightbox-modal" onwheel="zoomImage(event)">
        <span class="close-btn" onclick="closeLightbox()">&times;</span>
        <span class="nav-btn prev" onclick="navigate(-1)">&#10094;</span>
        <span class="nav-btn next" onclick="navigate(1)">&#10095;</span>
        <img id="lightboxImage" src="">
        <div class="caption" id="lightboxCaption"></div>
    </div>
    
    <script>
    const images = [];
    const captions = [];
    """
    
    # Pass image data into JavaScript arrays
    for img_path, caption in image_info:
        base64_img = get_base64_img(img_path)
        if base64_img:
            safe_caption = caption.replace("'", "\\'")
            gallery_html += f"images.push('{base64_img}'); captions.push('{safe_caption}');\n"
    
    gallery_html += """
    let currentIndex = 0;
    let zoomScale = 1;
    
    function openLightbox(index) {
        currentIndex = index;
        const modal = document.getElementById('lightboxModal');
        const modalImg = document.getElementById('lightboxImage');
        const modalCaption = document.getElementById('lightboxCaption');
        modal.style.display = 'flex';
        modalImg.src = images[index];
        modalCaption.textContent = captions[index];
        zoomScale = 1;
        modalImg.style.transform = `scale(${zoomScale})`;
    }
    
    function closeLightbox() {
        document.getElementById('lightboxModal').style.display = 'none';
    }
    
    function navigate(direction) {
        currentIndex = (currentIndex + direction + images.length) % images.length;
        const modalImg = document.getElementById('lightboxImage');
        const modalCaption = document.getElementById('lightboxCaption');
        modalImg.src = images[currentIndex];
        modalCaption.textContent = captions[currentIndex];
        zoomScale = 1;
        modalImg.style.transform = `scale(${zoomScale})`;
    }
    
    function zoomImage(event) {
        event.preventDefault();
        const modalImg = document.getElementById('lightboxImage');
        if (event.deltaY < 0) {
            zoomScale += 0.1;
        } else {
            zoomScale = Math.max(0.5, zoomScale - 0.1);
        }
        modalImg.style.transform = `scale(${zoomScale})`;
    }
    
    // Keyboard navigation
    document.addEventListener('keydown', function(event) {
        const modal = document.getElementById('lightboxModal');
        if (modal.style.display === 'flex') {
            if (event.key === 'ArrowRight') navigate(1);
            else if (event.key === 'ArrowLeft') navigate(-1);
            else if (event.key === 'Escape') closeLightbox();
        }
    });
    </script>
    """
    
    # Render in Streamlit
    st.components.v1.html(gallery_html, height=800)
###########
    # --- CALL TO ACTION ---
    st.markdown("### Join Us in Transforming Healthcare", unsafe_allow_html=True)
    
    st.markdown("""
    We’re on a mission to revolutionize healthcare with AI-powered solutions.  
    Whether you're a hospital, clinic, healthtech innovator, or investor — **let’s partner** to make healthcare smarter, faster, and more accessible.
    
    _We welcome collaborations, pilot programs and strategic partnerships._
    """, unsafe_allow_html=True)
