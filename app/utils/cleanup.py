from datetime import datetime, timedelta

from app.database.database import SessionLocal
from app.models.scan import Scan


def delete_old_scans():

    db = SessionLocal()

    try:

        expire_time = datetime.utcnow() - timedelta(
            hours=24
        )

        deleted = (
            db.query(Scan)
            .filter(
                Scan.created_at < expire_time
            )
            .delete()
        )

        db.commit()

        print(
            f"Deleted old scans: {deleted}"
        )

    finally:

        db.close()