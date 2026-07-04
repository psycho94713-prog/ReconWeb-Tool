import re
import requests
from bs4 import BeautifulSoup

from app.services.http_client import get

def extract_emails(domain: str):
    try:
        response = get(f"https://{domain}")

        soup = BeautifulSoup(response.text, "html.parser")

        html = soup.get_text()

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            html
        )

        emails = sorted(list(set(emails)))

        return {
            "status": "success",
            "count": len(emails),
            "emails": emails
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }