from datetime import datetime

from app.models.attempt import Attempt
from app.models.submission import Submission

from app.repositories.attempt_repository import AttemptRepository
from app.repositories.problem_repository import ProblemRepository
from app.repositories.submission_repository import SubmissionRepository


class PracticeService:

    def __init__(
        self,
        problem_repository: ProblemRepository,
        attempt_repository: AttemptRepository,
        submission_repository: SubmissionRepository
    ):
        self.problem_repository = problem_repository
        self.attempt_repository = attempt_repository
        self.submission_repository = submission_repository

    def start_attempt(self, problem_id: int):

        problem = self.problem_repository.get_by_id(problem_id)

        if not problem:
            raise ValueError("Problem not found")

        attempt = Attempt(
            problem_id=problem_id,
            status="DRAFT",
            started_at=datetime.utcnow()
        )

        return self.attempt_repository.create(attempt)

    def get_attempt(self, attempt_id: int):

        attempt = self.attempt_repository.get_by_id(attempt_id)

        if not attempt:
            raise ValueError("Attempt not found")

        return attempt

    def submit_attempt(
        self,
        attempt_id: int,
        submission_data: dict
    ):

        attempt = self.get_attempt(attempt_id)

        if attempt.status != "DRAFT":
            raise ValueError(
                "Only draft attempts can be submitted"
            )

        submission = Submission(
            attempt_id=attempt_id,
            submission_type="TEXT",
            **submission_data
        )

        self.submission_repository.create(submission)

        attempt.status = "SUBMITTED"
        attempt.submitted_at = datetime.utcnow()

        self.attempt_repository.update(attempt)

        return submission