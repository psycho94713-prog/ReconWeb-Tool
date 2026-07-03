import httpx


async def get_security_txt(domain: str):
    """
    Fetch and analyze security.txt file
    """

    urls = [
        f"https://{domain}/.well-known/security.txt",
        f"https://{domain}/security.txt"
    ]

    try:
        async with httpx.AsyncClient(timeout=15, follow_redirects=True) as client:

            for url in urls:

                response = await client.get(url)

                if response.status_code == 200:

                    lines = response.text.splitlines()

                    result = {
                        "available": True,
                        "url": url,
                        "contact": [],
                        "policy": [],
                        "hiring": [],
                        "encryption": [],
                        "expires": None
                    }

                    for line in lines:

                        line = line.strip()

                        if line.startswith("Contact:"):
                            result["contact"].append(
                                line.replace("Contact:", "").strip()
                            )

                        elif line.startswith("Policy:"):
                            result["policy"].append(
                                line.replace("Policy:", "").strip()
                            )

                        elif line.startswith("Hiring:"):
                            result["hiring"].append(
                                line.replace("Hiring:", "").strip()
                            )

                        elif line.startswith("Encryption:"):
                            result["encryption"].append(
                                line.replace("Encryption:", "").strip()
                            )

                        elif line.startswith("Expires:"):
                            result["expires"] = (
                                line.replace("Expires:", "").strip()
                            )

                    return result

        return {
            "available": False,
            "message": "security.txt not found"
        }

    except Exception as e:
        return {
            "available": False,
            "error": str(e)
        }