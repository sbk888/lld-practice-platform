from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.problem_repository import ProblemRepository
from app.repositories.attempt_repository import AttemptRepository
from app.services.practice_service import PracticeService


router = APIRouter(
    prefix="/api/attempts",
    tags=["Attempts"]
)


@router.post("/")
def start_attempt(
    problem_id: int,
    db: Session = Depends(get_db)
):
    problem_repository = ProblemRepository(db)
    attempt_repository = AttemptRepository(db)

    service = PracticeService(
        problem_repository,
        attempt_repository
    )

    try:
        attempt = service.start_attempt(problem_id)

        return {
            "message": "Attempt started successfully",
            "attempt": attempt
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.get("/{attempt_id}")
def get_attempt(
    attempt_id: int,
    db: Session = Depends(get_db)
):
    problem_repository = ProblemRepository(db)
    attempt_repository = AttemptRepository(db)

    service = PracticeService(
        problem_repository,
        attempt_repository
    )

    try:
        return service.get_attempt(attempt_id)

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )