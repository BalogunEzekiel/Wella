import streamlit as st
import pandas as pd
import os
import socket
from dotenv import load_dotenv
from utils.db import get_connection
from utils.auth import logout
from utils.sync_utils import sync_to_supabase
import bcrypt
from pytz import timezone
import time

load_dotenv()

def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        return False

def show_user_creation_form():
    st.markdown("### 👤 Create New User")
    conn = get_connection()
    cur = conn.cursor()

    with st.form("add_user", clear_on_submit=True):
        fullname = st.text_input("Full Name", placeholder="e.g Joe John")
        email = st.text_input("Email", placeholder="e.g., j_john@example.com")
        role = st.selectbox("Role", ["Select Role", "Doctor", "Nurse"])
        submit = st.form_submit_button("Create User")

        if submit:
            if role == "Select Role":
                st.warning("⚠️ Please select a valid role before submitting.")
            else:
                try:
                    default_password = os.getenv("DEFAULT_USER_PASSWORD", "DEFAULT_USER_PASSWORD")
                    hashed_pw = bcrypt.hashpw(default_password.encode(), bcrypt.gensalt()).decode()

                    cur.execute("""
                        INSERT INTO users (fullname, email, password, role, force_password_change)
                        VALUES (?, ?, ?, ?, 1)
                    """, (fullname, email, hashed_pw, role))

                    conn.commit()
                    st.success(f"✅ User **{fullname}** created as **{role}** successfully.")
                    time.sleep(1)
                    st.rerun()
                except Exception as err:
                    st.error(f"❌ Failed to create user: {err}")
    conn.close()
    
def show_users_table():
    st.markdown("### 📋 All Users")
    try:
        conn = get_connection()
        df = pd.read_sql_query("SELECT id, fullname, email, role FROM users", conn)
        st.dataframe(df)
        conn.close()
    except Exception as e:
        st.error(f"❌ Could not fetch users: {e}")

def show_patient_records():
    st.subheader("📊 Patient Records")
    try:
        conn = get_connection()
        df = pd.read_sql_query("SELECT * FROM patients ORDER BY created_at DESC", conn)
        conn.close()

        with st.form("filter_form", clear_on_submit=True):
            name_filter = st.text_input("🔍 Search by Patient Name", placeholder="Enter patient name")
            date_filter = st.date_input("📅 Filter by Date", [])
            submit_filter = st.form_submit_button("Apply Filter")

        if submit_filter:
            if name_filter:
                df = df[df['name'].str.contains(name_filter, case=False)]
            if date_filter:
                df['created_at'] = pd.to_datetime(df['created_at'])
                df = df[df['created_at'].dt.date == date_filter]

        st.dataframe(df)

    except Exception as e:
        st.error(f"❌ Could not load patient records: {e}")



def show_admin_dashboard():
    st.title("🛠️ Admin Dashboard")

    show_patient_records()
    show_user_creation_form()
    show_users_table()

    if st.button("🔄 Sync to Supabase"):
        status = sync_to_supabase()
        st.success(status)
        st.rerun()
