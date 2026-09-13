 # LLD Practice Platform - Design Note

## 1. Project Overview

### Problem

Low-Level Design (LLD) is an important software engineering skill, but learners often struggle to get meaningful feedback on their designs.

Existing learning resources provide problems, tutorials, design patterns, UML diagrams, and reference solutions. However, learners need a simple practice loop where they can:

- Choose an LLD problem
- Think about the design
- Submit their solution
- Receive structured feedback
- Review their weaknesses
- Try the problem again
- Track their previous attempts

### Proposed Solution

**LLD Practice Platform** is a focused practice platform where learners solve LLD problems, submit their design, receive explainable rubric-based feedback, and improve through repeated attempts.

The MVP focuses on the learning loop rather than building a large-scale coding or interview platform.

### Core Product Loop

```text
Choose Problem
      ↓
Think / Design
      ↓
Submit
      ↓
Get Feedback
      ↓
Review
      ↓
Improve
      ↓
Try Again
2. MVP Scope

The MVP contains a small set of LLD problems and provides a complete practice-to-feedback workflow.

Problems

The initial problem set contains four problems:

Problem	Difficulty
Parking Lot	Easy
Vending Machine	Easy
Elevator System	Medium
Library Management	Medium

The problem set is intentionally small so that the MVP can focus on the quality of the practice and feedback experience.
Submission Format

The learner submits a structured text-based design.

Each submission contains eight sections:

Requirements Understanding
Assumptions
Classes
Responsibilities
Relationships
Design Principles / Patterns
Edge Cases
Trade-offs

This format provides enough information to evaluate the learner's LLD reasoning without requiring a complete code implementation or diagram editor in the MVP.
3. User Flow

The main user journey is:
Dashboard
   ↓
Choose Problem
   ↓
Problem Details
   ↓
Start Attempt
   ↓
Practice / Design
   ↓
Submit Solution
   ↓
Evaluation
   ↓
Feedback
   ↓
History
   ↓
Retry
   ↓
New Attempt
Step 1 - Choose Problem

The learner views the available LLD problems.

Each problem provides:

Title
Difficulty
Problem description
Requirements
Constraints
Step 2 - Start Attempt

When the learner selects a problem, a new attempt is created.

The attempt starts with:

DRAFT

The attempt receives its own unique ID.

Step 3 - Think and Design

The learner works on the problem and fills in the structured design fields.

The learner explains:

What the requirements are
What assumptions were made
Which classes are required
What each class is responsible for
How classes interact
Which design principles or patterns are used
Possible edge cases
Design trade-offs
Step 4 - Submit

When the learner submits the solution:

DRAFT → SUBMITTED

The submission is saved before evaluation begins.

This ensures that the learner's work is preserved even if evaluation later fails.

Step 5 - Evaluation

The submitted solution is evaluated against the LLD rubric.

The evaluation lifecycle is:

SUBMITTED
    ↓
EVALUATING
    ↓
COMPLETED

If something goes wrong during evaluation:

EVALUATING
    ↓
FAILED
Step 6 - Feedback

The learner receives:

Overall score
Criterion-wise scores
Evidence from the submission
Concerns
Suggestions for improvement
Confidence value
Summary feedback

The feedback is designed to explain why a score was given instead of showing only a final number.

Step 7 - Review

The learner can review the feedback and identify weak areas in the design.

Step 8 - Try Again

The learner can retry the problem.

Retrying creates a new attempt instead of overwriting the previous attempt.

This allows the learner to compare their progress across attempts.

4. Attempt Lifecycle

An attempt represents one complete practice session for a problem.

The attempt can move through the following states:

DRAFT
  ↓
SUBMITTED
  ↓
EVALUATING
  ↓
COMPLETED

A failure can result in:

EVALUATING
  ↓
FAILED
Meaning of Each State
DRAFT

The learner has started the problem but has not submitted the solution.

SUBMITTED

The learner has submitted the solution and it is ready for evaluation.

EVALUATING

The evaluation process is running.

COMPLETED

Evaluation finished successfully and feedback is available.

FAILED

The evaluation process encountered an error.

5. Evaluation Rubric

The MVP uses a structured 100-point rubric.

Criterion	Maximum Score
Requirement Understanding	15
Class Responsibilities	20
Encapsulation & Interfaces	15
Coupling & Cohesion	15
Abstraction / Design Patterns	10
Extensibility	15
Edge Cases & Testability	5
Explanation & Trade-offs	5
Total	100
Why This Rubric?

LLD does not have only one correct design.

Different designs can be valid depending on:

Requirements
Assumptions
Constraints
Expected future changes
Trade-offs

Therefore, the platform evaluates important design qualities instead of comparing the submission against only one reference solution.

6. Feedback Model

Each evaluation criterion produces structured feedback.

A criterion result contains:

Criterion
Score
Maximum Score
Evidence
Concern
Suggestion
Confidence
Example
Criterion:
Class Responsibilities

Score:
14 / 20

Evidence:
The submission separates the parking lot,
floor and vehicle responsibilities.

Concern:
Some responsibilities are still concentrated
inside the parking lot class.

Suggestion:
Consider moving vehicle allocation logic into
a dedicated service or strategy.

Confidence:
0.85

This makes the feedback more actionable than simply saying:

Score: 70/100
7. Domain Model

The core domain contains the following concepts:

Problem
   │
   └── Attempt
          │
          └── Submission
                  │
                  └── Evaluation
                          │
                          └── CriterionResult
Problem

Represents an LLD problem available for practice.

Responsibilities:

Store problem information
Store requirements
Store constraints
Define difficulty
Provide the problem statement

Main attributes:

id
title
description
difficulty
requirements
constraints
Attempt

Represents one learner's practice session for a problem.

Responsibilities:

Track the selected problem
Track attempt status
Track start time
Track submission time
Represent the lifecycle of the attempt

Main attributes:

id
problem_id
status
started_at
submitted_at

The Attempt owns the lifecycle rather than the UI.

Submission

Represents the learner's submitted solution.

The MVP uses a text submission.

Main attributes:

id
attempt_id
submission_type

requirements_understanding
assumptions
classes
responsibilities
relationships
patterns
edge_cases
trade_offs

created_at

The submission concept is kept separate from Attempt so future submission formats can be added.

Possible future formats:

TextSubmission
CodeSubmission
DiagramSubmission
Evaluation

Represents the result of evaluating a submission.

Responsibilities:

Store evaluation status
Store overall score
Store feedback summary
Track rubric version
Track evaluation timestamps
Store evaluation errors when required

Main attributes:

id
attempt_id
status
overall_score
summary
error_message
rubric_version
created_at
completed_at
CriterionResult

Represents the result for one rubric criterion.

Main attributes:

id
evaluation_id
criterion_key
score
max_score
evidence
concern
suggestion
confidence

This allows the system to provide detailed feedback instead of only an overall score.

8. Core Domain Responsibilities

The platform follows clear responsibilities between domain objects.

Problem
→ Defines what the learner has to solve.

Attempt
→ Owns the practice lifecycle.

Submission
→ Represents what the learner submitted.

Evaluation
→ Represents the evaluation result.

CriterionResult
→ Represents detailed feedback for one rubric criterion.

This separation prevents one class from becoming responsible for the entire workflow.

9. Evaluation Design
Evaluator Abstraction

The evaluator is represented using an abstraction:

Evaluator
    ↓
evaluate(submission, problem)

The purpose is to avoid tightly coupling the application to one evaluation approach.

The current MVP uses a deterministic rule-based evaluator.

BaseEvaluator
      ↓
RuleEvaluator
Current Evaluator

The MVP uses RuleEvaluator.

Its purpose is to provide a working and predictable evaluation mechanism without depending on an external AI service.

This makes the prototype:

Easier to test
Easier to debug
Predictable
Suitable for a 2-day MVP
Future Evaluators

The evaluator abstraction allows future implementations such as:

RuleEvaluator
AI / LLM Evaluator
HumanEvaluator
HybridEvaluator

The rest of the application should not need major changes when the evaluator implementation changes.

10. Deterministic Evaluation vs LLM Evaluation

LLD solutions can have multiple valid approaches.

A purely deterministic evaluator can reliably check structured evidence and predefined rules, but it may not fully understand complex design reasoning.

An LLM-based evaluator can provide richer qualitative feedback, but introduces challenges such as:

Non-deterministic results
Higher cost
Latency
Prompt quality
Evaluation consistency
Need for validation

Therefore, the MVP starts with deterministic evaluation.

A future version can introduce AI evaluation behind the same evaluator abstraction.

A possible future architecture is:

Submission
    ↓
Evaluation Service
    ↓
Evaluator Interface
    ├── RuleEvaluator
    ├── AIEvaluator
    ├── HumanEvaluator
    └── HybridEvaluator
11. Architecture

The application uses a simple monolithic architecture.

┌─────────────────────────────┐
│       Next.js Frontend      │
│        TypeScript UI        │
└──────────────┬──────────────┘
               │ HTTP
               ↓
┌─────────────────────────────┐
│       FastAPI Backend       │
│                             │
│ API Layer                   │
│      ↓                      │
│ Service Layer               │
│      ↓                      │
│ Repository Layer            │
│      ↓                      │
│ SQLite Database             │
└─────────────────────────────┘
Frontend

Technology:

Next.js
TypeScript

Responsibilities:

Display problems
Start attempts
Collect submissions
Display feedback
Display attempt history
Provide retry flow
Backend

Technology:

FastAPI
Python

Responsibilities:

Expose REST APIs
Manage attempts
Save submissions
Start evaluations
Generate feedback
Manage history
Database

Technology:

SQLite

SQLite is sufficient for the MVP because the application is a small prototype.

A production version could move to PostgreSQL or another production database.

12. Backend Structure
backend/
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── domain/
│   │   ├── problem.py
│   │   ├── attempt.py
│   │   ├── submission.py
│   │   ├── evaluation.py
│   │   ├── evaluator.py
│   │   └── rubric.py
│   │
│   ├── models/
│   │   ├── problem.py
│   │   ├── attempt.py
│   │   ├── submission.py
│   │   ├── evaluation.py
│   │   └── criterion_result.py
│   │
│   ├── repositories/
│   │   ├── problem_repository.py
│   │   ├── attempt_repository.py
│   │   ├── submission_repository.py
│   │   ├── evaluation_repository.py
│   │   └── criterion_result_repository.py
│   │
│   ├── services/
│   │   ├── practice_service.py
│   │   └── evaluation_service.py
│   │
│   ├── evaluators/
│   │   ├── base.py
│   │   └── rule_evaluator.py
│   │
│   ├── schemas/
│   │   └── submission.py
│   │
│   └── api/
│       ├── problems.py
│       ├── attempts.py
│       └── evaluations.py
│
├── tests/
├── seed.py
├── requirements.txt
└── lld_platform.db
13. Repository Layer

Repositories isolate database access from business logic.

ProblemRepository

Responsible for:

Getting all problems
Getting a problem by ID
Creating problems
AttemptRepository

Responsible for:

Creating attempts
Finding attempts
Updating attempts
Getting attempts for a problem
Getting all attempts
SubmissionRepository

Responsible for:

Creating submissions
Finding submissions by attempt
EvaluationRepository

Responsible for:

Creating evaluations
Finding evaluations
Updating evaluations
CriterionResultRepository

Responsible for:

Creating criterion results
Getting criterion results for an evaluation

This separation makes the application easier to test and extend.

14. Service Layer

The service layer contains application-level business logic.

PracticeService

Responsible for the practice workflow.

Main responsibilities:

Start Attempt
Get Attempt
Submit Attempt

Important rule:

Only DRAFT attempts can be submitted.

When a submission is created:

Submission is saved
        ↓
Attempt becomes SUBMITTED
        ↓
submitted_at is recorded
EvaluationService

Responsible for the evaluation workflow.

Main responsibilities:

Start Evaluation
Run Evaluation
Fail Evaluation
Get Feedback

Evaluation flow:

Submitted Attempt
       ↓
Start Evaluation
       ↓
EVALUATING
       ↓
RuleEvaluator
       ↓
Criterion Results
       ↓
Overall Score
       ↓
COMPLETED

If evaluation fails:

Evaluation → FAILED
Attempt → FAILED
15. API Layer

The FastAPI application exposes endpoints for the core workflow.

Problems
GET /api/problems/
GET /api/problems/{problem_id}
Attempts
POST /api/attempts/
GET /api/attempts/
GET /api/attempts/{attempt_id}
POST /api/attempts/{attempt_id}/submit
POST /api/attempts/{attempt_id}/retry
Evaluations

The evaluation APIs handle starting evaluation, running evaluation, and retrieving feedback.

The API layer should remain thin and delegate business rules to services.

16. Database Design

The main database tables are:

problems
attempts
submissions
evaluations
criterion_results

Relationships:

Problem
  1
  │
  │
  N
Attempt
  1
  │
  │
  1
Submission


Attempt
  1
  │
  │
  1
Evaluation
  1
  │
  │
  N
CriterionResult

The one-to-one relationship between Attempt and Submission ensures that each attempt has one current submission in the MVP.

The one-to-one relationship between Attempt and Evaluation represents the evaluation associated with that attempt.

17. Frontend Screens

The MVP contains five major screens.

Dashboard

Shows:

Platform introduction
Available problems
Navigation to practice and history
Problem Details

Shows:

Problem title
Difficulty
Description
Requirements
Constraints
Start Attempt action
Practice

Provides the eight structured submission fields.

The learner can enter their design and submit it.

Feedback

Shows:

Overall score
Evaluation summary
Criterion-wise results
Evidence
Concerns
Suggestions
Confidence
Retry action
History

Shows previous attempts.

Example:

Attempt #2 → DRAFT
Attempt #1 → COMPLETED

Each attempt remains separate so progress can be tracked.

18. Retry Design

Retry is intentionally implemented by creating a new attempt.

Completed Attempt #1
        ↓
      Retry
        ↓
New Attempt #2
        ↓
      DRAFT

The previous attempt is not overwritten.

This preserves learning history and allows future features such as:

Score comparison
Improvement tracking
Weakness tracking
Progress charts
Attempt comparison
19. Handling Evaluation Failures

Evaluation can potentially fail because of:

Internal evaluator errors
Future external AI service failures
Network failures
Timeouts
Unexpected submission data

The system therefore stores evaluation status.

EVALUATING
COMPLETED
FAILED

When an error occurs:

Evaluation.status = FAILED
Evaluation.error_message = error
Attempt.status = FAILED

This makes failures visible instead of leaving the attempt permanently stuck.

20. Slow Evaluation

The current MVP performs evaluation directly for simplicity.

For a production system, slow evaluation should be moved to an asynchronous background process.

Possible future flow:

Submit
  ↓
Save Submission
  ↓
Queue Evaluation Job
  ↓
Return Immediately
  ↓
Background Worker
  ↓
Evaluate
  ↓
Save Feedback

The frontend can then poll for status or use a real-time update mechanism.

This keeps slow evaluation from blocking the user experience.

21. Extensibility

The design intentionally keeps important extension points.

Submission Formats

Current:

TextSubmission

Future:

CodeSubmission
DiagramSubmission
Evaluators

Current:

RuleEvaluator

Future:

AIEvaluator
HumanEvaluator
HybridEvaluator
Database

Current:

SQLite

Future:

PostgreSQL
Evaluation Processing

Current:

Synchronous

Future:

Background Job / Queue

This allows the MVP to remain simple while supporting future growth.

22. Design Trade-offs
Structured Text vs Code Editor
Chosen

Structured text.

Reason

It allows the learner to focus on LLD thinking rather than implementation syntax.

It also makes the MVP faster to build and easier to evaluate.

Future

A code editor can be added later for code-based LLD submissions.

Rule-Based Evaluation vs LLM
Chosen

Rule-based evaluation for the MVP.

Reason

It is deterministic, predictable, inexpensive, and easy to test.

Trade-off

It may not understand sophisticated design reasoning as deeply as an LLM.

Future

Add an LLM evaluator behind the evaluator abstraction.

SQLite vs PostgreSQL
Chosen

SQLite.

Reason

The MVP is a small prototype and does not require a production database.

Future

Move to PostgreSQL when deployment and concurrent usage require it.

Monolith vs Microservices
Chosen

Simple monolith.

Reason

The assignment is focused on LLD and product thinking rather than distributed infrastructure.

A monolith reduces unnecessary complexity and allows faster iteration.

23. Important Engineering Decisions
1. Separate Attempt and Submission

An attempt represents the practice session, while the submission represents the actual answer.

This keeps responsibilities clear.

2. Separate Evaluation and CriterionResult

Evaluation stores the overall result, while CriterionResult stores detailed feedback.

This makes the feedback model extensible.

3. Evaluator Abstraction

The application depends on an evaluator abstraction rather than directly depending on one evaluator implementation.

This makes future AI or human evaluation possible.

4. Rubric Versioning

The Evaluation stores:

rubric_version = v1

This is important because the rubric may change in future versions.

Old evaluations can therefore remain associated with the rubric version that was used to evaluate them.

5. Retry Creates a New Attempt

Previous work is preserved and improvement can be measured across attempts.

24. Testing Strategy

The platform should test both successful workflows and failure cases.

Core Tests
Problem
Fetch all problems
Fetch a problem by ID
Handle invalid problem ID
Attempt
Start an attempt
Get an attempt
Reject invalid problem
Submit a draft attempt
Reject submitting a non-draft attempt
Submission
Save a valid submission
Reject incomplete submission data
Prevent duplicate submission for the same attempt
Evaluation
Start evaluation for a submitted attempt
Reject evaluation for a draft attempt
Generate criterion results
Calculate overall score
Mark evaluation as completed
Handle evaluator failure
Mark failed evaluations correctly
Retry
Retry a completed attempt
Create a new attempt
Preserve the previous attempt
History
Return attempts in descending order
Show different attempts separately
25. Edge Cases

The application considers the following edge cases:

Invalid problem ID
Invalid attempt ID
Submitting an already submitted attempt
Evaluating an unsaved submission
Missing submission fields
Evaluator failure
Duplicate evaluation
Retrying an invalid attempt
Empty design fields

These cases are important because a working prototype should handle incorrect actions predictably instead of silently failing.

26. Security and Reliability Considerations

The MVP is a local prototype, but the design considers basic reliability.

Important considerations for a future production version include:

User authentication
Authorization
Input validation
Rate limiting
Secure AI API handling
Database backups
Evaluation timeout handling
Logging
Error monitoring
Abuse prevention

These are intentionally outside the MVP scope.

27. Future Improvements

Possible future improvements include:

AI-Powered Evaluation

Use an LLM to evaluate design reasoning and provide richer feedback.

Diagram Submission

Allow learners to submit UML or class diagrams.

Code Submission

Allow learners to implement their LLD solution in a supported programming language.

Attempt Comparison

Compare two attempts and show:

Previous Score
Current Score
Improved Criteria
Weak Criteria
Progress Dashboard

Track:

Problems solved
Average score
Strongest criteria
Weakest criteria
Improvement over time
Personalized Practice

Recommend problems based on previous weaknesses.

Human Review

Allow mentors or interviewers to review submissions.

28. Why This MVP

The MVP deliberately avoids trying to build a complete coding-interview platform.

The goal is to validate one important learning loop:

Practice
   ↓
Submit
   ↓
Receive Explainable Feedback
   ↓
Review Weaknesses
   ↓
Improve
   ↓
Try Again

A small, complete workflow is more useful for validating the product idea than a large collection of incomplete features.

29. Summary

The architecture is intentionally simple for the MVP while keeping clear extension points for future improvements.

The core product loop is:

Practice
↓
Submit
↓
Get Explainable Feedback
↓
Review Weaknesses
↓
Improve
↓
Try Again

This makes repeated practice and improvement the central purpose of the platform.
