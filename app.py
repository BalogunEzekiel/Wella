import streamlit as st
import pandas as pd
import socket
import time
from datetime import datetime, date

from utils.diagnosis_engine import run_diagnosis
from utils.sync_utils import sync_to_supabase
from utils.report_generator import generate_medical_report
from utils.db import get_connection

# ⬇️ NEW: Import shared UI
from components import render_header
from landing import landing_page

# Configure page
st.set_page_config(page_title="Wella.AI", layout="wide", initial_sidebar_state="expanded")

# Detect current page from query parameters
page = st.query_params.get("page", ["landing"])[0]

# ⬇️ Display sticky top menu
render_header(active=page)

# =============== Landing Page ==========================
if page == "landing" or page == "home":
    landing_page()
    st.stop()

# =============== Login & App Page ======================
if page == "login":
    # Sidebar branding
    st.sidebar.image("assets/logo.png", width=120)
    st.sidebar.markdown("Your Offline Health Companion")

    st.markdown("### 🩺Diagnostic Assistant for Primary Healthcare")
    st.markdown("***Helping rural clinics make informed medical decisions — even offline.***")

    role = st.sidebar.selectbox("Login Role", ["Select Role", "Nurse", "Admin"])
    show_dashboard = False

    if role == "Admin":
        with st.sidebar.expander("🔐 Admin Login"):
            admin_pin = st.text_input("Enter 4-digit Admin PIN", type="password")
            show_dashboard = admin_pin == "4321"
            if admin_pin and not show_dashboard:
                st.error("❌ Incorrect PIN")

    # Diagnosis Form
    with st.form("diagnosis_form", clear_on_submit=True):
        st.subheader("📋 Patient Symptom Entry")
        name = st.text_input("Patient Name", placeholder="Enter full name")
        age = st.number_input("Age", min_value=0, max_value=120)
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        symptoms = st.text_area("Symptoms (comma-separated)", placeholder="e.g. fever, headache")
        temperature = st.text_input("Temperature (°C)", placeholder="e.g. 37.2")
        blood_pressure = st.text_input("Blood Pressure (mmHg)", placeholder="e.g. 120/80")
        weight = st.text_input("Weight (kg)", placeholder="e.g. 65")
        submitted = st.form_submit_button("Run Diagnosis")

    if submitted and symptoms:
        try:
            with st.spinner("Running AI diagnosis..."):
                result = run_diagnosis(symptoms)
                st.success("Diagnosis generated successfully.")

                # Save to DB
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO patients (
                            name, age, gender, symptoms,
                            diagnosis, confidence, recommendation,
                            temperature, blood_pressure, weight
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        name, age, gender, symptoms,
                        result.get('Diagnosis', 'N/A'),
                        result.get('Confidence', 'N/A'),
                        result.get('Recommendation', 'N/A'),
                        temperature, blood_pressure, weight
                    ))
                    conn.commit()
                    conn.close()
                    st.info("✅ Patient record and vitals saved locally.")
                    time.sleep(7)
                    st.rerun()
                except Exception as db_err:
                    st.error(f"Database Error: {db_err}")

                # PDF Report
                pdf_file = generate_medical_report(name, age, gender, symptoms, result)
                st.download_button(
                    label="📄 Download Medical Report (PDF)",
                    data=pdf_file,
                    file_name=f"{name.replace(' ', '_')}_Wella_Report.pdf",
                    mime="application/pdf"
                )
        except Exception as diag_err:
            st.error(f"Diagnosis Engine Error: {diag_err}")

    # Admin Dashboard
    if show_dashboard:
        st.markdown("---")
        st.subheader("📊 Admin Dashboard – Patient Records")
        try:
            conn = get_connection()
            df = pd.read_sql_query("SELECT * FROM patients ORDER BY created_at DESC", conn)

            name_filter = st.text_input("🔍 Search by Patient Name")
            date_filter = st.date_input("📅 Filter by Date", [])

            if name_filter:
                df = df[df['name'].str.contains(name_filter, case=False)]
            if date_filter:
                df['created_at'] = pd.to_datetime(df['created_at'])
                df = df[df['created_at'].dt.date == date_filter]

            st.dataframe(df)
            conn.close()
        except Exception as e:
            st.error(f"Could not load records: {e}")

        if st.button("🔄 Sync to Supabase"):
            status = sync_to_supabase()
            st.success(status)
            st.rerun()

    # Connectivity Check
    def is_connected():
        try:
            socket.create_connection(("1.1.1.1", 53))
            return True
        except:
            return False

    if is_connected():
        st.sidebar.success("🌐 Online – Auto Sync Enabled")
        sync_msg = sync_to_supabase()
        st.sidebar.info(sync_msg)
    else:
        st.sidebar.warning("🚫 Offline Mode – Sync will resume when online")

import streamlit as st
from streamlit_option_menu import option_menu
import landing
import service
import about
import contactus
import app  # This is assuming `app.py` contains login or another relevant function

# Horizontal Navigation Menu
selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Service", "Diagnosis", "About", "Contact"],
    icons=["house", "briefcase", "activity", "info-circle", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    key="main_menu"  # ✅ this must be unique
)

# Route to the selected page
if selected == "Home":
    landing.landing_page()

elif selected == "Service":
    service.show_service()

elif selected == "Diagnosis":
    landing.login_page()  # or app.login_page() depending on where it is

elif selected == "About":
    about.show_about()

elif selected == "Contact":
    contactus.show_contact()
