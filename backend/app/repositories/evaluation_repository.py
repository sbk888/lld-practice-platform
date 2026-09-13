from sqlalchemy.orm import Session

from app.models.evaluation import Evaluation


class EvaluationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, evaluation: Evaluation):
        self.db.add(evaluation)
        self.db.commit()
        self.db.refresh(evaluation)

        return evaluation

    def get_by_attempt_id(self, attempt_id: int):
        return (
            self.db.query(Evaluation)
            .filter(Evaluation.attempt_id == attempt_id)
            .first()
        )

    def update(self, evaluation: Evaluation):
        self.db.commit()
        self.db.refresh(evaluation)

        return evaluation