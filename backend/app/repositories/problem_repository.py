from sqlalchemy.orm import Session

from app.models.problem import Problem


class ProblemRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Problem).all()

    def get_by_id(self, problem_id: int):
        return (
            self.db.query(Problem)
            .filter(Problem.id == problem_id)
            .first()
        )

    def create(self, problem: Problem):
        self.db.add(problem)
        self.db.commit()
        self.db.refresh(problem)

        return problem