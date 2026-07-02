from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.scan import Scan

router = APIRouter(
    prefix="/api/v1/history",
    tags=["History"]
)

@router.get("/")
async def get_history():

    db: Session = SessionLocal()

    try:

        scans = db.query(Scan).order_by(Scan.id.desc()).all()

        data = []

        for scan in scans:

            data.append({
                "id": scan.id,
                "domain": scan.domain,
                "scan_type": scan.scan_type,
                "risk_score": scan.risk_score,
                "grade": scan.grade,
                "status": scan.status,
                "created_at": scan.created_at
            })

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }

    finally:
        db.close()