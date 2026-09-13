from pydantic import BaseModel


class SubmissionCreate(BaseModel):
    requirements_understanding: str
    assumptions: str
    classes: str
    responsibilities: str
    relationships: str
    patterns: str
    edge_cases: str
    trade_offs: str