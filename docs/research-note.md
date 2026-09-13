# LLD Practice Platform - Research Note

## 1. Problem Understanding

Low-Level Design (LLD) is an important software engineering skill because it focuses on how a system is broken into classes, objects, interfaces, responsibilities, relationships, and behaviours.

However, practising LLD is different from practising programming problems.

In a typical programming problem, the learner can run the code against test cases and immediately know whether the implementation works. In LLD, there may be multiple valid designs for the same problem. Two learners may create very different class structures and still produce reasonable solutions.

This creates an important learning problem:

> A learner can complete an LLD problem but still be unsure whether the design is actually good.

The assignment itself highlights this difficulty with examples such as Parking Lot, Elevator, and Vending Machine problems. The main challenge is not simply providing problems, but helping learners understand how their design can improve. :contentReference[oaicite:1]{index=1}

The learner therefore needs a practice experience that supports:

- Understanding the requirements
- Making assumptions
- Identifying classes
- Assigning clear responsibilities
- Defining relationships
- Thinking about abstractions and design patterns
- Considering edge cases
- Explaining trade-offs
- Receiving useful feedback
- Trying the problem again

The important learning loop is:

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
Try Again
2. How LLD Practice Currently Works

Research into common LLD learning approaches shows that learners generally use a combination of:

LLD tutorials and articles
Interview preparation websites
GitHub repositories
Community discussions
Reference solutions
Design pattern resources
Coding/interview practice platforms

These approaches are useful for learning concepts and finding problems, but the learner still has to judge their own design.

A typical process is:

Find LLD Problem
      ↓
Study Requirements
      ↓
Create Classes / Relationships
      ↓
Compare With Examples
      ↓
Decide Whether Design Is Good

The difficult part is the final step.

A reference solution can show one possible design, but it does not necessarily mean that every different design is wrong.

Therefore, the main opportunity is not simply to create another collection of LLD questions.

The opportunity is to create a repeatable practice and feedback loop.

3. Existing Approaches and Tools Researched
3.1 LLD Learning Articles and Interview Resources

LLD learning resources explain concepts such as:

Object-oriented design
Classes and objects
Interfaces
SOLID principles
Design patterns
Relationships
Responsibilities
Extensibility

These resources are useful for learning the fundamentals and understanding how to approach common LLD questions.

However, they are primarily learning/reference resources.

The learner still needs to create a solution and determine how strong that solution is.

Observation

Good for:

Learning concepts
Understanding patterns
Studying example problems
Preparing for interviews

Limitation:

Limited support for repeated personal practice and structured feedback.
3.2 GitHub LLD Repositories

GitHub contains repositories dedicated to Low-Level Design and Object-Oriented Design.

These repositories commonly provide:

LLD questions
UML diagrams
SOLID principles
Design patterns
Example implementations
Common problems such as Parking Lot and Vending Machine

They are useful as reference material and provide a large amount of content.

Observation

Good for:

Finding many practice problems
Studying implementations
Exploring different design patterns
Comparing design approaches

Limitation:

The learner usually has to evaluate their own solution manually.
There is no consistent learner feedback loop across attempts.
3.3 LLD Practice / Assessment Platforms

Some newer platforms provide more interactive LLD practice.

For example, LLD Arena provides multiple LLD problems and supports features such as code-based practice, UML-oriented learning, progression, and AI-based evaluation.

This shows that there is value in combining LLD practice with automated feedback.

Observation

Good for:

Interactive practice
Larger problem sets
More advanced assessment
Automated evaluation

Limitation for this MVP:

A smaller and simpler product can focus specifically on the learning loop of submitting a design, receiving explainable feedback, reviewing weaknesses, and retrying.

The goal is not to compete with a large platform feature-for-feature, but to validate a focused practice experience.

4. Key Research Findings

The research and assignment guidance lead to several important findings.

Finding 1 - LLD Has Multiple Valid Solutions

LLD cannot always be evaluated using one reference answer.

For example, two solutions to a Parking Lot problem may use different class structures while both being reasonable.

Therefore:

One Reference Solution
        ≠
Only Correct Solution

Evaluation should instead consider design qualities such as:

Requirement understanding
Class responsibilities
Coupling
Cohesion
Encapsulation
Interfaces
Abstraction
Extensibility
Edge cases
Testability
Explanation quality

These dimensions are also specifically suggested in the assignment guide.

5. Finding 2 - Feedback Must Explain the Score

A simple score such as:

Score: 72 / 100

does not tell the learner what to improve.

Useful feedback should connect the score to evidence from the learner's design.

A better feedback structure is:

Criterion
    ↓
Score
    ↓
Evidence
    ↓
Concern
    ↓
Suggestion
    ↓
Confidence

For example:

Criterion:
Class Responsibilities

Score:
14 / 20

Evidence:
The solution separates vehicle and parking
responsibilities.

Concern:
Some allocation logic remains inside the
main parking lot class.

Suggestion:
Move allocation behaviour into a separate
strategy or service.

This makes feedback actionable.

The assignment guide also recommends structured feedback in the form:

criterion → score → evidence → concern → suggestion → confidence

rather than asking an evaluator an unrestricted question such as whether a design is good.

6. Finding 3 - A Structured Submission Is Enough for the MVP

LLD can be represented through different formats:

Format	What it provides
Text	Requirements, assumptions, classes, responsibilities and reasoning
Code	Concrete implementation, interfaces, coupling and testability
Diagram	Relationships, structure and abstraction
Combined	More evidence but more implementation effort

For a two-day prototype, supporting every format would add unnecessary complexity.

The assignment itself suggests selecting the smallest format that provides enough evidence of design quality.

Therefore, the MVP uses a structured text submission.

The learner provides:

Requirements Understanding
Assumptions
Classes
Responsibilities
Relationships
Design Principles / Patterns
Edge Cases
Trade-offs

This gives the evaluator enough information to judge the learner's LLD reasoning.

7. Finding 4 - Deterministic Checks and AI Should Have Different Roles

Not every part of LLD evaluation requires AI.

Some checks can be deterministic:

Required fields
Submission structure
Submission status
Duplicate handling
Known business rules
State transitions

Other areas involve more judgement:

Quality of class responsibilities
Design trade-offs
SOLID analysis
Abstraction quality
Improvement suggestions
Explanation analysis

The assignment guide also recommends separating deterministic checks from judgement-heavy evaluation.

Therefore, the platform should not depend entirely on an LLM.

For the MVP, a deterministic evaluator is used first because it is easier to test and keeps the prototype predictable.

An AI evaluator can later be added behind the same evaluator abstraction.

8. Finding 5 - Attempts and Feedback Should Be Preserved

The platform should support improvement rather than one-time solving.

If a learner retries a problem, the previous attempt should not be overwritten.

Instead:

Attempt #1
    ↓
Feedback
    ↓
Retry
    ↓
Attempt #2
    ↓
New Feedback

This allows the learner to see whether their design improves over time.

The assignment explicitly requires history so that the product supports improvement rather than only one-time solving.

9. Key Product Gap

The main gap identified is the lack of a simple, focused loop connecting:

Practice
   ↓
Submission
   ↓
Explainable Feedback
   ↓
Review
   ↓
Retry
   ↓
Improvement

Many existing resources are strong at providing:

Problems
+
Tutorials
+
Reference Solutions

But the learner still has to connect these resources into a personal improvement process.

The proposed platform focuses on making that process the product itself.

10. Proposed Product Direction

Based on the research, the product will be a focused LLD practice platform rather than a full LMS or large assessment system.

The MVP will provide:

Problems

A small set of LLD problems:

Parking Lot
Vending Machine
Elevator System
Library Management
Practice

A structured form where learners explain their design.

Submission

The platform saves the learner's solution and tracks its status.

Evaluation

The solution is evaluated against a fixed rubric.

Feedback

The learner receives criterion-wise feedback containing:

Score
Evidence
Concern
Suggestion
Confidence
History

Previous attempts are stored.

Retry

A learner can retry a completed problem through a new attempt.

11. Focused MVP

The MVP deliberately stays small.

4 Problems
     +
1 Structured Submission Format
     +
1 Evaluation Flow
     +
Rubric-Based Feedback
     +
Attempt History
     +
Retry

This follows the assignment's recommendation to build a focused two-day MVP instead of trying to support every possible feature.

The platform will use a simple monolithic architecture because the assignment is primarily an LLD/domain-design exercise and explicitly states that a simple monolith is acceptable.

12. Product Direction and Differentiation

The platform is not intended to compete with existing LLD resources by simply offering more problems.

Instead, its focus is:

Practice → Explainable Feedback → Review → Retry

The product differentiates through the learning loop rather than through the size of its problem library.

The important product goal is to help the learner answer:

"What is weak in my design,
and what should I improve in my next attempt?"

rather than only:

"What is the reference solution?"
13. Future Direction

The MVP can later evolve without changing the core practice flow.

Possible extensions include:

AI/LLM-based evaluation
Code submissions
UML/class diagram submissions
Human review
Hybrid evaluation
Attempt comparison
Progress tracking
Personalized problem recommendations

The domain model should therefore keep submission and evaluator behaviour replaceable.

For example:

Submission
   ├── TextSubmission
   ├── CodeSubmission
   └── DiagramSubmission

and:

Evaluator
   ├── RuleEvaluator
   ├── AIEvaluator
   ├── HumanEvaluator
   └── HybridEvaluator

This supports the assignment's change tests: adding another submission format or another evaluation approach should not require rewriting the entire practice flow.

14. Conclusion

The research suggests that the main challenge in LLD practice is not finding another problem to solve.

The bigger challenge is understanding whether the learner's design is reasonable and knowing how to improve it.

Therefore, the proposed LLD Practice Platform focuses on a small but complete learning loop:

Choose Problem
      ↓
Think / Design
      ↓
Submit
      ↓
Get Explainable Feedback
      ↓
Review Weaknesses
      ↓
Try Again

The MVP keeps the implementation intentionally simple while making the domain model and evaluation approach extensible.

The main design principle is:

Solve one clear learner problem well, then make the solution easy to evolve.

This aligns with the assignment's final guidance to prioritise a working end-to-end prototype, clean domain boundaries, useful feedback, thoughtful AI usage, and clear trade-offs rather than unnecessary technical complexity.
