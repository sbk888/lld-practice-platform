from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.problem_repository import ProblemRepository
from app.repositories.attempt_repository import AttemptRepository
from app.repositories.submission_repository import SubmissionRepository

from app.services.practice_service import PracticeService

from app.schemas.submission import SubmissionCreate


router = APIRouter(
    prefix="/api/attempts",
    tags=["Attempts"]
)


def get_practice_service(db: Session):

    return PracticeService(
        ProblemRepository(db),
        AttemptRepository(db),
        SubmissionRepository(db)
    )


@router.post("/")
def start_attempt(
    problem_id: int,
    db: Session = Depends(get_db)
):

    service = get_practice_service(db)

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
@router.post("/{attempt_id}/retry")
def retry_attempt(
    attempt_id: int,
    db: Session = Depends(get_db)
):
    attempt_repository = AttemptRepository(db)

    old_attempt = attempt_repository.get_by_id(attempt_id)

    if not old_attempt:
        raise HTTPException(
            status_code=404,
            detail="Attempt not found"
        )

    new_attempt = PracticeService(
        ProblemRepository(db),
        AttemptRepository(db),
        SubmissionRepository(db)
    ).start_attempt(old_attempt.problem_id)

    return {
        "message": "New attempt created successfully",
        "attempt": new_attempt
    }

@router.get("/")
def get_all_attempts(
    db: Session = Depends(get_db)
):
    repository = AttemptRepository(db)
    return repository.get_all()
@router.get("/{attempt_id}")
def get_attempt(
    attempt_id: int,
    db: Session = Depends(get_db)
):

    service = get_practice_service(db)

    try:
        return service.get_attempt(attempt_id)

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.post("/{attempt_id}/submit")
def submit_attempt(
    attempt_id: int,
    submission: SubmissionCreate,
    db: Session = Depends(get_db)
):

    service = get_practice_service(db)

    try:
        result = service.submit_attempt(
            attempt_id,
            submission.model_dump()
        )

        return {
            "message": "Solution submitted successfully",
            "submission": result
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )