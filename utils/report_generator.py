from fpdf import FPDF
import qrcode
from PIL import Image
from datetime import datetime
from io import BytesIO

# Generate QR Code
def generate_qr_code(data: str) -> bytes:
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return buffer.getvalue()

# Add Watermark
def add_watermark(pdf: FPDF):
    pdf.set_text_color(220, 220, 220)
    pdf.set_font("Arial", "B", 50)
    pdf.rotate(45, x=70, y=180)
    pdf.text(60, 190, "WELLA AI")
    pdf.rotate(0)

# Main function to create the report
def generate_medical_report(name, age, gender, symptoms, result):
    pdf = FPDF()
    pdf.add_page()

    # Watermark
    add_watermark(pdf)

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Wella Diagnostic Medical Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True)

    # Patient Info
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Patient Details", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, f"""
Name: {name}
Age: {age}
Gender: {gender}
Symptoms: {symptoms}
""")

    # Diagnosis
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Diagnosis Result", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Diagnosis: {result.get('Diagnosis', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Confidence: {result.get('Confidence', 'N/A')}%", ln=True)

    # Recommendation
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Professional Recommendation & Prescription", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, result.get('Recommendation', 'No recommendation available.'))

    # QR Code
    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    report_id = f"{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    qr_data = f"WellaReport:{report_id}"
    qr_image = generate_qr_code(qr_data)

    qr_path = f"temp_qr_{report_id}.png"
    with open(qr_path, "wb") as f:
        f.write(qr_image)

    pdf.image(qr_path, x=160, y=250, w=30)

    # Output
    output = BytesIO()
    pdf.output(output)
    output.seek(0)
    return output
