import requests


def get_asn(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, timeout=10)
        data = response.json()

        return {
            "ip": data.get("ip"),
            "asn": data.get("org"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country")
        }

    except Exception as e:
        return {
            "error": str(e)
        }