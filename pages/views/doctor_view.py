# pages/views/doctor_view.py
import streamlit as st
import pandas as pd
from utils.db import get_connection
from utils.report_generator import generate_treatment_report
import datetime
from pytz import timezone

def show_doctor_dashboard():
    st.subheader("🧾 Doctor View – Patient Diagnoses")

    try:
        conn = get_connection()
        df = pd.read_sql_query("SELECT * FROM patients ORDER BY created_at DESC", conn)
        conn.close()

        if df.empty:
            st.info("No patient records available yet.")
            return

        # Selectbox with no default selection
        patient_name = st.selectbox("Select Patient", df['name'].unique(), index=None, placeholder="Choose a patient")

        if patient_name:
            patient_record = df[df['name'] == patient_name].iloc[0]

            # Display patient record with wrap styling
            st.write("### Latest Diagnosis")
            styled_df = pd.DataFrame(patient_record).transpose().style.set_properties(
                **{'white-space': 'pre-wrap'},
                subset=['recommendation'] if 'recommendation' in patient_record else None
            )
            st.dataframe(styled_df, use_container_width=True, height=400)

            # Input for doctor notes and appointment
            treatment = st.text_area("🩹 Doctor's Treatment / Notes", value=patient_record.get('doctor_notes', ''), placeholder="Enter treatment notes or observations...")
            appointment_date = st.date_input("📅 Next Appointment Date", value=patient_record.get('appointment_date', datetime.date.today()))

            if st.button("Update Record and Generate Report"):
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE patients SET doctor_notes = ?, appointment_date = ?
                        WHERE patient_id = ?
                    """, (treatment, appointment_date.strftime("%Y-%m-%d"), patient_record['patient_id']))
                    conn.commit()
                    conn.close()
            
                    st.success("✅ Doctor's notes updated successfully.")
            
                    # Prepare data for report
                    name = patient_record['name']
                    age = patient_record['age']
                    gender = patient_record['gender']
                    symptoms = patient_record['symptoms']
                    diagnosis_data = {
                        'diagnosis': patient_record['diagnosis'],
                        'recommendation': patient_record.get('recommendation', '')
                    }
            
                    # Generate PDF report
                    pdf_data = generate_treatment_report(
                        name=name,
                        age=age,
                        gender=gender,
                        symptoms=symptoms,
                        diagnosis_data=diagnosis_data,
                        doctor_notes=treatment,
                        appointment_date=appointment_date.strftime("%Y-%m-%d")
                    )
            
                    # Display download button
                    st.download_button(
                        label="📄 Download Treatment Report",
                        data=pdf_data,
                        file_name=f"{name.replace(' ', '_')}_treatment_report.pdf",
                        mime="application/pdf"
                    )
            
                    st.rerun()
            
                except Exception as e:
                    st.error(f"❌ Could not load records: {e}")
                        
