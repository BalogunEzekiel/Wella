import streamlit as st
from PIL import Image
from streamlit_card import card

def show_service():
    st.set_page_config(page_title="Our Services – Wella.AI", layout="wide")

    # Title
    st.markdown("<h2 style='text-align: center; color: #0E4A86;'>Our Smart Healthcare Services</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Empowering healthcare with intelligent solutions – Because Every Diagnosis Matters.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Services
    services = [
        {
            "title": "AI Diagnostic Engine",
            "description": "Instantly analyze symptoms and medical data using advanced AI to provide likely diagnosis suggestions, helping medical professionals make informed decisions even offline.",
            "image": "assets/AI.jpg",
            "icon": "fas fa-brain"
        },
        {
            "title": "Health Analytics Dashboard",
            "description": "Powerful visualizations and health trend analytics to monitor clinic activity and more—all from one intuitive dashboard.",
            "image": "assets/analytics.jpg",
            "icon": "fas fa-chart-line"
        },
        {
            "title": "Offline Patient Management",
            "description": "Rural clinics and hospitals can register, manage and retrieve patient records without needing constant internet access.",
            "image": "assets/offline.png",
            "icon": "fas fa-file-medical"
        },
        {
            "title": "Smart Doctor Support",
            "description": "Doctors receive real-time diagnostics, automated recommendation reports and potential health risk alerts, powered by machine learning algorithms.",
            "image": "assets/diagnotics.jpg",
            "icon": "fas fa-user-md"
        }
    ]

    for idx, service in enumerate(services):
        cols = st.columns([1, 2]) if idx % 2 == 0 else st.columns([2, 1])
        with cols[0 if idx % 2 == 0 else 1]:
            try:
                st.image(service["image"], use_container_width=True)
            except:
                st.warning(f"Image not found: {service['image']}")
        with cols[1 if idx % 2 == 0 else 0]:
            st.markdown(f"<h4><i class='{service['icon']}'></i> {service['title']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:16px'>{service['description']}</p>", unsafe_allow_html=True)

        st.markdown("---")

    # CTA (Contact Us removed)
    st.markdown("### 💡 Ready to transform healthcare in your community?")
    st.markdown("<p style='font-size: 18px;'>Partner with us or integrate Wella.AI into your clinic today. Let’s make intelligent healthcare accessible to all.</p>", unsafe_allow_html=True)
