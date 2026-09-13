from app.domain.rubric import RUBRIC
from app.evaluators.base import BaseEvaluator


class RuleEvaluator(BaseEvaluator):

    def evaluate(self, submission, problem):

        results = []

        fields = {
            "requirement_understanding": submission.requirements_understanding,
            "class_responsibilities": submission.responsibilities,
            "encapsulation_interfaces": submission.classes,
            "coupling_cohesion": submission.relationships,
            "abstraction_patterns": submission.patterns,
            "extensibility": submission.trade_offs,
            "edge_cases_testability": submission.edge_cases,
            "explanation_tradeoffs": submission.trade_offs,
        }

        for criterion in RUBRIC:

            key = criterion["key"]
            max_score = criterion["max_score"]
            content = fields.get(key, "")

            if content and len(content.strip()) >= 20:
                score = max_score
                evidence = "The submission provides relevant information for this criterion."
                concern = ""
                suggestion = "Continue refining this part of the design."
                confidence = 0.85
            else:
                score = max_score * 0.5
                evidence = "The submission contains limited information for this criterion."
                concern = "The explanation is too brief."
                suggestion = "Provide more specific design reasoning and examples."
                confidence = 0.75

            results.append({
                "criterion_key": key,
                "score": score,
                "max_score": max_score,
                "evidence": evidence,
                "concern": concern,
                "suggestion": suggestion,
                "confidence": confidence
            })

        overall_score = sum(
            result["score"] for result in results
        )

        return {
            "overall_score": overall_score,
            "results": results
        }