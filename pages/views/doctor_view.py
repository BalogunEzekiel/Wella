# pages/views/doctor_view.py
import streamlit as st
import pandas as pd
from utils.db import get_connection
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

        # Selectbox with no default selected
        patient_name = st.selectbox("Select Patient", df['name'].unique(), index=None, placeholder="Choose a patient")

        if patient_name:
            patient_record = df[df['name'] == patient_name].iloc[0]

            # Display patient record with scroll and Recommendation text wrap
            st.write("### Latest Diagnosis")
            styled_df = pd.DataFrame(patient_record).transpose().style.set_properties(
                **{'white-space': 'pre-wrap'},
                subset=['recommendation'] if 'recommendation' in patient_record else None
            )
            st.dataframe(styled_df, use_container_width=True, height=400)

            treatment = st.text_area("🩹 Doctor's Treatment / Notes", placeholder="Enter treatment notes or observations...")
            appointment_date = st.date_input("📅 Next Appointment Date")

            if st.button("Update Record"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE patients SET doctor_notes = ?, appointment_date = ?
                    WHERE patient_id = ?
                """, (treatment, appointment_date.strftime("%Y-%m-%d"), patient_record['patient_id']))
                conn.commit()
                conn.close()
                st.success("✅ Doctor's notes updated successfully.")
                st.rerun()

    except Exception as e:
        st.error(f"❌ Could not load records: {e}")
