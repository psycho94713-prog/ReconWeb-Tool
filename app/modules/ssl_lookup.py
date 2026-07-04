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
                    
                    "subject": ", ".join(
                        f"{k}={v}"
                        for item in cert["subject"]
                        for k, v in item
               ),

                "issuer": ", ".join(
                    f"{k}={v}"
                    for item in cert["issuer"]
                    for k, v in item
                ),
                    
                    "valid_from": str(valid_from),
                    "expiry": str(expiry),
                    "days_remaining": (expiry - datetime.utcnow()).days,
                    "serial_number": cert.get("serialNumber")
                }

    except Exception as e:
        return {
            "error": str(e)
        }