import sublist3r


def get_subdomains(domain: str):
    try:
        subdomains = sublist3r.main(
            domain,
            20,          # threads
            None,        # savefile
            ports=None,
            silent=True,
            verbose=False,
            enable_bruteforce=False,
            engines=None
        )

        return {
            "count": len(subdomains),
            "subdomains": subdomains
        }

    except Exception as e:
        return {
            "error": str(e)
        }