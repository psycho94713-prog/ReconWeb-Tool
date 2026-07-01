from app.services.http_client import get


COMMON_PATHS = [
    "/admin",
    "/login",
    "/dashboard",
    "/backup",
    "/config",
    "/phpmyadmin",
    "/robots.txt",
    "/.git"
]


def enumerate_directories(domain: str):
    results = []

    for path in COMMON_PATHS:
        try:
            response = get(f"https://{domain}{path}")

            if response.status_code < 400:
                results.append({
                    "path": path,
                    "status_code": response.status_code
                })

        except Exception:
            pass

    return {
        "status": "success",
        "found": len(results),
        "directories": results
    }