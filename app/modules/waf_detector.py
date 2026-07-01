from app.services.http_client import get

def detect_waf(domain: str):
    try:
        response = get(f"https://{domain}")   

        headers = response.headers

        server = headers.get("Server", "").lower()

        waf = "Unknown"

        if "cloudflare" in server:
            waf = "Cloudflare"

        elif "akamai" in server:
            waf = "Akamai"

        elif "sucuri" in server:
            waf = "Sucuri"

        elif "imperva" in server:
            waf = "Imperva"

        elif "awselb" in server:
            waf = "AWS WAF"

        elif "f5" in server:
            waf = "F5 BIG-IP"

        return {
            "status": "success",
            "waf": waf
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }