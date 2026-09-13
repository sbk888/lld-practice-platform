from sqlalchemy.orm import Session

from app.models.submission import Submission


class SubmissionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, submission: Submission):
        self.db.add(submission)
        self.db.commit()
        self.db.refresh(submission)

        return submission

    def get_by_attempt_id(self, attempt_id: int):
        return (
            self.db.query(Submission)
            .filter(Submission.attempt_id == attempt_id)
            .first()
        )