import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ADMINS = os.getenv("ADMINS", "").lower().split(",")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
DEFAULT_PASSWORDS = {
    "Doctor": os.getenv("DEFAULT_PASSWORD_DOCTOR"),
    "Nurse": os.getenv("DEFAULT_PASSWORD_NURSE")
}

def require_login():
    if not st.session_state.get("authenticated", False):
        st.warning("🔒 Please login to access the diagnosis page.")

        # Declare placeholders outside the form
        login_placeholder = st.empty()

        with login_placeholder.form("login_form"):
            username = st.text_input("Email", key="login_email").strip().lower()
            password = st.text_input("Password", type="password", key="login_password")
            submit = st.form_submit_button("Login")

            if submit:
                # Admin login
                if username in ADMINS and password == ADMIN_PASSWORD:
                    st.session_state.authenticated = True
                    st.session_state.user = {"email": username, "role": "Admin"}
                    st.success("✅ Login successful. Redirecting...")
                    st.rerun()

                # Doctor/Nurse login
                elif password in DEFAULT_PASSWORDS.values():
                    role = [k for k, v in DEFAULT_PASSWORDS.items() if v == password][0]
                    st.session_state.authenticated = True
                    st.session_state.user = {"email": username, "role": role}
                    st.success(f"✅ {role} login successful. Redirecting...")
                    st.rerun()

                else:
                    st.error("❌ Invalid credentials")

        # Block rendering anything after this
        st.stop()

def check_authentication():
    return st.session_state.get("user")

def enforce_role(role, allowed_roles):
    if role not in allowed_roles:
        st.error("🚫 Access denied: Insufficient role.")
        st.stop()
