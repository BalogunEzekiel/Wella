from fpdf import FPDF
from datetime import datetime
from io import BytesIO

def generate_medical_report(name, age, gender, symptoms, result):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(200, 10, "WellaAI Medical Diagnosis Report", ln=True, align="C")

    # Date
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True)

    # Patient Info
    pdf.set_font("Arial", "B", 13)
    pdf.ln(8)
    pdf.cell(0, 10, "Patient Information", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"Name: {name}\nAge: {age}\nGender: {gender}\nSymptoms: {symptoms}")

    # Diagnosis Section
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 10, "Diagnosis Summary", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(240, 248, 255)  # Light blue

    pdf.cell(60, 10, "Diagnosis", 1, 0, 'C', True)
    pdf.cell(130, 10, result.get('Diagnosis', 'N/A'), 1, 1)

    pdf.cell(60, 10, "Confidence", 1, 0, 'C', True)
    pdf.cell(130, 10, f"{result.get('Confidence', 'N/A')}%", 1, 1)

    pdf.cell(60, 10, "Recommendation", 1, 0, 'C', True)
    pdf.multi_cell(130, 10, result.get('Recommendation', 'N/A'), 1)

    # Footer
    report_id = f"WELLAREPORT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    pdf.set_y(-30)
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 10, f"Report ID: {report_id}", ln=True, align="C")
    pdf.cell(0, 10, "Verify at: www.wella.health", ln=True, align="C")

    # Return as bytes
    return BytesIO(pdf.output(dest='S').encode('latin1'))
