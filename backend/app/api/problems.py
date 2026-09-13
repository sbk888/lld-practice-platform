from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.problem_repository import ProblemRepository

router = APIRouter(
    prefix="/api/problems",
    tags=["Problems"]
)


@router.get("/")
def get_problems(db: Session = Depends(get_db)):
    repository = ProblemRepository(db)

    problems = repository.get_all()

    return problems


@router.get("/{problem_id}")
def get_problem(
    problem_id: int,
    db: Session = Depends(get_db)
):
    repository = ProblemRepository(db)

    problem = repository.get_by_id(problem_id)

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found"
        )

    return problem