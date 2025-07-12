from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self._line_height = 10  # default line height

    def set_line_height(self, height):
        self._line_height = height

    def get_line_height(self):
        return self._line_height

    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "🩺 Medical Diagnostic Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 0, "C")

def generate_medical_report(name, age, gender, symptoms, result):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)
    pdf.set_line_height(7.5 * 1.5)  # or simply pdf._line_height = 11.25

    # Patient Details
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Patient Details", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Age: {age}", ln=True)
    pdf.cell(0, 10, f"Gender: {gender}", ln=True)
    pdf.ln(5)

    # Symptoms
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Reported Symptoms", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, pdf.get_line_height(), symptoms)
    pdf.ln(5)

    # Diagnosis
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Diagnosis Result", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Diagnosis: {result.get('Diagnosis', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Confidence: {result.get('Confidence', 'N/A')}%", ln=True)
    pdf.ln(5)

    # Recommendation
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Recommendation", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, pdf.get_line_height(), result.get("Recommendation", "No recommendation provided."))

    # Save to file
    output_path = "medical_report.pdf"
    pdf.output(output_path)
    return output_path
