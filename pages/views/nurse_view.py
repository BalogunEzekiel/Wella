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


