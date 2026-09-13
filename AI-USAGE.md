# AI Usage

AI tools were used as development assistants throughout the project. The final decisions were reviewed and adapted based on the assignment requirements and the intended learner experience.

## 1. MVP Scope

### AI suggestion

Use a small number of LLD problems and focus on one complete practice loop instead of building a large learning platform.

### Decision

Accepted.

### Why

The assignment explicitly prioritizes a focused MVP and the learner journey. A smaller scope allowed the core flow to be implemented end-to-end.

---

## 2. Structured Submission Format

### AI suggestion

Use structured text fields for requirements, assumptions, classes, responsibilities, relationships, patterns, edge cases and trade-offs.

### Decision

Accepted.

### Why

The format provides enough evidence of LLD reasoning while keeping the prototype simpler than supporting code and diagrams at the same time.

---

## 3. Rubric-Based Evaluation

### AI suggestion

Avoid treating one reference solution as the only correct answer. Evaluate multiple design dimensions instead.

### Decision

Accepted.

### Why

LLD can have multiple valid solutions. A rubric provides more useful learning feedback than simply comparing the submission with one fixed solution.

---

## 4. Evaluator Abstraction

### AI suggestion

Separate the evaluator from the practice flow so different evaluation approaches can be introduced later.

### Decision

Accepted.

### Why

The current prototype can use a rule-based evaluator while the architecture leaves room for AI, human or hybrid evaluation later.

---

## 5. Attempt Lifecycle

### AI suggestion

Represent the attempt lifecycle using explicit states such as DRAFT, SUBMITTED, EVALUATING, COMPLETED and FAILED.

### Decision

Accepted.

### Why

Explicit states make submission and evaluation behaviour easier to understand and provide a clear place to handle evaluation failures.

## Overall Reflection

AI was mainly used for brainstorming, implementation assistance, debugging, code refinement and documentation support. Important architectural and product decisions were reviewed against the assignment requirements rather than accepting AI suggestions blindly.