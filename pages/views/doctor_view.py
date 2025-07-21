# pages/views/doctor_view.py
import streamlit as st


def show_doctor_dashboard():
    st.subheader("🩺 Doctor Dashboard")
    st.markdown("View patient data and provide recommendations here.")
    # Replace below with actual patient data fetching and display
    st.info("No patient records available yet.")


update:
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
