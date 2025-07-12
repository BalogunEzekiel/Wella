import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime
from utils.diagnosis_engine import run_diagnosis
from utils.sync_utils import sync_to_supabase
import sqlite3
from utils.report_generator import generate_medical_report

# Configuration
st.set_page_config(page_title="Wella Diagnostic Assistant", layout="wide", initial_sidebar_state="expanded")

conn = sqlite3.connect("wella.db")
cursor = conn.cursor()

# Branding
st.sidebar.image("assets/logo.png", width=120)
st.sidebar.title("Wella")
st.sidebar.markdown("Your Offline Health Companion")

st.title("🩺 Wella – AI Diagnostic Assistant for Primary Healthcare")
st.markdown("Helping rural clinics make informed medical decisions — even offline.")

# PIN-protected Admin Dashboard toggle
with st.sidebar.expander("🔐 Admin Login"):
    admin_pin = st.text_input("Enter 4-digit Admin PIN", type="password")
    show_dashboard = admin_pin == "4321"
    if admin_pin and not show_dashboard:
        st.error("❌ Incorrect PIN")

# Patient Symptom Form
with st.form("diagnosis_form"):
    st.subheader("📋 Patient Symptom Entry")
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    symptoms = st.text_area("Symptoms (comma-separated)", placeholder="e.g. fever, headache, vomiting")
    submitted = st.form_submit_button("Run Diagnosis")

if submitted and symptoms:
    result = run_diagnosis(symptoms)
    st.subheader("🧠 Diagnosis Result")
    st.write(result)
    st.success("Diagnosis generated successfully.")

    # Save to local SQLite
    conn = sqlite3.connect("medguide.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (name, age, gender, symptoms, diagnosis, confidence, recommendation)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, symptoms, result['Diagnosis'], result['Confidence'], result['Recommendation']))
    conn.commit()
    conn.close()
    st.info("Patient record saved locally.")

    # ✅ Generate PDF Medical Report
    pdf_file = generate_medical_report(name, age, gender, symptoms, result)

    # ✅ Download button
    st.download_button(
        label="📄 Download Medical Report (PDF)",
        data=pdf_file,
        file_name=f"{name.replace(' ', '_')}_Wella_Report.pdf",
        mime="application/pdf"
    )

# Admin Dashboard
if show_dashboard:
    st.markdown("---")
    st.subheader("📊 Admin Dashboard – Patient Records")
    try:
        conn = sqlite3.connect("medguide.db")
        df = pd.read_sql_query("SELECT * FROM patients ORDER BY created_at DESC", conn)
        st.dataframe(df)
        conn.close()
    except Exception as e:
        st.error(f"Could not load records: {e}")

    if st.button("🔄 Sync to Supabase"):
        status = sync_to_supabase()
        st.success(status)

# Auto Sync (when internet available)
def is_connected():
    import socket
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        return False

if is_connected():
    st.sidebar.info("🌐 Online – Auto Sync Enabled")
    sync_msg = sync_to_supabase()
    st.sidebar.success(sync_msg)
else:
    st.sidebar.warning("🚫 Offline Mode – Sync will resume when online")
