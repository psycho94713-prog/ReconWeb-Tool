from app.services.http_client import get


def detect_technology(domain: str):
    try:
        response = get(f"https://{domain}")

        headers = response.headers
        html = response.text.lower()

        technologies = []

        server = headers.get("Server", "").lower()
        powered = headers.get("X-Powered-By", "").lower()

        # Web Servers
        if "nginx" in server:
            technologies.append("Nginx")

        if "apache" in server:
            technologies.append("Apache")

        if "iis" in server:
            technologies.append("Microsoft IIS")

        # Backend
        if "php" in powered:
            technologies.append("PHP")

        if "asp.net" in powered:
            technologies.append("ASP.NET")

        if "express" in powered:
            technologies.append("Node.js")

        # Frontend
        if "react" in html:
            technologies.append("React")

        if "angular" in html:
            technologies.append("Angular")

        if "vue" in html:
            technologies.append("Vue.js")

        if "bootstrap" in html:
            technologies.append("Bootstrap")

        if "jquery" in html:
            technologies.append("jQuery")

        # CMS
        if "wp-content" in html:
            technologies.append("WordPress")

        return {
            "status": "success",
            "count": len(technologies),
            "technologies": sorted(list(set(technologies)))
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }