from fastapi import APIRouter
from pydantic import BaseModel

from app.modules.whois_lookup import get_whois
from app.modules.dns_lookup import get_dns
from app.modules.ssl_lookup import get_ssl_info
from app.modules.headers_lookup import get_headers
#from app.modules.tech_lookup import detect_technology
from app.modules.subdomain_lookup import get_subdomains
from app.modules.port_scan import scan_ports
from app.modules.subdomain_lookup import get_subdomains

router = APIRouter(prefix="/api/v1/osint", tags=["OSINT"])


class DomainRequest(BaseModel):
    domain: str


@router.post("/domain")
async def scan_domain(request: DomainRequest):
    return {
        "domain": request.domain,
        "whois": get_whois(request.domain),
        "dns": get_dns(request.domain),
        "ssl": get_ssl_info(request.domain),
        "headers": get_headers(request.domain),
        #"technology": detect_technology(request.domain)
        "subdomains": get_subdomains(request.domain),
        "ports": scan_ports(request.domain),
        "subdomains": get_subdomains(request.domain)
    }