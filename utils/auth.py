import streamlit as st
import os
import bcrypt
from dotenv import load_dotenv
from utils.db import get_connection

# Load environment variables from .env
load_dotenv()

ADMINS = os.getenv("ADMINS", "").lower().split(",")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

def require_login():
    if not st.session_state.get("authenticated", False):
        st.warning("🔒 Please login to access the diagnosis page.")

        with st.form("login_form"):
            username = st.text_input("Email").strip().lower()
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")

            if submit:
                # Check DB for user
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("SELECT email, role, password FROM users WHERE email = %s", (username,))
                result = cur.fetchone()
                cur.close()
                conn.close()

                if result and bcrypt.checkpw(password.encode(), result[2].encode()):
                    st.session_state.authenticated = True
                    st.session_state.user = {"email": result[0], "role": result[1]}
                    st.success(f"✅ Login successful as {result[1]}. Redirecting...")
                    st.rerun()

                # Optional fallback for .env Admins
                elif username in ADMINS and password == ADMIN_PASSWORD:
                    st.session_state.authenticated = True
                    st.session_state.user = {"email": username, "role": "Admin"}
                    st.success("✅ Admin login successful. Redirecting...")
                    st.rerun()

                else:
                    st.error("❌ Invalid credentials")

        st.stop()  # Prevent further page rendering if not logged in

def check_authentication():
    return st.session_state.get("user")

def enforce_role(role, allowed_roles):
    if role not in allowed_roles:
        st.error("🚫 Access denied: Insufficient role.")
        st.stop()

def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.success("🔒 Logged out successfully.")
    st.rerun()
