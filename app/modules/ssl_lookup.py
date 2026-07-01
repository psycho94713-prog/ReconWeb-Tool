import ssl
import socket
from datetime import datetime


def get_ssl_info(domain: str):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:

                cert = ssock.getpeercert()

                expiry = datetime.strptime(
                    cert["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                valid_from = datetime.strptime(
                    cert["notBefore"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                return {
                    "subject": dict(x[0] for x in cert["subject"]),
                    "issuer": dict(x[0] for x in cert["issuer"]),
                    "valid_from": str(valid_from),
                    "expiry": str(expiry),
                    "days_remaining": (expiry - datetime.utcnow()).days,
                    "serial_number": cert.get("serialNumber")
                }

    except Exception as e:
        return {
            "error": str(e)
        }