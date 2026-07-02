from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def generate_report(scan_data: dict) -> bytes:
    """
    Generate a simple PDF report from scan data.
    Returns the PDF as bytes.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Advanced Website OSINT Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    for key, value in scan_data.items():
        elements.append(
            Paragraph(f"<b>{key.upper()}</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(str(value), styles["BodyText"])
        )

        elements.append(Spacer(1, 8))

    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf