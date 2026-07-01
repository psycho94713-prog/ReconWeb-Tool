from bs4 import BeautifulSoup
from app.services.http_client import get


def analyze_javascript(domain: str):
    try:
        response = get(f"https://{domain}")

        soup = BeautifulSoup(response.text, "html.parser")

        scripts = []

        libraries = []

        for script in soup.find_all("script"):

            src = script.get("src")

            if src:
                scripts.append(src)

                s = src.lower()

                if "jquery" in s:
                    libraries.append("jQuery")

                if "react" in s:
                    libraries.append("React")

                if "vue" in s:
                    libraries.append("Vue")

                if "angular" in s:
                    libraries.append("Angular")

                if "bootstrap" in s:
                    libraries.append("Bootstrap")

        libraries = sorted(list(set(libraries)))

        return {
            "status": "success",
            "script_count": len(scripts),
            "scripts": scripts,
            "libraries": libraries
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }