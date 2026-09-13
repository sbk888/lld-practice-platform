RUBRIC = [
    {
        "key": "requirement_understanding",
        "name": "Requirement Understanding",
        "max_score": 15
    },
    {
        "key": "class_responsibilities",
        "name": "Class Responsibilities",
        "max_score": 20
    },
    {
        "key": "encapsulation_interfaces",
        "name": "Encapsulation & Interfaces",
        "max_score": 15
    },
    {
        "key": "coupling_cohesion",
        "name": "Coupling & Cohesion",
        "max_score": 15
    },
    {
        "key": "abstraction_patterns",
        "name": "Abstraction / Design Patterns",
        "max_score": 10
    },
    {
        "key": "extensibility",
        "name": "Extensibility",
        "max_score": 15
    },
    {
        "key": "edge_cases_testability",
        "name": "Edge Cases & Testability",
        "max_score": 5
    },
    {
        "key": "explanation_tradeoffs",
        "name": "Explanation & Trade-offs",
        "max_score": 5
    }
]


def get_total_score():
    return sum(item["max_score"] for item in RUBRIC)