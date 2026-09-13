from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey

from app.database import Base


class CriterionResult(Base):
    __tablename__ = "criterion_results"

    id = Column(Integer, primary_key=True, index=True)

    evaluation_id = Column(
        Integer,
        ForeignKey("evaluations.id"),
        nullable=False
    )

    criterion_key = Column(
        String(100),
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    max_score = Column(
        Float,
        nullable=False
    )

    evidence = Column(
        Text,
        nullable=False
    )

    concern = Column(
        Text,
        nullable=True
    )

    suggestion = Column(
        Text,
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )