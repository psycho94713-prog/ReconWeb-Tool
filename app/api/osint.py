from fastapi import APIRouter
from pydantic import BaseModel

from app.modules.whois_lookup import get_whois
from app.modules.dns_lookup import get_dns

router = APIRouter(prefix="/api/v1/osint", tags=["OSINT"])


class DomainRequest(BaseModel):
    domain: str


@router.post("/domain")
async def scan_domain(request: DomainRequest):
    return {
        "domain": request.domain,
        "whois": get_whois(request.domain),
        "dns": get_dns(request.domain)
    }