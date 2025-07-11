import streamlit as st
import pandas as pd
import numpy as np
import os
from utils.diagnosis_engine import run_diagnosis
from utils.sync_utils import sync_to_supabase

st.set_page_config(page_title="MedGuide Diagnostic Assistant", layout="centered")

# Logo and title
st.image("assets/logo.png.png", width=100)
st.title("🩺 Wella – Offline Diagnostic Assistant")
st.markdown("Helping rural clinics make informed medical decisions — offline.")

# Symptom input form
with st.form("diagnosis_form"):
    st.subheader("Enter Patient Symptoms")
    symptoms = st.text_area("List symptoms (comma-separated)", placeholder="e.g. fever, headache, body pain")
    submit = st.form_submit_button("Diagnose")

if submit and symptoms:
    result = run_diagnosis(symptoms)
    st.subheader("🧠 Diagnosis Result")
    st.write(result)
    st.success("Recommendations generated successfully.")
    st.rerun()

# Manual sync option
if st.button("🔄 Sync Records to Supabase"):
    sync_status = sync_to_supabase()
    st.info(sync_status)
