from sqlalchemy.orm import Session
from app.models.criterion_result import CriterionResult


class CriterionResultRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, result: CriterionResult):
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        return result

    def get_by_evaluation_id(self, evaluation_id: int):
        return (
            self.db.query(CriterionResult)
            .filter(CriterionResult.evaluation_id == evaluation_id)
            .all()
        )