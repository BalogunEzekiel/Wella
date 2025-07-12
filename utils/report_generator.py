from fpdf import FPDF
from datetime import datetime
from io import BytesIO
import random
import string

# Add Watermark
def add_watermark(pdf: FPDF):
    pdf.set_text_color(240, 240, 240)
    pdf.set_font("Arial", "B", 50)
    pdf.rotate(45, x=70, y=180)
    pdf.text(60, 190, "WELLA AI")
    pdf.rotate(0)

# Generate unique barcode string
def generate_barcode():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# Main function to create the report
def generate_medical_report(name, age, gender, symptoms, result):
    pdf = FPDF()
    pdf.add_page()

    # Watermark
    add_watermark(pdf)

    # Title
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(200, 10, "Wella Diagnostic Medical Report", ln=True, align="C")
    pdf.set_text_color(0, 0, 0)

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True)

    # Section: Patient Info
    pdf.set_font("Arial", "B", 14)
    pdf.set_fill_color(200, 230, 255)
    pdf.cell(0, 10, "Patient Details", ln=True, fill=True)
    pdf.set_font("Arial", "", 12)
    pdf.set_line_height(7.5 * 1.5)
    pdf.cell(40, 10, "Name:", 1)
    pdf.cell(0, 10, name, 1, ln=True)
    pdf.cell(40, 10, "Age:", 1)
    pdf.cell(0, 10, str(age), 1, ln=True)
    pdf.cell(40, 10, "Gender:", 1)
    pdf.cell(0, 10, gender, 1, ln=True)
    pdf.cell(40, 10, "Symptoms:", 1)
    pdf.multi_cell(0, 10, symptoms, 1)

    # Section: Diagnosis Result
    pdf.ln(4)
    pdf.set_font("Arial", "B", 14)
    pdf.set_fill_color(255, 230, 200)
    pdf.cell(0, 10, "Diagnosis Result", ln=True, fill=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(50, 10, "Diagnosis:", 1)
    pdf.cell(0, 10, result.get("Diagnosis", "N/A"), 1, ln=True)
    pdf.cell(50, 10, "Confidence:", 1)
    pdf.cell(0, 10, f"{result.get('Confidence', 'N/A')}%", 1, ln=True)

    # Section: Recommendation
    pdf.ln(4)
    pdf.set_font("Arial", "B", 14)
    pdf.set_fill_color(220, 255, 220)
    pdf.cell(0, 10, "Professional Recommendation & Prescription", ln=True, fill=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, result.get("Recommendation", "No recommendation available."))

    # Footer with barcode and website
    pdf.set_y(-30)
    pdf.set_font("Arial", "I", 10)
    barcode = generate_barcode()
    pdf.cell(0, 10, f"Unique Report ID: {barcode}", ln=True, align="C")
    pdf.cell(0, 10, "Verify at: www.wellahealth.africa/authenticate", ln=True, align="C")

    # Output to BytesIO
    pdf_output = pdf.output(dest='S').encode('latin1')
    return BytesIO(pdf_output)
