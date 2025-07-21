import streamlit as st

def show_nurse_form():
    st.subheader("📝 Patient Diagnosis Form")
    with st.form("nurse_form"):
        patient_name = st.text_input("Patient Full Name", placeholder="e.g., John Doe")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        symptoms = st.text_area("Symptoms", placeholder="Describe symptoms here...")
        submit = st.form_submit_button("Submit Diagnosis")

        if submit:
            st.success(f"Diagnosis for {patient_name} submitted successfully!")


update:
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
