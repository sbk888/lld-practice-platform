from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.evaluation_repository import EvaluationRepository
from app.repositories.criterion_result_repository import CriterionResultRepository


router = APIRouter(
    prefix="/api/feedback",
    tags=["Feedback"]
)


@router.get("/{attempt_id}")
def get_feedback(
    attempt_id: int,
    db: Session = Depends(get_db)
):

    evaluation_repository = EvaluationRepository(db)
    criterion_repository = CriterionResultRepository(db)

    evaluation = evaluation_repository.get_by_attempt_id(
        attempt_id
    )

    if not evaluation:
        raise HTTPException(
            status_code=404,
            detail="Evaluation not found"
        )

    results = criterion_repository.get_by_evaluation_id(
        evaluation.id
    )

    return {
        "attempt_id": attempt_id,
        "evaluation_id": evaluation.id,
        "status": evaluation.status,
        "overall_score": evaluation.overall_score,
        "summary": evaluation.summary,
        "rubric_version": evaluation.rubric_version,
        "criteria": results
    }