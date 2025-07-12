from fpdf import FPDF
from datetime import datetime
from io import BytesIO
import random

# Add Watermark
def add_watermark(pdf: FPDF):
    pdf.set_text_color(220, 220, 220)
    pdf.set_font("Arial", "B", 48)
    pdf.rotate(45, x=70, y=180)
    pdf.text(60, 190, "WELLA AI")
    pdf.rotate(0)

# Main function to create the report
def generate_medical_report(name, age, gender, symptoms, result, temperature="", blood_pressure="", weight="", appointment_date=""):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    line_spacing = 8

    # Watermark
    add_watermark(pdf)

    # Header
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 70, 120)
    pdf.cell(200, 10, "Wella Diagnostic Medical Report", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True)

    # Patient Info
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, line_spacing, "👤 Patient Details", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, line_spacing, f"Name: {name}", ln=True)
    pdf.cell(0, line_spacing, f"Age: {age}     Gender: {gender}", ln=True)
    pdf.cell(0, line_spacing, f"Symptoms: {symptoms}", ln=True)

    # Diagnosis Table
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, line_spacing, "🧠 Diagnosis Summary", ln=True)

    pdf.set_fill_color(230, 240, 255)
    pdf.set_font("Arial", "", 12)
    pdf.cell(50, line_spacing, "Diagnosis", border=1, fill=True)
    pdf.cell(40, line_spacing, "Confidence (%)", border=1, fill=True)
    pdf.cell(100, line_spacing, "Recommendation", border=1, ln=True, fill=True)

    pdf.set_fill_color(255, 255, 255)
    pdf.cell(50, line_spacing, result.get('Diagnosis', 'N/A'), border=1)
    pdf.cell(40, line_spacing, result.get('Confidence', 'N/A'), border=1)
    pdf.cell(100, line_spacing, result.get('Recommendation', 'N/A')[:45] + "...", border=1, ln=True)

    # Vitals Table
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, line_spacing, "🩺 Vitals & Clinical Observations", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(245, 245, 245)
    pdf.cell(50, line_spacing, "Temperature (°C)", border=1, fill=True)
    pdf.cell(40, line_spacing, "Blood Pressure", border=1, fill=True)
    pdf.cell(40, line_spacing, "Weight (kg)", border=1, fill=True)
    pdf.cell(60, line_spacing, "Next Appointment", border=1, ln=True, fill=True)

    pdf.set_fill_color(255, 255, 255)
    pdf.cell(50, line_spacing, temperature or "N/A", border=1)
    pdf.cell(40, line_spacing, blood_pressure or "N/A", border=1)
    pdf.cell(40, line_spacing, weight or "N/A", border=1)
    pdf.cell(60, line_spacing, appointment_date or "N/A", border=1, ln=True)

    # Footnote & Barcode
    pdf.ln(15)
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Visit https://wella.healthcare/verify to authenticate this report.", ln=True)
    report_id = f"W-{random.randint(100000,999999)}-{datetime.now().strftime('%y%m%d')}"
    pdf.cell(0, 6, f"Report ID: {report_id}", ln=True)

    # Return PDF
    pdf_output = pdf.output(dest="S").encode("latin1")
    return BytesIO(pdf_output)
