import streamlit as st

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
                st.rerun()  # Use new rerun
            else:
                st.error("❌ Invalid credentials")

        st.stop()  # Prevent page content from rendering if not authenticated
