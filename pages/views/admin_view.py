# pages/views/admin_view.py
import streamlit as st
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
def show_admin_dashboard():
    st.subheader("👤 Admin Dashboard")
    conn = sqlite3.connect("wella.db")
    cur = conn.cursor()

    st.markdown("### Create New User")
    with st.form("add_user", clear_on_submit=True):
        fullname = st.text_input("Full Name", placeholder="e.g., Janet Grace")
        email = st.text_input("Email", placeholder="e.g., janet.grace@wella.ai")
        role = st.selectbox("Role", ["user"])  # Admins must be created through code
        submit = st.form_submit_button("Create User")

        if submit:
            default_password = os.getenv("USER_DEFAULT_PASSWORD", "Doctor@123")
            cur.execute(
                "INSERT INTO users (email, password, role, fullname, must_change_password) VALUES (?, ?, ?, ?, 1)",
                (email, default_password, role, fullname)
            )
            conn.commit()
            st.success(f"User {fullname} created with default password.")

    st.markdown("### All Users")
    cur.execute("SELECT id, fullname, email, role FROM users")
    users = cur.fetchall()
    for user in users:
        st.text(f"{user[0]}. {user[1]} - {user[2]} ({user[3]})")

    conn.close()


update
