# Testing

## 1. Testing Goal

Testing focuses on important behaviour, failure cases and edge cases in the LLD Practice Platform.

The main goal is to verify that the practice flow works correctly and that invalid operations are handled safely.

## 2. Core Behaviour Tests

### Test 1: View Problems

Expected:

The API returns the available LLD problems.

Result:

Passed.

### Test 2: Start Valid Attempt

Input:

A valid problem ID.

Expected:

A new attempt is created with DRAFT status.

Result:

Passed.

### Test 3: Invalid Problem

Input:

A problem ID that does not exist.

Expected:

The API returns an error indicating that the problem was not found.

Result:

Passed.

### Test 4: Submit Attempt

Input:

A valid DRAFT attempt with the required submission fields.

Expected:

The submission is stored and the attempt changes to SUBMITTED.

Result:

Passed.

### Test 5: Submit Non-Draft Attempt

Input:

An attempt that has already been submitted.

Expected:

The system rejects the submission because only DRAFT attempts can be submitted.

Result:

Passed.

### Test 6: Start Evaluation

Input:

A SUBMITTED attempt.

Expected:

An evaluation is created and the attempt changes to EVALUATING.

Result:

Passed.

### Test 7: Run Evaluation

Input:

A valid submitted attempt with an evaluation.

Expected:

Criterion results are generated, an overall score is calculated, and the attempt becomes COMPLETED.

Result:

Passed.

### Test 8: Retrieve Feedback

Input:

A completed attempt.

Expected:

The API returns:

- Overall score
- Evaluation status
- Summary
- Rubric version
- Criterion results

Result:

Passed.

### Test 9: Invalid Attempt

Input:

An attempt ID that does not exist.

Expected:

The API returns an appropriate not-found error.

Result:

Passed.

### Test 10: Retry Attempt

Input:

An existing attempt.

Expected:

A new attempt is created for the same problem.

The previous attempt remains in history.

Result:

Passed.

## 3. Edge Cases

The following cases were considered:

- Invalid problem ID
- Invalid attempt ID
- Submitting an already submitted attempt
- Evaluating an attempt that has not been submitted
- Missing submission
- Missing evaluation
- Evaluation failure
- Retrying an existing attempt

## 4. Manual End-to-End Test

The complete user flow was tested through the frontend:

Choose Problem
→ Start Practice
→ Fill Submission
→ Submit
→ Evaluate
→ View Feedback
→ View History
→ Try Again

The flow completed successfully.

## 5. History Verification

The history screen was checked after completing an attempt and creating a retry.

The history displayed separate attempts, confirming that retry creates a new attempt rather than overwriting the previous attempt.

## 6. API Verification

The FastAPI Swagger documentation was used to verify that the expected API routes were available.

Important routes verified include:

- Problems
- Attempts
- Submit
- Retry
- Evaluation
- Feedback

## 7. Testing Conclusion

The core MVP workflow and important failure cases were tested.

The current implementation successfully demonstrates the required practice → submit → feedback → retry workflow.
