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

        patient_name = st.selectbox(
            "Select Patient",
            df['name'].unique(),
            index=None,
            placeholder="Choose a patient"
        )

        if patient_name:
            patient_record = df[df['name'] == patient_name].iloc[0]

            st.write("### Latest Diagnosis")
            display_df = pd.DataFrame(patient_record).transpose().head(2)
            st.dataframe(display_df, use_container_width=True, height=400)

            doctor_notes = patient_record['doctor_notes'] if pd.notnull(patient_record['doctor_notes']) else ''
            appointment_date_value = (
                pd.to_datetime(patient_record['appointment_date']).date()
                if pd.notnull(patient_record['appointment_date'])
                else datetime.date.today()
            )

            # Initialize pdf_data
            pdf_data = None

            with st.form("doctor_treatment_form", clear_on_submit=True):
                treatment = st.text_area(
                    "🩹 Doctor's Treatment / Notes",
                    value=doctor_notes,
                    placeholder="Enter treatment notes or prescriptions..."
                )
                appointment_date = st.date_input(
                    "📅 Next Appointment Date",
                    value=appointment_date_value
                )

                submitted = st.form_submit_button("Update Record and Generate Report")
                if submitted:
                    try:
                        conn = get_connection()
                        cursor = conn.cursor()
                        cursor.execute("""
                            UPDATE patients 
                            SET doctor_notes = ?, appointment_date = ?
                            WHERE patient_id = ?
                        """, (treatment, appointment_date.strftime("%Y-%m-%d"), patient_record['patient_id']))
                        conn.commit()
                        conn.close()

                        st.success("✅ Doctor's notes updated successfully.")

                        diagnosis_data = {
                            'diagnosis': patient_record['diagnosis'],
                            'confidence': patient_record['confidence'],
                            'recommendation': patient_record['recommendation']
                        }

                        pdf_data = generate_treatment_report(
                            name=patient_record['name'],
                            age=patient_record['age'],
                            gender=patient_record['gender'],
                            symptoms=patient_record['symptoms'],
                            diagnosis_data=diagnosis_data,
                            doctor_notes=treatment,
                            appointment_date=appointment_date.strftime("%Y-%m-%d")
                        )

                        # Store in session state to access outside form
                        st.session_state['pdf_data'] = pdf_data
                        st.session_state['file_name'] = f"{patient_record['name'].replace(' ', '_')}_treatment_report.pdf"

                    except Exception as e:
                        st.error(f"❌ Could not update or generate report: {e}")

            # ⬇️ Moved OUTSIDE the form
            if 'pdf_data' in st.session_state:
                st.download_button(
                    label="📄 Download Treatment Report",
                    data=st.session_state['pdf_data'],
                    file_name=st.session_state['file_name'],
                    mime="application/pdf"
                )

    except Exception as e:
        st.error(f"❌ Error loading patient records: {e}")
