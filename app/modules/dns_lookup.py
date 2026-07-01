import dns.resolver


def get_dns(domain: str):

    records = {}

    record_types = ["A", "AAAA", "MX", "NS", "TXT"]

    for record in record_types:

        try:

            answers = dns.resolver.resolve(domain, record)

            records[record] = [str(r) for r in answers]

        except Exception:

            records[record] = []

    return records