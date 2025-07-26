
import streamlit as st
import time
from pytz import timezone

def show_contact():
    st.set_page_config(page_title="Contact Us", layout="centered")

    # Responsive and sidebar removal styling
    st.markdown("""
        <style>
        /* Hide sidebar permanently */
        [data-testid="stSidebar"] {
            display: none;
        }

        /* Make layout mobile-friendly */
        [data-testid="stAppViewContainer"] > .main {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .contact-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #064635;
            text-align: center;
        }
        .contact-subheader {
            font-size: 1.2rem;
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .contact-section {
            background-color: #f6f6f6;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .emergency {
            background-color: #fcdede;
            padding: 1rem;
            border-left: 6px solid #c1121f;
            font-size: 1rem;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .form-control {
            padding: 8px;
            font-size: 1rem;
        }

        @media screen and (max-width: 768px) {
            h1, h2, h3, h4 {
                font-size: 1.2rem !important;
            }
            p, li, .contact-subheader, .emergency, .stTextInput>div>input, .stTextArea>div>textarea {
                font-size: 0.95rem !important;
                line-height: 1.5;
            }
            .block-container {
                padding: 1rem 0.5rem !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="contact-header">Contact Us</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-subheader">Don’t hesitate to reach out, our Healthcare Team is here to help 24/7.</div>', unsafe_allow_html=True)

    st.image("./assets/AI_Me.png", caption="24/7 Emergency Support", use_container_width=True)

    st.markdown('<div class="emergency">🚨 24/7 Emergency Support — Call Our Emergency Line: +234-806-2529-172</div>', unsafe_allow_html=True)

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    with st.container():
        st.markdown("### Get In Touch With Us")
        st.write("We’re here to assist with your inquiries or general support needs. Fill out the contact form below and we’ll get back to you ASAP.")

        with st.form("contact_form", clear_on_submit=True):
            full_name = st.text_input("Full Name *", placeholder="Enter your full name")
            email = st.text_input("Email *", placeholder="Enter your Email address")
            phone = st.text_input("Phone Number", placeholder="+234 801 234 5678")
            subject = st.text_input("Subject *", placeholder="Enter your subject matter")
            message = st.text_area("Message", placeholder="Enter your message")

            submitted = st.form_submit_button("Submit")

            if submitted:
                if full_name and email and subject and message:
                    st.session_state.submitted = True
                else:
                    st.warning("⚠️ Please fill all required fields.")
                    st.stop()

    if st.session_state.submitted:
        st.success("✅ Your message has been received. We’ll respond shortly!")
        time.sleep(1.5)
        st.session_state.submitted = False
        st.rerun()

    st.markdown("### 📞 Contact Info")
    st.write("###### We're here to help. Reach out to us via any of the following channels:")

    st.write("- 📱 **Phone:** [+234 806 252 9172](tel:+2348062529172)")
    st.write("- 📧 **Email:** [helpline@wella.ai](mailto:helpline@wella.ai)")
    st.write("- 💬 **Chat with Support Team:** [WhatsApp](https://wa.me/2348062529172)")

    st.markdown("---")

    st.image("assets/AI_Me.png", use_container_width=True)

    st.markdown("---")

    st.markdown("### 🌐 Stay Connected", unsafe_allow_html=True)

    html_code = """
    <style>
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 10px;
            flex-wrap: wrap;
        }
        .social-icons a img {
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border-radius: 8px;
        }
        .social-icons a:hover img {
            transform: scale(1.1);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
    </style>

    <div class="social-icons">
        <a href="https://www.facebook.com/share/16pgExaeBr/" target="_blank">
            <img src="https://img.icons8.com/color/48/facebook.png" alt="Facebook"/>
        </a>
        <a href="https://x.com/EzekielOBalogun?t=nmlZqljflqWtdyR0B1MuaA&s=09" target="_blank">
            <img src="https://img.icons8.com/color/48/twitter--v1.png" alt="Twitter/X"/>
        </a>
        <a href="https://www.linkedin.com/in/ezekiel-balogun-39a14438" target="_blank">
            <img src="https://img.icons8.com/color/48/linkedin.png" alt="LinkedIn"/>
#        </a>
#        <a href="https://github.com/BalogunEzekiel" target="_blank">
#            <img src="https://img.icons8.com/ios-filled/50/000000/github.png" alt="GitHub"/>
        </a>
        <a href="https://datatech.hashnode.dev" target="_blank">
            <img src="https://img.icons8.com/nolan/48/domain.png" alt="Blog"/>
        </a>
    </div>
    """

    st.markdown(html_code, unsafe_allow_html=True)
