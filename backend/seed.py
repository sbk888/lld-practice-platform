from app.database import SessionLocal
from app.models.problem import Problem


problems = [
    {
        "title": "Parking Lot",
        "description": "Design a parking lot system that manages vehicles, parking spots, and vehicle entry and exit.",
        "difficulty": "Easy",
        "requirements": """
1. The parking lot should support different vehicle types.
2. Vehicles should be assigned suitable parking spots.
3. A vehicle should be able to enter and exit.
4. The system should track available and occupied spots.
5. The design should be easy to extend for new vehicle types.
""",
        "constraints": """
Focus on classes, responsibilities, relationships, interfaces,
and extensibility. No need to implement a real payment system.
"""
    },
    {
        "title": "Vending Machine",
        "description": "Design a vending machine that allows users to select products, insert money, and purchase products.",
        "difficulty": "Easy",
        "requirements": """
1. The machine should display available products.
2. A user should be able to select a product.
3. The machine should accept money.
4. The machine should check product availability.
5. The machine should return change when required.
6. The design should handle invalid selections and insufficient money.
""",
        "constraints": """
Focus on object-oriented design, state handling,
responsibilities, and extensibility.
"""
    },
    {
        "title": "Elevator System",
        "description": "Design an elevator system that manages multiple elevators and handles requests from different floors.",
        "difficulty": "Medium",
        "requirements": """
1. The system should support multiple elevators.
2. Users should be able to request an elevator.
3. An elevator should move between floors.
4. The system should decide which elevator should handle a request.
5. The design should support future scheduling improvements.
""",
        "constraints": """
Focus on class responsibilities, abstraction,
interfaces, elevator selection, and extensibility.
"""
    },
    {
        "title": "Library Management",
        "description": "Design a library management system for managing books, members, borrowing, and returning books.",
        "difficulty": "Medium",
        "requirements": """
1. The library should maintain a collection of books.
2. Members should be able to borrow available books.
3. Members should be able to return books.
4. The system should track borrowed and available books.
5. The design should support different types of library items.
6. The system should handle unavailable books.
""",
        "constraints": """
Focus on domain modeling, encapsulation,
responsibilities, relationships, and extensibility.
"""
    }
]


def seed_database():
    db = SessionLocal()

    try:
        existing_count = db.query(Problem).count()

        if existing_count > 0:
            print("Problems already exist. Skipping seed.")
            return

        for problem_data in problems:
            problem = Problem(**problem_data)
            db.add(problem)

        db.commit()

        print("Successfully added 4 LLD problems.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()