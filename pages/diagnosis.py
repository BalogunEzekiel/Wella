import streamlit as st
import pandas as pd
import socket
import time
from utils.db import get_connection
from utils.diagnosis_engine import run_diagnosis
from utils.report_generator import generate_medical_report
from utils.sync_utils import sync_to_supabase
from utils.auth import require_login, check_authentication, enforce_role

# ✅ Force login before anything else
require_login()

# ✅ Now get the user info and check roles
user = check_authentication()
role = user['role']
enforce_role(role, allowed_roles=["Nurse", "Admin", "Doctor"])

def show_diagnosis():
    # Authenticate User
    user = check_authentication()
    if not user:
        st.warning("🔒 Please login to access the diagnosis page.")
        return

    # Sidebar
    st.sidebar.image("assets/logo.png", width=120)
    st.sidebar.markdown("Your Offline Health Companion")
    st.sidebar.markdown(f"👤 Logged in as: `{user['email']}` ({role})")

    st.markdown("### 🩺Diagnostic Assistant for Primary Healthcare")
    st.markdown("***Helping rural clinics make informed medical decisions — even offline.***")

    # Nurse Dashboard: Create Diagnosis
    if role == "Nurse":
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

                    try:
                        conn = get_connection()
                        cursor = conn.cursor()
                        cursor.execute("""
                            INSERT INTO patients (
                                name, age, gender, symptoms,
                                diagnosis, confidence, recommendation,
                                temperature, blood_pressure, weight, created_by
                            )
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (
                            name, age, gender, symptoms,
                            result.get('Diagnosis', 'N/A'),
                            result.get('Confidence', 'N/A'),
                            result.get('Recommendation', 'N/A'),
                            temperature, blood_pressure, weight,
                            user['id']
                        ))
                        conn.commit()
                        conn.close()
                        st.info("✅ Patient record and vitals saved locally.")
                    except Exception as db_err:
                        st.error(f"Database Error: {db_err}")

                    pdf_file = generate_medical_report(name, age, gender, symptoms, result)
                    st.download_button(
                        label="📄 Download Medical Report (PDF)",
                        data=pdf_file,
                        file_name=f"{name.replace(' ', '_')}_Wella_Report.pdf",
                        mime="application/pdf"
                    )
            except Exception as diag_err:
                st.error(f"Diagnosis Engine Error: {diag_err}")

    # Doctor Dashboard: View and Treat
    elif role == "Doctor":
        st.subheader("🧾 Doctor View – Patient Diagnoses")
        try:
            conn = get_connection()
            df = pd.read_sql_query("SELECT * FROM patients ORDER BY created_at DESC", conn)
            conn.close()

            patient_name = st.selectbox("Select Patient", df['name'].unique())
            patient_record = df[df['name'] == patient_name].iloc[0]

            st.write("### Latest Diagnosis")
            st.json(patient_record.to_dict())

            treatment = st.text_area("🩹 Doctor's Treatment / Notes")
            appointment_date = st.date_input("📅 Next Appointment Date")
            if st.button("Update Record"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE patients SET doctor_notes = ?, appointment_date = ?
                    WHERE id = ?
                """, (treatment, appointment_date.strftime("%Y-%m-%d"), patient_record['id']))
                conn.commit()
                conn.close()
                st.success("Doctor's notes updated.")

        except Exception as e:
            st.error(f"Could not load records: {e}")

    # Admin Dashboard: Manage Users and Sync
    elif role == "Admin":
        st.subheader("📊 Admin Dashboard – Patient Records")
        try:
            conn = get_connection()
            df = pd.read_sql_query("SELECT * FROM patients ORDER BY created_at DESC", conn)
            conn.close()

            name_filter = st.text_input("🔍 Search by Patient Name")
            date_filter = st.date_input("📅 Filter by Date", [])

            if name_filter:
                df = df[df['name'].str.contains(name_filter, case=False)]
            if date_filter:
                df['created_at'] = pd.to_datetime(df['created_at'])
                df = df[df['created_at'].dt.date == date_filter]

            st.dataframe(df)

        except Exception as e:
            st.error(f"Could not load records: {e}")

        if st.button("🔄 Sync to Supabase"):
            status = sync_to_supabase()
            st.success(status)
            st.rerun()

    # Connectivity
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
