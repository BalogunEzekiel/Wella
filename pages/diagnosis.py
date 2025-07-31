# app/pages/diagnosis.py
import streamlit as st
import sys, os
from dotenv import load_dotenv
from utils.auth import logout, require_login, check_authentication, enforce_role
from utils.sync_utils import sync_to_supabase
from pages.views.admin_view import show_admin_dashboard
from pages.views.doctor_view import show_doctor_dashboard
from pages.views.nurse_view import show_nurse_dashboard
import sqlite3

# Load environment variables
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def show_diagnosis():
    require_login()
    user = check_authentication()
    if not user:
        st.warning("🔒 Please login to access the diagnosis page.")
        return

    role = user.get("role")
    enforce_role(role, allowed_roles=["Nurse", "Admin", "Doctor"])

    st.title("🩺 Wella.AI Diagnosis Page")
    st.markdown(f"Welcome, **{user.get('email', 'User')}**")
    st.markdown(f"Welcome, **{user.get('name', 'User')}**")

    ############################################################################################

    # Connect to the database
    conn = sqlite3.connect("wella.db")
    cursor = conn.cursor()
    
    # Example: get user_id from session state or login system
    user_id = st.session_state.get("user_id", None)
    
    # Fetch user full name from the users table
    if user_id:
        cursor.execute("SELECT name FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            name = result[0]
        else:
            name = "User"
    else:
        name = "User"
    
    # Display welcome message
    st.markdown(f"Welcome, **{name}**")

    #############################################################################################
    # Logout Button
    if st.sidebar.button("🚪 Logout"):
        logout()
        st.session_state["page"] = "Home"
        st.session_state["selected_option"] = "Home"
        st.rerun()

    st.sidebar.image("assets/logo.png", width=100)
    st.sidebar.markdown("Your Offline Health Companion")
    st.sidebar.markdown(f"👤 Logged in as: {user['email']} ({role})")

    st.markdown("### 🧬 Diagnostic Assistant for Primary Healthcare")
    st.markdown("***Helping rural clinics make informed medical decisions — even offline.***")

    # Role-based view
    if role == "Nurse":
        show_nurse_dashboard(user)
    elif role == "Doctor":
        show_doctor_dashboard()
    elif role == "Admin":
        show_admin_dashboard()

    # Sync Status
    if is_connected():
        st.sidebar.success("🌐 Online – Auto Sync Enabled")
        sync_msg = sync_to_supabase()
        st.sidebar.info(sync_msg)
    else:
        st.sidebar.warning("⛔ Offline Mode – Sync will resume when online")
    
def is_connected():
    import socket
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        return False
