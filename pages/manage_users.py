import streamlit as st
from utils.auth import require_login, check_authentication, enforce_role
from utils.db import get_connection
import bcrypt

# Protect the page
require_login()
user = check_authentication()
enforce_role(user["role"], allowed_roles=["Admin"])

st.title("👥 User Management (Admin Only)")

# Form to create a new user
with st.form("create_user_form"):
    email = st.text_input("User Email").strip().lower()
    role = st.selectbox("Select Role", ["Doctor", "Nurse"])
    password = st.text_input("Set Password", type="password")
    submit = st.form_submit_button("Create User")

    if submit:
        if not email or not password:
            st.error("Email and Password are required.")
        else:
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO users (email, role, password)
                VALUES (%s, %s, %s)
                ON CONFLICT (email) DO UPDATE SET role = EXCLUDED.role, password = EXCLUDED.password
            """, (email, role, hashed_password))
            conn.commit()
            st.success(f"✅ {role} user '{email}' created successfully.")
