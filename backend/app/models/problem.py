from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String(50), nullable=False)
    requirements = Column(Text, nullable=False)
    constraints = Column(Text, nullable=True)