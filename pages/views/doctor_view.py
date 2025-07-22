# pages/views/doctor_view.py
import streamlit as st
import pandas as pd
from utils.db import get_connection
from utils.report_generator import generate_treatment_report
import datetime

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
                # Update DB with new doctor's note and appointment date
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE patients SET doctor_notes = ?, appointment_date = ?
                    WHERE patient_id = ?
                """, (treatment, appointment_date.strftime("%Y-%m-%d"), patient_record['patient_id']))
                conn.commit()
                conn.close()

                # Refresh local copy with updated notes
                patient_record['doctor_notes'] = treatment
                patient_record['appointment_date'] = appointment_date.strftime("%Y-%m-%d")

                # Generate report
                pdf_file = generate_treatment_report(patient_record.to_dict())

                st.success("✅ Record updated and treatment report generated.")
                st.download_button(
                    label="📥 Download Treatment Report (PDF)",
                    data=pdf_file,
                    file_name=f"{patient_name}_Treatment_Report.pdf",
                    mime="application/pdf"
                )
                st.rerun()

    except Exception as e:
        st.error(f"❌ Could not load records: {e}")
