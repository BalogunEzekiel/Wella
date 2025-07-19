import streamlit as st
from PIL import Image

def show_service():
    # Page config
    st.set_page_config(page_title="Our Services – Wella.AI", layout="wide")

    # Title Section
    st.markdown("<h2 style='text-align: center; color: #0E4A86;'>Our Smart Healthcare Services</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Empowering health with intelligent solutions – Because Every Diagnosis Matters.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Services Section
    services = [
        {
            "title": "🧠 AI Diagnostic Engine",
            "description": "Instantly analyze symptoms and medical data using advanced AI to provide likely diagnosis suggestions, helping medical professionals make informed decisions even offline.",
            "image": "assets/ai_diagnosis.png"
        },
        {
            "title": "🩺 Virtual Health Assistant",
            "description": "Patients can engage with our smart assistant for quick symptom checks, health advice, and connecting with a doctor for more personalized care.",
            "image": "assets/virtual_assistant.png"
        },
        {
            "title": "📊 Health Analytics Dashboard",
            "description": "Powerful visualizations and health trend analytics to monitor patient records, clinic activity, and more—all from one intuitive dashboard.",
            "image": "assets/analytics_dashboard.png"
        },
        {
            "title": "📁 Offline Patient Management",
            "description": "Rural clinics and hospitals can register, manage, and retrieve patient records without needing constant internet access.",
            "image": "assets/offline_records.png"
        },
        {
            "title": "👨‍⚕️ Smart Doctor Support",
            "description": "Doctors receive real-time suggestions, automated reports, and alerts for possible health risks, powered by machine learning algorithms.",
            "image": "assets/doctor_support.png"
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
#    if st.button("📞 Contact Us Now"):
#        selected = "Contact"

import contact  # or: from contact import show_contact

    if st.button("📞 Contact Us Now"):
        contact.show_contact()
        
    #        elif st.session_state.page == "contact":
    #    elif selected == "Contact":
    #        contact.show_contact()
