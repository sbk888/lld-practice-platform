from sqlalchemy.orm import Session

from app.models.attempt import Attempt


class AttemptRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, attempt: Attempt):
        self.db.add(attempt)
        self.db.commit()
        self.db.refresh(attempt)

        return attempt

    def get_by_id(self, attempt_id: int):
        return (
            self.db.query(Attempt)
            .filter(Attempt.id == attempt_id)
            .first()
        )

    def update(self, attempt: Attempt):
        self.db.commit()
        self.db.refresh(attempt)

        return attempt

    def get_by_problem(self, problem_id: int):
        return (
            self.db.query(Attempt)
            .filter(Attempt.problem_id == problem_id)
            .all()
        )
    def get_all(self):
        return (
        self.db.query(Attempt)
        .order_by(Attempt.started_at.desc())
        .all()
    )