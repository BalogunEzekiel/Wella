# report_generator.py
import streamlit as st
from fpdf import FPDF
from io import BytesIO
from datetime import datetime
import os
import tempfile
import barcode
from barcode.writer import ImageWriter
from pytz import timezone

def generate_medical_report(name, age, gender, symptoms, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    line_spacing = 12

    # === Header: Logo + Title Centered ===    
    logo_path = "assets/logo.png"
    logo_width = 30
    logo_height = 30  # Increased from 10 to 30
    spacing = 1
    title = "Diagnosis Report"

    pdf.set_font("Arial", "B", 16)
    title_width = pdf.get_string_width(title) + 2
    page_width = pdf.w - pdf.l_margin - pdf.r_margin  # Effective width after margins
    total_width = logo_width + spacing + title_width
    start_x = pdf.l_margin + (page_width - total_width) / 2
    y_pos = 10

    pdf.image(logo_path, x=start_x, y=y_pos, w=logo_width, h=logo_height)
    pdf.set_xy(start_x + logo_width + spacing, y_pos + 5)  # Vertically center text w.r.t logo
    pdf.set_text_color(0, 51, 102)
    pdf.cell(title_width, logo_height, title, align="L")
    pdf.ln(20)  # Add more space below due to taller header

    # === Date ===
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    user_tz = timezone("Africa/Lagos")  # Replace with dynamic tz as needed
    local_time = datetime.now(user_tz)
    pdf.cell(0, line_spacing, f"Date: {local_time.strftime('%d %B %Y, %I:%M %p')}", ln=True)
    
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

    # === Diagnosis Summary ===
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

        pdf.set_auto_page_break(auto=False)
        footer_y = 270

        pdf.image(temp_barcode.name, x=150, y=footer_y, w=45, h=15)
        os.unlink(temp_barcode.name)

    except Exception as e:
        pdf.set_y(-40)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"[Error generating barcode: {e}]", ln=True, align="C")

    # Export as BytesIO
    output = BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    output.write(pdf_bytes)
    output.seek(0)
    return output

def generate_treatment_report(name, age, gender, symptoms, diagnosis_data, doctor_notes, appointment_date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    line_spacing = 12

    # === Header: Logo + Title Centered ===    
    logo_path = "assets/logo.png"
    logo_width = 30
    logo_height = 30
    spacing = 1
    title = "Treatment Report"

    pdf.set_font("Arial", "B", 16)
    title_width = pdf.get_string_width(title) + 2
    page_width = pdf.w - pdf.l_margin - pdf.r_margin
    total_width = logo_width + spacing + title_width
    start_x = pdf.l_margin + (page_width - total_width) / 2
    y_pos = 10

    pdf.image(logo_path, x=start_x, y=y_pos, w=logo_width, h=logo_height)
    pdf.set_xy(start_x + logo_width + spacing, y_pos + 5)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(title_width, logo_height, title, align="L")
    pdf.ln(20)

    # === Date ===
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    user_tz = timezone("Africa/Lagos")
    local_time = datetime.now(user_tz)
    pdf.cell(0, line_spacing, f"Date: {local_time.strftime('%d %B %Y, %I:%M %p')}", ln=True)

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

    # === Diagnosis Summary ===
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, line_spacing, "Diagnosis Summary", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(230, 240, 255)

    summary_data = [
        ("Diagnosis", diagnosis_data.get("diagnosis", "N/A")),
        ("Confidence", f"{diagnosis_data.get('confidence', 'N/A')}%"),
        ("Recommendation", diagnosis_data.get("recommendation", "N/A"))
    ]

    for label, value in summary_data:
        pdf.cell(40, line_spacing, label, 1, 0, 'C', True)
        pdf.multi_cell(150, line_spacing, str(value), 1)

    # === Doctor's Treatment Section ===
    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, line_spacing, "Doctor's Treatment", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(240, 255, 240)

    treatment_data = [
        ("Doctor's Notes", doctor_notes or "Not provided"),
        ("Next Appointment", appointment_date or "Not scheduled")
    ]

    for label, value in treatment_data:
        pdf.cell(40, line_spacing, label, 1, 0, 'C', True)
        pdf.multi_cell(150, line_spacing, str(value), 1)

    # === Footer with Barcode ===
    report_id = f"WELLA.AI-TREATMENT-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    try:
        barcode_obj = barcode.get('code128', report_id, writer=ImageWriter())
        temp_barcode = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        barcode_obj.write(temp_barcode)
        temp_barcode.close()

        pdf.set_auto_page_break(auto=False)
        footer_y = 270
        pdf.image(temp_barcode.name, x=150, y=footer_y, w=45, h=15)
        os.unlink(temp_barcode.name)

    except Exception as e:
        pdf.set_y(-40)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"[Error generating barcode: {e}]", ln=True, align="C")

    # Export as BytesIO
    output = BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    output.write(pdf_bytes)
    output.seek(0)
    return output
