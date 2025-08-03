'import streamlit as st
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

        with st.form("login_form", clear_on_submit=True):
            username = st.text_input("Email", placeholder="e.g. johndoe@example.com").strip().lower()
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submit = st.form_submit_button("Login")

            if submit:
                # Connect and check DB for user
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("SELECT fullname, email, role, password FROM users WHERE email = ?", (username,))
                result = cur.fetchone()
                cur.close()
                conn.close()

                if result:
                    stored_fullname, stored_email, stored_role, stored_password_hash = result
                    if bcrypt.checkpw(password.encode(), stored_password_hash.encode()):
                        st.session_state.authenticated = True
                        st.session_state.user = {
                            "email": stored_email,
                            "role": stored_role,
                            "fullname": stored_fullname
                        }
                        st.success(f"✅ Login successful as {stored_role}. Redirecting...")
                        st.rerun()
                    else:
                        st.warning("⚠️ Incorrect password. Please try again.")
                elif username in ADMINS and password == ADMIN_PASSWORD:
                    st.session_state.authenticated = True
                    st.session_state.user = {
                        "email": username,
                        "role": "Admin",
                        "fullname": "Admin User"
                    }
                    st.success("✅ Admin login successful. Redirecting...")
                    st.rerun()
                else:
                    st.warning("⚠️ This email has not been registered. Contact Admin to register.")

        st.stop()

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
