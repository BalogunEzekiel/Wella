import streamlit as st

def show_contact():
    st.set_page_config(page_title="Contact Us", layout="centered")

    st.markdown("""
        <style>
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
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="contact-header">Contact Us</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-subheader">Don’t hesitate to reach out, our Healthcare Team is here to help 24/7.</div>', unsafe_allow_html=True)

    st.image("./assets/AI_Me.png", caption="24/7 Emergency Support", use_container_width=True)

    st.markdown('<div class="emergency">🚨 24/7 Emergency Support — Call Our Emergency Line: +234-806-2529-172</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown("### Get In Touch With Us")
        st.write("We’re here to assist with your inquiries or general support needs. Fill out the contact form below, and we’ll get back to you ASAP.")

        with st.form("contact_form"):
            full_name = st.text_input("Full Name *", placeholder="Enter your full name")
            email = st.text_input("Email *", placeholder="Enter your Email address")
            phone = st.text_input("Phone Number", placeholder="+234 801 234 5678")
            subject = st.text_input("Subject *", placeholder="Enter your subject matter")
            message = st.text_area("Message", placeholder="Enter your message")

            submitted = st.form_submit_button("Submit")
            
            if submitted:
                if full_name and email and subject and message:
                    st.success("✅ Your message has been received. We’ll respond shortly!")
                else:
                    st.warning("⚠️ Please fill all required fields.")
                    st.rerun()

    st.markdown("### 📞 Contact Info")
    st.write("#### We're here to help. Reach out to us via any of the following channels:")
    
    st.write("- 📱 **Phone:** [+234 806 252 9172](tel:+2348062529172)")
    st.write("- 📧 **Email:** [helpline@wella.ai](mailto:helpline@wella.ai)")
    st.write("- 💬 **Chat with Support Team:** [WhatsApp](https://wa.me/2348062529172)")

    st.markdown("---")

    st.image("assets/AI_Me.png", use_container_width=True)

    st.markdown("### 🌐 Stay Connected")

    social_icons = """
    <style>
    .social-icons {
        display: flex;
        gap: 25px;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 10px;
    }
    .social-icons a img {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .social-icons a:hover img {
        transform: scale(1.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    </style>
    
    <div class="social-icons">
        <a href="https://www.facebook.com/share/16pgExaeBr/" target="_blank">
            <img src="https://img.icons8.com/color/48/facebook.png" alt="Facebook"/>
        </a>
    
        <a href="https://x.com/EzekielOBalogun?t=nmlZqljflqWtdyR0B1MuaA&s=09" target="_blank">
            <img src="https://img.icons8.com/color/48/twitter--v1.png" alt="Twitter/X"/>
        </a>
    
        <a href="https://www.linkedin.com/in/ezekiel-balogun-39a14438?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
            <img src="https://img.icons8.com/color/48/linkedin.png" alt="LinkedIn"/>
        </a>
    
        <a href="https://github.com/BalogunEzekiel" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/github.png" alt="GitHub"/>
        </a>
    
        <a href="https://datatech.hashnode.dev" target="_blank">
            <img src="https://img.icons8.com/nolan/48/domain.png" alt="Blog"/>
        </a>
    </div>
    """
    
    st.markdown(social_icons, unsafe_allow_html=True)
