from fpdf import FPDF
from datetime import datetime
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import tempfile

def generate_medical_report(name, age, gender, symptoms, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    line_spacing = 12  # For double-line spacing

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "WellaAI Diagnosis Report", ln=True, align="C")

    # Date
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    pdf.cell(0, line_spacing, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True)

    # Patient Info Table
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, line_spacing, "Patient Information", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(245, 245, 245)

    patient_data = [
        ("Name", name),
        ("Age", age),
        ("Gender", gender),
        ("Symptoms", symptoms)
    ]

    for label, value in patient_data:
        pdf.cell(40, line_spacing, f"{label}:", border=1, fill=True)
        pdf.multi_cell(150, line_spacing, str(value), border=1)

    # Diagnosis Section
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, line_spacing, "Diagnosis Summary", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(230, 240, 255)

    pdf.cell(40, line_spacing, "Diagnosis", 1, 0, 'C', True)
    pdf.multi_cell(150, line_spacing, result.get("Diagnosis", "N/A"), 1)

    pdf.cell(40, line_spacing, "Confidence", 1, 0, 'C', True)
    pdf.multi_cell(150, line_spacing, f"{result.get('Confidence', 'N/A')}%", 1)

    pdf.cell(40, line_spacing, "Recommendation", 1, 0, 'C', True)
    pdf.multi_cell(150, line_spacing, result.get("Recommendation", "N/A"), 1)

    # Footer with Barcode
    report_id = f"WELLAREPORT-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Generate barcode image
    barcode_obj = barcode.get('code128', report_id, writer=ImageWriter())
    temp_barcode = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    barcode_obj.write(temp_barcode)
    temp_barcode.close()

    # Add barcode to PDF
    pdf.set_y(-45)
    pdf.image(temp_barcode.name, x=80, w=50, h=15)

    # Footer text
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.ln(18)
    pdf.cell(0, 6, f"Report ID: {report_id}", ln=True, align="C")
    pdf.cell(0, 6, "Verify this report at: https://www.wella.health", ln=True, align="C")

    # Return as PDF bytes
    return BytesIO(pdf.output(dest='S').encode('latin1'))
