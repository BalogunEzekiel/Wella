import streamlit as st
from utils.run_diagnosis import run_diagnosis
from utils.medical_report import generate_medical_report
from utils.db import get_connection
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

def show_nurse_form(user):
    st.subheader("📋 Patient Symptom Entry")

    with st.form("diagnosis_form", clear_on_submit=True):
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
