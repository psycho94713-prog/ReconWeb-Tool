from fastapi import APIRouter
import asyncio
from concurrent.futures import ThreadPoolExecutor

from pydantic import BaseModel

from app.modules.whois_lookup import get_whois
from app.modules.dns_lookup import get_dns
from app.modules.ssl_lookup import get_ssl_info
from app.modules.headers_lookup import get_headers
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
from app.modules.technology_detector import detect_technology
from app.modules.risk_score import calculate_risk_score

from app.database.database import SessionLocal
from app.crud.scan import save_scan

router = APIRouter(prefix="/api/v1/osint", tags=["OSINT"])


class DomainRequest(BaseModel):
    domain: str

@router.post("/domain")
async def scan_domain(request: DomainRequest):

    db = SessionLocal()

    loop = asyncio.get_running_loop()

    executor = ThreadPoolExecutor(max_workers=10)

    whois_future = loop.run_in_executor(executor, get_whois, request.domain)
    dns_future = loop.run_in_executor(executor, get_dns, request.domain)
    ssl_future = loop.run_in_executor(executor, get_ssl_info, request.domain)
    headers_future = loop.run_in_executor(executor, get_headers, request.domain)
    technology_future = loop.run_in_executor(executor, detect_technology, request.domain)

    subdomain_future = loop.run_in_executor(executor, get_subdomains, request.domain)
    ports_future = loop.run_in_executor(executor, scan_ports, request.domain)
    geoip_future = loop.run_in_executor(executor, get_geoip, request.domain)
    emails_future = loop.run_in_executor(executor, extract_emails, request.domain)
    cms_future = loop.run_in_executor(executor, detect_cms, request.domain)
    waf_future = loop.run_in_executor(executor, detect_waf, request.domain)
    security_future = loop.run_in_executor(executor, analyze_security_headers,        request.domain)
    javascript_future = loop.run_in_executor(executor, analyze_javascript, request.domain)
    directory_future = loop.run_in_executor(executor, enumerate_directories,   request.domain)
    emailsec_future = loop.run_in_executor(executor, check_email_security, request.domain)

    scan_data = {
       
        "domain": request.domain,
       
        "whois": await whois_future,
        "dns": await dns_future,
        "ssl": await ssl_future,
        "headers": await headers_future,
        "technology": await technology_future,
        "subdomains": await subdomain_future,
        "ports": await ports_future,
        "geoip": await geoip_future,
        "asn": get_asn(get_geoip(request.domain).get("ip")),
        "emails": await emails_future,
        "cms": await cms_future,
        "waf": await waf_future,
        "security_headers": await security_future,
        "javascript": await javascript_future,
        "directories": await directory_future,
        "email_security": await emailsec_future, 
    }
    
    scan_data["asn"] = get_asn(scan_data["geoip"].get("ip"))
    scan_data["risk_score"] = calculate_risk_score(scan_data)

    save_scan(
        db=db,
        domain=request.domain,
        scan_type="full",
        risk_score=scan_data["risk_score"]["score"],
        grade=scan_data["risk_score"]["grade"],
        status="Completed"
    )    
   
    executor.shutdown(wait=False)

    return scan_data