from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)

    problem_id = Column(
        Integer,
        ForeignKey("problems.id"),
        nullable=False
    )

    status = Column(
        String(30),
        nullable=False,
        default="DRAFT"
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    submitted_at = Column(
        DateTime,
        nullable=True
    )