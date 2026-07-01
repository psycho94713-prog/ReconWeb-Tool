from app.services.http_client import get


def analyze_security_headers(domain: str):
    try:
        response = get(f"https://{domain}")

        headers = response.headers

        security_headers = {
            "Content-Security-Policy": headers.get("Content-Security-Policy", "Missing"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security", "Missing"),
            "X-Frame-Options": headers.get("X-Frame-Options", "Missing"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options", "Missing"),
            "Referrer-Policy": headers.get("Referrer-Policy", "Missing"),
            "Permissions-Policy": headers.get("Permissions-Policy", "Missing")
        }

        return {
            "status": "success",
            "headers": security_headers
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }