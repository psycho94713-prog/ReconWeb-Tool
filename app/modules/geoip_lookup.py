import requests


def get_geoip(domain: str):
    try:
        # Domain ka IP nikalo
        ip = requests.get(f"https://dns.google/resolve?name={domain}&type=A").json()

        if "Answer" not in ip:
            return {
                "status": "error",
                "message": "IP address not found"
            }

        ip_address = ip["Answer"][0]["data"]

        # IP ka GeoIP data
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

        return {
            "status": "success",
            "ip": ip_address,
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "zip": data.get("zip"),
            "isp": data.get("isp"),
            "org": data.get("org"),
            "latitude": data.get("lat"),
            "longitude": data.get("lon"),
            "timezone": data.get("timezone")
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }