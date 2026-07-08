from app.services.http_client import get


def detect_technology(domain: str):
    try:
        response = get(f"https://{domain}")

        headers = response.headers
        html = response.text.lower()

        technologies = []

        details = {
            "server": None,
            "backend": [],
            "frontend": [],
            "cms": [],
            "cdn": [],
            "analytics": []
        }

        server = headers.get("Server", "").lower()
        powered = headers.get("X-Powered-By", "").lower()

        # Web Servers
        
        if server:
            details["server"] = server
        
        if "nginx" in server:
            technologies.append("Nginx")
            details["backend"].append("Nginx") 

        if "apache" in server:
            technologies.append("Apache")
            details["backend"].append("Apache")

        if "iis" in server:
            technologies.append("Microsoft IIS")
            details["backend"].append("Microsoft IIS")

        # Backend
        if "php" in powered:
            technologies.append("PHP")
            details["backend"].append("PHP")

        if "asp.net" in powered:
            technologies.append("ASP.NET")
            details["backend"].append("ASP.NET")

        if "express" in powered:
             technologies.append("Node.js")
             details["backend"].append("Node.js")

        # Frontend
        if "react" in html:
            technologies.append("React")
            details["frontend"].append("React")

        if "angular" in html:
            technologies.append("Angular")
            details["frontend"].append("Angular")
        
        if "vue" in html:
            technologies.append("Vue.js")
            details["frontend"].append("Vue.js")

        if "bootstrap" in html:
            technologies.append("Bootstrap")
            details["frontend"].append("Bootstrap")

        if "jquery" in html:
            technologies.append("jQuery")
            details["frontend"].append("jQuery")

        # Analytics Detection
        if "google-analytics" in html or "gtag" in html:
            technologies.append("Google Analytics")
            details["analytics"].append("Google Analytics")

        if "googletagmanager" in html:
            technologies.append("Google Tag Manager")
            details["analytics"].append("Google Tag Manager")
        
        # CDN Detection
        if "cloudflare" in str(headers).lower():
            technologies.append("Cloudflare")
            details["cdn"].append("Cloudflare")

        # CMS
        if "wp-content" in html:
            technologies.append("WordPress")
            details["cms"].append("WordPress")
        return {
            "status": "success",
            "count": len(technologies),
            "technologies": sorted(list(set(technologies))),
            "details": details
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }