# report_generator.py

from fpdf import FPDF
from io import BytesIO
from datetime import datetime
import os
import tempfile
import barcode
from barcode.writer import ImageWriter


def generate_medical_report(name, age, gender, symptoms, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    line_spacing = 12

    # === Title ===
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "WellaAI Diagnosis Report", ln=True, align="C")

    # === Date ===
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    pdf.cell(0, line_spacing, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True)

    # === Patient Info ===
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, line_spacing, "Patient Information", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(245, 245, 245)

    patient_data = [
        ("Name", name or "N/A"),
        ("Age", age if age is not None else "N/A"),
        ("Gender", gender or "N/A"),
        ("Symptoms", symptoms or "N/A")
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
        pdf.multi_cell(150, line_spacing, str(value), 1)

    # === Footer with Barcode ===
    report_id = f"WELLAREPORT-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    try:
        barcode_obj = barcode.get('code128', report_id, writer=ImageWriter())
        temp_barcode = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        barcode_obj.write(temp_barcode)
        temp_barcode.close()

        # Prevent auto-splitting
        pdf.set_auto_page_break(auto=False)

        # Footer Y position
        footer_y = 270

        # Left-aligned text
        pdf.set_xy(10, footer_y)
        pdf.set_font("Arial", "I", 10)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(0, 5, f"Report ID: {report_id}\nVerify at: https://www.wella.health", align="L")

        # Right-aligned barcode
        pdf.image(temp_barcode.name, x=150, y=footer_y, w=45, h=15)

        os.unlink(temp_barcode.name)

    except Exception as e:
        pdf.set_y(-40)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"[Error generating barcode: {e}]", ln=True, align="C")

    # ✅ Correct way to get PDF as BytesIO
    output = BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin1')  # 'S' returns as string
    output.write(pdf_bytes)
    output.seek(0)
    return output
