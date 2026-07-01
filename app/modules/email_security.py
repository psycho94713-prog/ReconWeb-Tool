import dns.resolver


def check_email_security(domain: str):
    result = {
        "spf": "Not Found",
        "dmarc": "Not Found",
        "dkim": "Not Checked"
    }

    try:
        answers = dns.resolver.resolve(domain, "TXT")

        for record in answers:
            txt = "".join(record.strings[0].decode() if isinstance(record.strings[0], bytes) else record.strings[0])

            if "v=spf1" in txt.lower():
                result["spf"] = txt

    except Exception:
        pass

    try:
        answers = dns.resolver.resolve(f"_dmarc.{domain}", "TXT")

        for record in answers:
            txt = "".join(record.strings[0].decode() if isinstance(record.strings[0], bytes) else record.strings[0])

            if "v=dmarc1" in txt.lower():
                result["dmarc"] = txt

    except Exception:
        pass

    return {
        "status": "success",
        "records": result
    }