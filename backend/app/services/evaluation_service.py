from datetime import datetime

from app.models.evaluation import Evaluation
from app.models.criterion_result import CriterionResult

from app.repositories.evaluation_repository import EvaluationRepository
from app.repositories.attempt_repository import AttemptRepository
from app.repositories.submission_repository import SubmissionRepository
from app.repositories.problem_repository import ProblemRepository
from app.repositories.criterion_result_repository import CriterionResultRepository

from app.evaluators.rule_evaluator import RuleEvaluator


class EvaluationService:

    def __init__(
        self,
        evaluation_repository,
        attempt_repository,
        submission_repository,
        problem_repository,
        criterion_result_repository,
    ):
        self.evaluation_repository = evaluation_repository
        self.attempt_repository = attempt_repository
        self.submission_repository = submission_repository
        self.problem_repository = problem_repository
        self.criterion_result_repository = criterion_result_repository

    def start_evaluation(self, attempt_id: int):

        attempt = self.attempt_repository.get_by_id(attempt_id)

        if not attempt:
            raise ValueError("Attempt not found")

        if attempt.status != "SUBMITTED":
            raise ValueError(
                "Only submitted attempts can be evaluated"
            )

        attempt.status = "EVALUATING"
        self.attempt_repository.update(attempt)

        evaluation = Evaluation(
            attempt_id=attempt_id,
            status="EVALUATING",
            rubric_version="v1",
            created_at=datetime.utcnow(),
        )

        return self.evaluation_repository.create(evaluation)

    def run_evaluation(self, attempt_id: int):

        attempt = self.attempt_repository.get_by_id(attempt_id)

        if not attempt:
            raise ValueError("Attempt not found")

        evaluation = self.evaluation_repository.get_by_attempt_id(
            attempt_id
        )

        if not evaluation:
            raise ValueError("Evaluation not found")

        submission = self.submission_repository.get_by_attempt_id(
            attempt_id
        )

        if not submission:
            raise ValueError("Submission not found")

        problem = self.problem_repository.get_by_id(
            attempt.problem_id
        )

        if not problem:
            raise ValueError("Problem not found")

        try:
            evaluator = RuleEvaluator()

            result = evaluator.evaluate(
                submission,
                problem
            )

            for item in result["results"]:

                criterion_result = CriterionResult(
                    evaluation_id=evaluation.id,
                    criterion_key=item["criterion_key"],
                    score=item["score"],
                    max_score=item["max_score"],
                    evidence=item["evidence"],
                    concern=item["concern"],
                    suggestion=item["suggestion"],
                    confidence=item["confidence"],
                )

                self.criterion_result_repository.create(
                    criterion_result
                )

            evaluation.status = "COMPLETED"
            evaluation.overall_score = result["overall_score"]

            evaluation.summary = (
                "Your design has been evaluated against the "
                "LLD rubric. Review each criterion to identify "
                "strengths and areas for improvement."
            )

            evaluation.completed_at = datetime.utcnow()

            attempt.status = "COMPLETED"
            self.attempt_repository.update(attempt)

            return self.evaluation_repository.update(
                evaluation
            )

        except Exception as error:

            self.fail_evaluation(
                attempt_id,
                str(error)
            )

            raise

    def fail_evaluation(
        self,
        attempt_id: int,
        error_message: str
    ):

        evaluation = self.evaluation_repository.get_by_attempt_id(
            attempt_id
        )

        if not evaluation:
            raise ValueError("Evaluation not found")

        evaluation.status = "FAILED"
        evaluation.error_message = error_message
        evaluation.completed_at = datetime.utcnow()

        attempt = self.attempt_repository.get_by_id(
            attempt_id
        )

        if attempt:
            attempt.status = "FAILED"
            self.attempt_repository.update(attempt)

        return self.evaluation_repository.update(
            evaluation
        )

    def get_feedback(self, attempt_id: int):

        evaluation = self.evaluation_repository.get_by_attempt_id(
            attempt_id
        )

        if not evaluation:
            raise ValueError("Evaluation not found")

        criteria = (
            self.criterion_result_repository
            .get_by_evaluation_id(evaluation.id)
        )

        return {
            "attempt_id": attempt_id,
            "evaluation_id": evaluation.id,
            "status": evaluation.status,
            "overall_score": evaluation.overall_score,
            "summary": evaluation.summary,
            "rubric_version": evaluation.rubric_version,
            "criteria": criteria,
        }