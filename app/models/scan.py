from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)

    domain = Column(String, index=True)

    scan_type = Column(String)

    risk_score = Column(Integer)

    grade = Column(String)

    status = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)