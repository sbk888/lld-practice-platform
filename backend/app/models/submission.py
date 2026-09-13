from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String
from datetime import datetime

from app.database import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id"),
        nullable=False,
        unique=True
    )

    submission_type = Column(
        String(30),
        nullable=False,
        default="TEXT"
    )

    requirements_understanding = Column(Text, nullable=False)
    assumptions = Column(Text, nullable=False)
    classes = Column(Text, nullable=False)
    responsibilities = Column(Text, nullable=False)
    relationships = Column(Text, nullable=False)
    patterns = Column(Text, nullable=False)
    edge_cases = Column(Text, nullable=False)
    trade_offs = Column(Text, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )