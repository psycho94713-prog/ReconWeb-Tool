import sublist3r


def get_subdomains(domain: str):
    try:
        subdomains = sublist3r.main(
            domain=domain,
            threads=40,
            savefile=None,
            ports=None,
            silent=True,
            verbose=False,
            enable_bruteforce=False,
            engines=None
        )

        return {
            "status": "success",
            "count": len(subdomains),
            "subdomains": sorted(list(set(subdomains)))
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }