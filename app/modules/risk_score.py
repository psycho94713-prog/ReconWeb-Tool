def calculate_risk_score(scan_data: dict):

    score = 100
    reasons = []

    # SSL Check
    ssl = scan_data.get("ssl", {})

    if ssl.get("status") != "success":
        score -= 20
        reasons.append("SSL Certificate Issue")
    else:
        reasons.append("SSL Certificate Valid")

    # WAF Check
    waf = scan_data.get("waf", {})

    if waf.get("detected") is True:
        reasons.append("Web Application Firewall Detected")
    else:
        score -= 10
        reasons.append("No Web Application Firewall")

    # Cloudflare Check
    technology = scan_data.get("technology", {})

    if technology.get("cloudflare") is True:
        reasons.append("Cloudflare Protection Enabled")
    else:
        score -= 5
        reasons.append("Cloudflare Protection Not Detected")

    # Grade Calculation
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"

    return {
        "score": score,
        "grade": grade,
        "reasons": reasons
    }