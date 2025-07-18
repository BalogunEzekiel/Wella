import streamlit as st

def contact_page():
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

    st.image("assets/woman_using_phone.jpg", caption="24/7 Emergency Support", use_column_width=True)

    st.markdown('<div class="emergency">🚨 24/7 Emergency Support — Call Our Emergency Line: +234-800-9000-000</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown("### Get In Touch With Us")
        st.write("We’re here to assist with your healthcare inquiries, appointment bookings, or general support needs. Fill out the contact form below, and we’ll get back to you ASAP.")

        with st.form("contact_form"):
            full_name = st.text_input("Full Name *", placeholder="Enter your full name")
            email = st.text_input("Email *", placeholder="Enter your Email address")
            phone = st.text_input("Phone Number", placeholder="+234...")
            subject = st.text_input("Subject *", placeholder="Enter your subject matter")
            message = st.text_area("Message", placeholder="Enter your message")

            submitted = st.form_submit_button("Submit")

            if submitted:
                if full_name and email and subject and message:
                    st.success("✅ Your message has been received. We’ll respond shortly!")
                else:
                    st.warning("⚠️ Please fill all required fields.")

    st.markdown("### 📞 Contact Info")
    st.write("- **Phone:** (+234) 8060593391")
    st.write("- **Email:** Healthpointer@gmail.com")
    st.markdown("Need quick answers? [Visit our FAQ Section](#)")

    st.markdown("---")

    st.markdown("### 📲 Stay Connected")
    st.markdown("""
    - 📘 Facebook: [@HealthPointer](#)
    - 📷 Instagram: [@HealthPointer](#)
    - 🐦 Twitter/X: [@HealthPointer](#)
    - 🔗 LinkedIn: [@HealthPointer](#)
    """)

    st.image("assets/illustration_person_computer.png", use_column_width=True)

def show_contact():
    contact_page()

# Call the function to render the page
if __name__ == "__main__":
    contact_page()
