# utils/auth.py

import streamlit as st

def check_authentication():
    return st.session_state.get("authenticated", False)

def get_current_user():
    return st.session_state.get("user", {})

def enforce_role(required_roles):
    user = get_current_user()
    if user.get("role") not in required_roles:
        st.error("You don't have permission to view this page.")
        st.stop()

def require_login():
    if not st.session_state.get("authenticated"):
        st.warning("🔒 Please login to access the diagnosis page.")
        if st.button("🔑 Login"):
            st.switch_page("diagnosis.py")
        st.stop()
