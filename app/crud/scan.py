from sqlalchemy.orm import Session

from app.models.scan import Scan


def save_scan(
    db: Session,
    domain: str,
    scan_type: str,
    risk_score: int,
    grade: str,
    status: str
):
    scan = Scan(
        domain=domain,
        scan_type=scan_type,
        risk_score=risk_score,
        grade=grade,
        status=status
    )

    db.add(scan)
    db.commit()
    db.refresh(scan)

    return scan