from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path
from datetime import datetime

def generate_pdf_report(scan_data: dict):
    """
    Generate PDF report for a completed OSINT scan.
    """

    reports_dir = Path("app/reports")

    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{scan_data['domain']}_{timestamp}.pdf"

    pdf_path = reports_dir / filename

    doc = SimpleDocTemplate(str(pdf_path))

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Advanced Website OSINT Report",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Target Domain:</b> {scan_data['domain']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Scan Date:</b> {datetime.now().strftime('%d %B %Y %I:%M:%S %p')}",
            styles["Normal"]
        )
    )
    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # Build the PDF
    doc.build(elements)

    return str(pdf_path)

    elements.append(
        Paragraph(
            "<b>========== Scan Summary ==========</b>",
            styles["Heading2"]
        )
    )

    risk = scan_data.get("risk_score", {})

    elements.append(
        Paragraph(
            f"<b>Risk Score:</b> {risk.get('score', 'N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Grade:</b> {risk.get('grade', 'N/A')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )
    # ===============================
    # WHOIS Information
    # ===============================

    elements.append(
        Paragraph("<b>WHOIS Information</b>", styles["Heading2"])
    )

    whois = scan_data.get("whois", {})

    for key, value in whois.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # DNS Information
    # ===============================

    elements.append(
        Paragraph("<b>DNS Information</b>", styles["Heading2"])
    )

    dns = scan_data.get("dns", {})

    for key, value in dns.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # SSL Information
    # ===============================

    elements.append(
        Paragraph("<b>SSL Certificate</b>", styles["Heading2"])
    )

    ssl = scan_data.get("ssl", {})

    for key, value in ssl.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # Technology
    # ===============================

    elements.append(
        Paragraph("<b>Technology Detection</b>", styles["Heading2"])
    )

    tech = scan_data.get("technology", {})

    for key, value in tech.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # CMS
    # ===============================

    elements.append(
        Paragraph("<b>CMS Detection</b>", styles["Heading2"])
    )

    cms = scan_data.get("cms", {})

    for key, value in cms.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # WAF
    # ===============================

    elements.append(
        Paragraph("<b>WAF Detection</b>", styles["Heading2"])
    )

    waf = scan_data.get("waf", {})

    for key, value in waf.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # GeoIP
    # ===============================

    elements.append(
        Paragraph("<b>GeoIP Information</b>", styles["Heading2"])
    )

    geoip = scan_data.get("geoip", {})

    for key, value in geoip.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # ASN
    # ===============================

    elements.append(
        Paragraph("<b>ASN Information</b>", styles["Heading2"])
    )

    asn = scan_data.get("asn", {})

    for key, value in asn.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # Email Discovery
    # ===============================

    elements.append(
        Paragraph("<b>Email Discovery</b>", styles["Heading2"])
    )

    emails = scan_data.get("emails", {})

    elements.append(
        Paragraph(str(emails), styles["Normal"])
    )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # Wayback Machine
    # ===============================

    elements.append(
        Paragraph("<b>Wayback Machine</b>", styles["Heading2"])
    )

    wayback = scan_data.get("wayback", {})

    for key, value in wayback.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # Sitemap
    # ===============================

    elements.append(
        Paragraph("<b>Sitemap Analyzer</b>", styles["Heading2"])
    )

    sitemap = scan_data.get("sitemap", {})

    for key, value in sitemap.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # ===============================
    # Security.txt
    # ===============================

    elements.append(
        Paragraph("<b>Security.txt Checker</b>", styles["Heading2"])
    )

    security = scan_data.get("security_txt", {})

    for key, value in security.items():
        elements.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))    

     # ===============================
    # Security Recommendations
    # ===============================

    elements.append(
        Paragraph("<b>Security Recommendations</b>", styles["Heading2"])
    )

    recommendations = []

    risk = scan_data.get("risk_score", {})
    score = risk.get("score", 0)

    if score < 50:
        recommendations.append(
            "High Risk: Immediate security review is recommended."
        )
    elif score < 75:
        recommendations.append(
            "Medium Risk: Improve website security configuration."
        )
    else:
        recommendations.append(
            "Low Risk: Current security posture looks good."
        )

    security_headers = scan_data.get("security_headers", {})
    if isinstance(security_headers, dict):
        missing = security_headers.get("missing_headers", [])
        if missing:
            recommendations.append(
                "Missing Security Headers: " + ", ".join(missing)
            )

    if not scan_data.get("wayback", {}).get("available", False):
        recommendations.append(
            "No Wayback archive found."
        )

    if not scan_data.get("security_txt", {}).get("available", False):
        recommendations.append(
            "Publish a security.txt file to help security researchers contact you."
        )

    if not scan_data.get("sitemap", {}).get("available", False):
        recommendations.append(
            "Sitemap.xml was not found."
        )

    for item in recommendations:
        elements.append(
            Paragraph(f"• {item}", styles["Normal"])
        )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # ===============================
    # Footer
    # ===============================

    elements.append(
        Paragraph(
            "Generated by Advanced Website OSINT Framework",
            styles["Heading3"]
        )
    )

    # ===============================
    # Build PDF
    # ===============================

    doc.build(elements)

    return {
        "success": True,
        "filename": filename,
        "path": str(pdf_path)
    }   