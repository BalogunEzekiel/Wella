import streamlit as st
import os
from dotenv import load_dotenv

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
        
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")

        if submit:
            if username == "admin" and password == "1234":
                st.session_state.authenticated = True
                st.success("✅ Login successful. Redirecting...")
                st.rerun()  # This replaces deprecated `st.experimental_rerun()`
            else:
                st.error("❌ Invalid credentials")

        st.stop()  # Stop rendering anything else if not logged in

def check_authentication():
    return {"role": "Admin"} if st.session_state.get("authenticated") else None

def enforce_role(role, allowed_roles):
    if role not in allowed_roles:
        st.error("🚫 Access denied: Insufficient role.")
        st.stop()
