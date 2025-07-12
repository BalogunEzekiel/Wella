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
    }
]


def run_diagnosis(symptoms_text):
    """
    Processes a comma-separated symptom string and returns a diagnosis dictionary.
    """
    cleaned_input = re.sub(r"[^a-zA-Z0-9, ]", "", symptoms_text).lower()
    input_symptoms = {sym.strip() for sym in cleaned_input.split(",") if sym.strip()}

    best_match = None
    max_overlap = 0

    for rule in DISEASE_RULES:
        overlap = input_symptoms.intersection(rule["symptoms"])
        if len(overlap) >= rule["min_match"] and len(overlap) > max_overlap:
            best_match = rule
            max_overlap = len(overlap)

    if best_match:
        return {
            "Diagnosis": best_match["name"],
            "Confidence": best_match["confidence"],
            "Recommendation": best_match["recommendation"],
            "Matched Symptoms": ", ".join(input_symptoms.intersection(best_match["symptoms"])),
            "Considered Symptoms": ", ".join(best_match["symptoms"])
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
