# Human-in-the-Loop Agent — Test Cases

## Test 1: Essay Generation

**Input:** The benefits and risks of artificial intelligence in education.

**Expected Result:** The agent researches the topic using Tavily and generates an essay draft using Groq.

**Actual Result:** Passed. Research completed and the essay draft was generated.

## Test 2: Human Review and Revision

**Action:** Requested a revision with the feedback: "Make the conclusion stronger and explain the risks more clearly."

**Expected Result:** The agent revises the essay using the human feedback and pauses for review again.

**Actual Result:** Passed. The essay was revised and presented for another review.

## Test 3: Essay Approval

**Action:** Approved the revised essay.

**Expected Result:** The workflow resumes and finishes with the status `approved`.

**Actual Result:** Passed. The workflow finished with status `approved` after one revision.

## Test 4: Flask Application

**Action:** Opened the application, submitted an essay topic, reviewed the draft, requested a revision, and approved the essay.

**Expected Result:** The application displays the draft and supports the human review workflow.

**Actual Result:** Passed. The Flask home and review pages loaded successfully, and form submissions completed without server errors.

## Conclusion

The human-in-the-loop essay-writing workflow was implemented and tested successfully. The agent supports research, essay generation, human feedback, revision, and final approval.