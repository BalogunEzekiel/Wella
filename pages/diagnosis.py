# app/pages/diagnosis.py
import streamlit as st
import sys, os
from dotenv import load_dotenv
from utils.auth import logout, require_login, check_authentication, enforce_role
from utils.sync_utils import sync_to_supabase
from .views import nurse_view, doctor_view, admin_view

# Load environment variables
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def show_diagnosis():
    require_login()
    user = check_authentication()
    if not user:
        st.warning("\U0001F512 Please login to access the diagnosis page.")
        return

    role = user.get("role")
    enforce_role(role, allowed_roles=["Nurse", "Admin", "Doctor"])

    st.title("\U0001FA7A Wella.AI Diagnosis Page")
    st.markdown("Welcome, **{}**".format(user.get("email", "User")))

    st.sidebar.image("assets/logo.png", width=120)
    st.sidebar.markdown("Your Offline Health Companion")
    st.sidebar.markdown(f"\U0001F464 Logged in as: `{user['email']}` ({role})")

    st.markdown("### \U0001FA7ADiagnostic Assistant for Primary Healthcare")
    st.markdown("***Helping rural clinics make informed medical decisions — even offline.***")

    if role == "Nurse":
        nurse_view.render(user)
    elif role == "Doctor":
        doctor_view.render()
    elif role == "Admin":
        admin_view.render()

    if is_connected():
        st.sidebar.success("\U0001F310 Online – Auto Sync Enabled")
        sync_msg = sync_to_supabase()
        st.sidebar.info(sync_msg)
    else:
        st.sidebar.warning("\u26D4 Offline Mode – Sync will resume when online")

    if st.sidebar.button("\U0001F6AA Logout"):
        logout()

def is_connected():
    import socket
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        return False
