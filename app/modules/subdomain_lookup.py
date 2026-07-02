import requests


HEADERS = {
    "User-Agent": "Advanced-Website-OSINT/1.0"
}


def get_from_crtsh(domain: str):

    try:

        url = f"https://crt.sh/?q=%.{domain}&output=json"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        if response.status_code != 200:
            return set()

        data = response.json()

        results = set()

        for item in data:

            names = item.get("name_value", "")

            for name in names.split("\n"):

                name = name.strip().lower()

                if name.endswith(domain):
                    results.add(name)

        return results

    except Exception:

        return set()
def get_from_alienvault(domain: str):

    try:

        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        if response.status_code != 200:
            return set()

        data = response.json()

        results = set()

        for item in data.get("passive_dns", []):

            hostname = item.get("hostname", "").strip().lower()

            if hostname.endswith(domain):
                results.add(hostname)

        return results

    except Exception:

        return set()
def get_from_rapiddns(domain: str):

    try:

        url = f"https://rapiddns.io/subdomain/{domain}?full=1"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        if response.status_code != 200:
            return set()

        results = set()

        for line in response.text.splitlines():

            line = line.strip().lower()

            if domain in line:

                words = line.replace("<", " ").replace(">", " ").split()

                for word in words:

                    word = word.strip()

                    if word.endswith(domain):
                        results.add(word)

        return results

    except Exception:

        return set()
def get_subdomains(domain: str):

    results = set()

    # Source 1
    results.update(get_from_crtsh(domain))

    # Source 2
    results.update(get_from_alienvault(domain))

    # Source 3
    results.update(get_from_rapiddns(domain))

    results = sorted(results)

    return {
        "status": "success",
        "count": len(results),
        "subdomains": results
    }
