
import streamlit as st
from PIL import Image

def show_service():
    # Page config
    st.set_page_config(page_title="Our Services – Wella.AI", layout="wide")

    # Hide sidebar permanently
    st.markdown("""
        <style>
            /* Hide sidebar and hamburger */
            [data-testid="stSidebar"], [data-testid="stSidebarNav"], .css-h5rgaw, .css-1lcbmhc, .css-6qob1r {
                display: none !important;
            }

            /* Main padding and width */
            .main {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                max-width: 100% !important;
            }

            /* Custom service box style */
            .service-box {
                padding: 20px;
                border-radius: 15px;
                background-color: #f9f9f9;
                transition: all 0.3s ease;
                box-shadow: 0px 0px 8px rgba(0,0,0,0.08);
            }
            .service-box:hover {
                background-color: #e6f0ff;
                transform: scale(1.02);
                box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
            }
            .service-title {
                font-size: 24px;
                font-weight: bold;
                color: #0E4A86;
                margin-bottom: 10px;
            }
            .service-desc {
                font-size: 17px;
                color: #333333;
                line-height: 1.6;
            }

            /* Responsive adjustments for mobile */
            @media only screen and (max-width: 768px) {
                .service-title {
                    font-size: 20px !important;
                }
                .service-desc {
                    font-size: 15px !important;
                }
                .element-container > div > div {
                    flex-direction: column !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h2 style='text-align: center; color: #0E4A86;'>Our Smart Healthcare Services</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Empowering healthcare with intelligent solutions – Because Every Diagnosis Matters.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Services List
    services = [
        {
            "title": "🧠 AI Diagnostic Engine",
            "description": "Instantly analyze symptoms and medical data using advanced AI to provide likely diagnosis suggestions, helping medical professionals make informed decisions even offline.",
            "image": "assets/AI.jpg"
        },
        {
            "title": "📊 Health Analytics Dashboard",
            "description": "Powerful visualizations and health trend analytics to monitor clinic activity and more—all from one intuitive dashboard.",
            "image": "assets/analytics.jpg"
        },
        {
            "title": "📁 Offline Patient Management",
            "description": "Rural clinics and hospitals can register, manage and retrieve patient records without needing constant internet access.",
            "image": "assets/offline.png"
        },
        {
            "title": "👨‍⚕️ Smart Doctor Support",
            "description": "Doctors receive real-time diagnostics, automated recommendation reports and potential health risk alerts, powered by machine learning algorithms.",
            "image": "assets/diagnotics.jpg"
        }
    ]

    # Display each service
    for idx, service in enumerate(services):
        cols = st.columns([1.2, 1.8]) if idx % 2 == 0 else st.columns([1.8, 1.2])
        with cols[0 if idx % 2 == 0 else 1]:
            try:
                img = Image.open(service["image"])
                st.image(img, use_container_width=True)
            except:
                st.warning(f"Image not found: {service['image']}")
        with cols[1 if idx % 2 == 0 else 0]:
            with st.container():
                st.markdown(f"""
                    <div class='service-box'>
                        <div class='service-title'>{service['title']}</div>
                        <div class='service-desc'>{service['description']}</div>
                    </div>
                """, unsafe_allow_html=True)
        st.markdown("")

    # Call-to-Action
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#0E4A86;'>💡 Ready to transform healthcare in your community?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Partner with us or integrate <strong>Wella.AI</strong> into your clinic today. Let’s make intelligent healthcare accessible to all.</p>", unsafe_allow_html=True)
