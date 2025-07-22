import re

# Symptom rule definitions with weighted matches and medical logic
DISEASE_RULES = [
    {
        "name": "Malaria",
        "symptoms": {"fever", "chills", "headache", "sweating", "body pain", "nausea"},
        "min_match": 2,
        "confidence": "High",
        "recommendation": (
            "Administer a full course of antimalarial drugs such as artemether-lumefantrine. "
            "Advise hydration, rest, and follow-up in 3 days."
        )
    },
    {
        "name": "Pneumonia",
        "symptoms": {"cough", "fever", "chest pain", "shortness of breath", "fatigue"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Start empirical antibiotic therapy (e.g., amoxicillin/clavulanate). "
            "Encourage rest and check for signs of respiratory distress."
        )
    },
    {
        "name": "Typhoid Fever",
        "symptoms": {"fever", "abdominal pain", "diarrhea", "weakness", "loss of appetite"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Prescribe ciprofloxacin or azithromycin. Recommend proper fluid intake and light diet. "
            "Monitor temperature regularly."
        )
    },
    {
        "name": "Common Cold",
        "symptoms": {"sore throat", "runny nose", "sneezing", "mild cough"},
        "min_match": 2,
        "confidence": "Low",
        "recommendation": (
            "Suggest rest, warm fluids, vitamin C, and paracetamol for symptom relief. "
            "Avoid cold weather and crowd exposure."
        )
    },
    {
        "name": "COVID-19",
        "symptoms": {"fever", "dry cough", "loss of taste", "loss of smell", "fatigue"},
        "min_match": 2,
        "confidence": "High",
        "recommendation": (
            "Recommend self-isolation, supportive care, and testing. Monitor oxygen saturation levels. "
            "Refer for medical evaluation if symptoms worsen."
        )
    },
    {
        "name": "Dengue Fever",
        "symptoms": {"fever", "rash", "joint pain", "muscle pain", "headache", "eye pain"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Recommend paracetamol for fever and pain. Avoid NSAIDs. Ensure adequate hydration and monitor platelet count."
        )
    },
    {
        "name": "Tuberculosis",
        "symptoms": {"persistent cough", "weight loss", "night sweats", "fever", "fatigue"},
        "min_match": 2,
        "confidence": "High",
        "recommendation": (
            "Refer for sputum test and chest X-ray. Begin DOTS therapy if confirmed. Advise isolation during infectious phase."
        )
    },
    {
        "name": "Asthma",
        "symptoms": {"shortness of breath", "wheezing", "cough", "chest tightness"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Administer bronchodilators (e.g., salbutamol inhaler). Monitor peak flow. Refer if symptoms persist or worsen."
        )
    },
    {
        "name": "Hypertension",
        "symptoms": {"headache", "dizziness", "blurred vision", "chest discomfort"},
        "min_match": 2,
        "confidence": "Low",
        "recommendation": (
            "Check blood pressure. Initiate lifestyle changes. If persistent, consider starting antihypertensives."
        )
    },
    {
        "name": "Urinary Tract Infection",
        "symptoms": {"burning urination", "frequent urination", "lower abdominal pain", "cloudy urine"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Prescribe antibiotics like nitrofurantoin. Encourage increased fluid intake. Recommend urinalysis."
        )
    },
    {
        "name": "Peptic Ulcer",
        "symptoms": {"abdominal pain", "bloating", "nausea", "heartburn", "loss of appetite"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Start proton pump inhibitors (e.g., omeprazole). Avoid NSAIDs. Recommend H. pylori testing."
        )
    },
    {
        "name": "Migraine",
        "symptoms": {"headache", "nausea", "light sensitivity", "visual disturbance"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Recommend rest in a dark room, NSAIDs or triptans if available. Avoid known triggers."
        )
    },
    {
        "name": "Diabetes Mellitus",
        "symptoms": {"frequent urination", "excessive thirst", "fatigue", "blurred vision", "weight loss"},
        "min_match": 2,
        "confidence": "Low",
        "recommendation": (
            "Check blood glucose. Recommend dietary control and refer for endocrinology follow-up if elevated."
        )
    },
    {
        "name": "Hepatitis B",
        "symptoms": {"fatigue", "nausea", "yellow eyes", "dark urine", "abdominal pain"},
        "min_match": 2,
        "confidence": "High",
        "recommendation": (
            "Refer for liver function tests and viral load. Counsel on avoiding alcohol. Monitor liver health closely."
        )
    },
    {
        "name": "Appendicitis",
        "symptoms": {"abdominal pain", "nausea", "vomiting", "loss of appetite", "fever"},
        "min_match": 2,
        "confidence": "High",
        "recommendation": (
            "Urgently refer to surgical unit. Avoid food and water intake. Monitor for signs of rupture."
        )
    },
    {
        "name": "Gastroenteritis",
        "symptoms": {"diarrhea", "vomiting", "abdominal cramps", "fever"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Recommend oral rehydration salts (ORS), zinc supplements, and dietary rest. Monitor hydration status."
        )
    },
    {
        "name": "Sinusitis",
        "symptoms": {"facial pain", "nasal congestion", "headache", "postnasal drip"},
        "min_match": 2,
        "confidence": "Low",
        "recommendation": (
            "Use nasal saline irrigation, steam inhalation, and decongestants. Antibiotics if bacterial signs persist."
        )
    },
    {
        "name": "Otitis Media",
        "symptoms": {"ear pain", "fever", "hearing loss", "ear discharge"},
        "min_match": 2,
        "confidence": "Moderate",
        "recommendation": (
            "Prescribe amoxicillin if bacterial. Recommend analgesics and follow-up in 3 days."
        )
    },
    {
        "name": "Anemia",
        "symptoms": {"fatigue", "pale skin", "shortness of breath", "dizziness"},
        "min_match": 2,
        "confidence": "Low",
        "recommendation": (
            "Check hemoglobin levels. Recommend iron-rich foods or iron supplements. Investigate underlying causes."
        )
    },
    {
        "name": "Measles",
        "symptoms": {"fever", "rash", "runny nose", "red eyes", "cough"},
        "min_match": 2,
        "confidence": "High",
        "recommendation": (
            "Isolate the patient. Provide supportive care including vitamin A. Monitor for complications like pneumonia."
        )
    }
]

def run_diagnosis(symptoms_text):
    print("DEBUG: symptoms_text received =>", symptoms_text, type(symptoms_text))


#def run_diagnosis(symptoms_text):
    """
    Processes a comma-separated symptom string and returns a diagnosis dictionary.
    """
    # === Input validation ===
    if not isinstance(symptoms_text, str) or not symptoms_text.strip():
        return {
            "Diagnosis": "Invalid Input",
            "Confidence": "None",
            "Recommendation": "Please provide symptoms as a comma-separated string.",
            "Matched Symptoms": "None",
            "Considered Symptoms": "N/A"
        }

    # === Preprocess and tokenize symptoms ===
    cleaned_input = re.sub(r"[^a-zA-Z0-9, ]", "", symptoms_text).lower()
    input_symptoms = {sym.strip() for sym in cleaned_input.split(",") if sym.strip()}

    best_match = None
    max_overlap = 0

    # === Match against disease rules ===
    for rule in DISEASE_RULES:
        overlap = input_symptoms.intersection(rule["symptoms"])
        if len(overlap) >= rule["min_match"] and len(overlap) > max_overlap:
            best_match = rule
            max_overlap = len(overlap)

    # === Return result ===
    if best_match:
        return {
            "Diagnosis": best_match["name"],
            "Confidence": best_match["confidence"],
            "Recommendation": best_match["recommendation"],
            "Matched Symptoms": ", ".join(sorted(input_symptoms.intersection(best_match["symptoms"]))),
            "Considered Symptoms": ", ".join(sorted(best_match["symptoms"]))
        }
    else:
        return {
            "Diagnosis": "Unknown",
            "Confidence": "Low",
            "Recommendation": (
                "Insufficient symptom match. Refer to a doctor for further evaluation or request lab tests "
                "such as malaria RDT, Widal, or chest X-ray depending on severity."
            ),
            "Matched Symptoms": "None",
            "Considered Symptoms": "N/A"
        }
