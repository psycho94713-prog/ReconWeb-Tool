import requests


def get_headers(domain: str):
    try:
        url = f"https://{domain}"

        response = requests.get(url, timeout=10)

        return dict(response.headers)

    except Exception as e:
        return {
            "error": str(e)
        }