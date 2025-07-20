from fpdf import FPDF
from datetime import datetime
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import tempfile
import os

def generate_medical_report(name, age, gender, symptoms, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    line_spacing = 12  # Double line spacing for readability

    # === Logo and Title ===
    pdf.image("logo.png", x=10, y=10, w=30)  # Ensure 'logo.png' is in same folder
    pdf.set_xy(50, 10)
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "Wella.AI Diagnosis Report", ln=True, align="L")
    pdf.ln(20)

    # === Date ===
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, line_spacing, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True)

    # === Patient Info ===
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

    # === Diagnosis ===
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, line_spacing, "Diagnosis Summary", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(230, 240, 255)

    diagnosis_data = [
        ("Diagnosis", result.get("Diagnosis", "N/A")),
        ("Confidence", f"{result.get('Confidence', 'N/A')}%"),
        ("Recommendation", result.get("Recommendation", "N/A"))
    ]

    for label, value in diagnosis_data:
        pdf.cell(40, line_spacing, label, 1, 0, 'C', True)
        pdf.multi_cell(150, line_spacing, value, 1)

    # === Footer with Barcode ===
    report_id = f"WELLA.AIREPORT-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    try:
        barcode_obj = barcode.get('code128', report_id, writer=ImageWriter())
        temp_barcode = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        barcode_obj.write(temp_barcode)
        temp_barcode.close()

        # Prevent auto-splitting
        pdf.set_auto_page_break(auto=False)

        footer_y = 270  # Position close to bottom

        # Left-aligned footer text
        pdf.set_xy(10, footer_y)
        pdf.set_font("Arial", "I", 10)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(0, 5, f"Report ID: {report_id}\nVerify at: https://www.wella.ai", align="L")

        # Right-aligned barcode
        pdf.image(temp_barcode.name, x=150, y=footer_y, w=45, h=15)

        # Clean up temp file
        os.unlink(temp_barcode.name)

    except Exception as e:
        pdf.set_y(-40)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"[Error generating barcode: {e}]", ln=True, align="C")

    # === Return PDF as binary data ===
    output = BytesIO()
    pdf.output(output)
    output.seek(0)
    return output
