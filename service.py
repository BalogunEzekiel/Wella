import streamlit as st
from PIL import Image

def show_service():
    # Page config
    st.set_page_config(page_title="Our Services – Wella.AI", layout="wide")

    # Title Section
    st.markdown("<h2 style='text-align: center; color: #0E4A86;'>Our Smart Healthcare Services</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Empowering healthcare with intelligent solutions – Because Every Diagnosis Matters.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Services Section
    services = [
        {
            "title": "🧠 AI Diagnostic Engine",
            "description": "Instantly analyze symptoms and medical data using advanced AI to provide likely diagnosis suggestions, helping medical professionals make informed decisions even offline.",
            "image": "assets/AI.jpg"
        },
#        {
#            "title": "🩺 Virtual Health Assistant",
#            "description": "Patients can engage with our smart assistant for quick symptom checks, health advice, and connecting with a doctor for more personalized care.",
#            "image": "assets/virtual_assistant.png"
#        },
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

    # Display services
    for idx, service in enumerate(services):
        cols = st.columns([1, 2]) if idx % 2 == 0 else st.columns([2, 1])
        with cols[0 if idx % 2 == 0 else 1]:
            try:
                img = Image.open(service["image"])
                st.image(img, use_column_width=True)
            except:
                st.warning(f"Image not found: {service['image']}")
        with cols[1 if idx % 2 == 0 else 0]:
            st.markdown(f"### {service['title']}")
            st.write(service["description"])
        st.markdown("---")

    # CTA
    st.markdown("### 💡 Ready to transform healthcare in your community?")
    st.markdown("<p style='font-size: 18px;'>Partner with us or integrate Wella.AI into your clinic today. Let’s make intelligent healthcare accessible to all.</p>", unsafe_allow_html=True)
