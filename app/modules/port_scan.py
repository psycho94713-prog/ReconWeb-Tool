import nmap


def scan_ports(target):
    try:
        scanner = nmap.PortScanner()

        scanner.scan(
            target,
            arguments="-F"
        )

        result = {}

        for host in scanner.all_hosts():
            result[host] = {
                "state": scanner[host].state(),
                "protocols": {}
            }

            for proto in scanner[host].all_protocols():
                result[host]["protocols"][proto] = []

                ports = scanner[host][proto].keys()

                for port in sorted(ports):
                    result[host]["protocols"][proto].append({
                        "port": port,
                        "state": scanner[host][proto][port]["state"],
                        "service": scanner[host][proto][port]["name"]
                    })

        return result

    except Exception as e:
        return {
            "error": str(e)
        }