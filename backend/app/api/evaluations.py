from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.evaluation_repository import EvaluationRepository
from app.repositories.attempt_repository import AttemptRepository
from app.repositories.submission_repository import SubmissionRepository
from app.repositories.problem_repository import ProblemRepository
from app.repositories.criterion_result_repository import (
    CriterionResultRepository
)

from app.services.evaluation_service import EvaluationService


router = APIRouter(
    prefix="/api/evaluations",
    tags=["Evaluations"]
)


def get_evaluation_service(db: Session):

    return EvaluationService(
        EvaluationRepository(db),
        AttemptRepository(db),
        SubmissionRepository(db),
        ProblemRepository(db),
        CriterionResultRepository(db),
    )


@router.post("/{attempt_id}/start")
def start_evaluation(
    attempt_id: int,
    db: Session = Depends(get_db)
):

    service = get_evaluation_service(db)

    try:

        evaluation = service.start_evaluation(
            attempt_id
        )

        return {
            "message": "Evaluation started",
            "evaluation": evaluation
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.post("/{attempt_id}/run")
def run_evaluation(
    attempt_id: int,
    db: Session = Depends(get_db)
):

    service = get_evaluation_service(db)

    try:

        evaluation = service.run_evaluation(
            attempt_id
        )

        return {
            "message": "Evaluation completed",
            "evaluation": evaluation
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/{attempt_id}/feedback")
def get_feedback(
    attempt_id: int,
    db: Session = Depends(get_db)
):

    service = get_evaluation_service(db)

    try:

        return service.get_feedback(
            attempt_id
        )

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )