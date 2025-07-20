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
    # Define dimensions and content
    logo_path = "assets/logo.png"
    logo_width = 30
    logo_height = 10
    spacing = 5
    title = "Wella.AI Diagnosis Report"
    
    # Set font for measuring and rendering
    pdf.set_font("Arial", "B", 16)
    title_width = pdf.get_string_width(title) + 2  # text width + padding
    page_width = pdf.w
    
    # Calculate total width and X start
    total_width = logo_width + spacing + title_width
    start_x = (page_width - total_width) / 2
    y_pos = 10
    
    # Add logo
    pdf.image(logo_path, x=start_x, y=y_pos, w=logo_width, h=logo_height)
    
    # Add title next to logo
    pdf.set_xy(start_x + logo_width + spacing, y_pos)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(title_width, logo_height, title, align="L")
    
    # Add vertical space after header
    pdf.ln(20)
    st.markdown(---)

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
    report_id = f"WELLA.AI-REPORT-{datetime.now().strftime('%Y%m%d%H%M%S')}"

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
        pdf.multi_cell(0, 5, f"Report ID: {report_id}\nVerify at: https://www.wella.ai", align="L")

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
