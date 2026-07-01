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
from app.modules.geoip_lookup import get_geoip
from app.modules.asn_lookup import get_asn
from app.modules.email_extractor import extract_emails
from app.modules.cms_detector import detect_cms
from app.modules.waf_detector import detect_waf
from app.modules.security_headers import analyze_security_headers
from app.modules.javascript_analyzer import analyze_javascript
from app.modules.directory_enum import enumerate_directories
from app.modules.email_security import check_email_security

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
        "subdomains": get_subdomains(request.domain),
        "geoip": get_geoip(request.domain),
        "asn": get_asn(get_geoip(request.domain).get("ip")),
        "emails": extract_emails(request.domain),
        "cms": detect_cms(request.domain),
        "waf": detect_waf(request.domain),
        "security_headers": analyze_security_headers(request.domain),
        "javascript": analyze_javascript(request.domain),
        "directories": enumerate_directories(request.domain),
        "email_security": check_email_security(request.domain)
        
    }