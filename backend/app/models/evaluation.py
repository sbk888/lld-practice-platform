from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String, Float
from datetime import datetime

from app.database import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id"),
        nullable=False,
        unique=True
    )

    status = Column(
        String(30),
        nullable=False,
        default="EVALUATING"
    )

    overall_score = Column(
        Float,
        nullable=True
    )

    summary = Column(
        Text,
        nullable=True
    )

    error_message = Column(
        Text,
        nullable=True
    )

    rubric_version = Column(
        String(20),
        nullable=False,
        default="v1"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )