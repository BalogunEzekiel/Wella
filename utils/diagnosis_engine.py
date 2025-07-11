def run_diagnosis(symptoms_text):
    symptoms = [s.strip().lower() for s in symptoms_text.split(",")]
    # Very basic rules (replace with real model logic)
    if "fever" in symptoms and "headache" in symptoms:
        return {"Diagnosis": "Malaria", "Confidence": "High"}
    elif "cough" in symptoms and "shortness of breath" in symptoms:
        return {"Diagnosis": "Pneumonia", "Confidence": "Moderate"}
    else:
        return {"Diagnosis": "Unknown", "Confidence": "Low"}
