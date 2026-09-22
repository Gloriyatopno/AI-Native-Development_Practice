# LLM Evaluation - Learning Notes

## 1. What is LLM Evaluation?

LLM evaluation is the process of testing an LLM system to determine whether its responses are correct, relevant, safe, complete, and consistent with the information provided to it.

Evaluation helps developers measure system performance and identify areas that need improvement.

---

## 2. Why Evaluation is Important

LLM responses can vary and may sometimes contain incorrect or unsupported information.

Evaluation helps developers:

- Measure response quality.
- Detect incorrect answers.
- Check whether responses follow the provided context.
- Identify unsupported information.
- Check whether all parts of a question are answered.
- Compare generated responses with expected or expert answers.
- Test prompt improvements.
- Perform regression testing.
- Monitor system performance over time.

---

# Evaluation Part I

## 3. Evaluation When There is a Single Right Answer

Some tasks have one clearly correct answer.

For example:

```text
Question:
What is the capital of France?

Expected answer:
Paris
```

The generated response can be directly compared with the ideal answer.

### Basic Process

```text
User Question
      ↓
Generate Response
      ↓
Compare with Ideal Answer
      ↓
Pass / Fail
      ↓
Calculate Accuracy
```

---

## 4. Development Test Set

A development set contains examples of user messages and their ideal answers.

It can be used to test whether the system consistently produces the expected results.

Examples include:

- Finding products within a budget.
- Finding products from a category.
- Finding multiple requested products.
- Finding products suitable for a specific purpose.
- Handling queries where no matching product exists.

---

## 5. Hard Test Cases

Normal test cases may not reveal weaknesses in a prompt.

Hard test cases are more challenging examples designed to expose problems in the system.

Examples:

- A query containing multiple products.
- A query involving multiple categories.
- A query asking for a subset of products.
- A query with ambiguous wording.
- A query for a product that does not exist.

These cases help identify where the prompt or system needs improvement.

---

## 6. Prompt Improvement

When a difficult test case produces an incorrect result, the prompt can be improved.

For example, improvements may include:

- Giving clearer instructions.
- Requiring a specific output format.
- Adding examples.
- Adding additional few-shot examples.
- Explicitly instructing the model not to include additional text.

After improving the prompt, the difficult test cases should be run again.

---

## 7. Regression Testing

Regression testing checks whether a change that fixes one problem causes another previously working case to fail.

### Process

```text
Original Test Cases
       ↓
Identify Problem
       ↓
Improve Prompt
       ↓
Test Problematic Case
       ↓
Run Previous Test Cases Again
       ↓
Compare Results
```

A good prompt improvement should solve the target problem while maintaining previous performance.

---

## 8. Measuring Accuracy

For single-answer evaluation, the generated response can be compared with the ideal answer.

A simple accuracy calculation is:

```text
Accuracy = Number of Correct Responses / Total Number of Test Cases
```

Example:

```text
Correct responses = 5
Total test cases = 5

Accuracy = 5 / 5 = 100%
```

In the practical implementation, all five single-answer tests passed.

---

# Evaluation Part II

## 9. Evaluation When There is No Single Right Answer

Some LLM tasks do not have one exact answer.

For example, a customer may ask a product-related question that can be answered correctly in different ways.

In these situations, exact string matching is not enough.

Instead, the response can be evaluated using:

- A rubric.
- An expert answer.
- The supplied context.
- Factual consistency.
- Completeness.

---

## 10. Rubric-Based Evaluation

A rubric defines specific criteria that the response must satisfy.

Example criteria:

1. Is the response based only on the provided context?
2. Does the response contain unsupported information?
3. Does the response conflict with the provided context?
4. Does the response answer the customer's question completely?

Example:

```text
Based on context: Y
Unsupported information: N
Conflicts with context: N
Answers question: Y
```

This provides a structured way to evaluate an open-ended response.

---

## 11. Expert-Answer Comparison

Another method is to compare the generated response with an expert or ideal answer.

The wording does not have to be identical.

The main goal is to determine whether the generated response is factually consistent with the expert answer and available context.

For example:

```text
Expert:
The FotoSnap DSLR Camera has a rating of 4.7.

Assistant:
The FotoSnap DSLR Camera is rated 4.7.
```

The wording is different, but the factual information is equivalent.

---

## 12. Different Evaluation Outcomes

An evaluator can classify an answer based on its relationship to the expert answer.

Possible categories include:

```text
A = Correct and fully supported
B = Correct with additional supported information
C = Partially correct or incomplete
D = Contains a factual disagreement
E = Different wording but factually equivalent
```

The exact evaluation categories can be adapted depending on the application.

---

# 13. Evaluating an LLM System Over Time

Evaluation should not only happen once.

A system can be evaluated repeatedly as prompts, models, and application logic change.

Continuous evaluation helps developers:

- Monitor performance.
- Detect regressions.
- Identify new failure cases.
- Compare improvements.
- Maintain response quality.

---

# 14. Responsible LLM Development

The course also emphasizes responsible development.

An LLM application should aim to provide responses that are:

- Safe.
- Accurate.
- Relevant.
- Appropriate in tone.
- Consistent with the available information.

User inputs and generated outputs should be evaluated when necessary to maintain system quality and safety.

---

# 15. End-to-End Evaluation Workflow

An LLM application can use an evaluation process such as:

```text
User Input
    ↓
Moderation
    ↓
Process / Chain Prompts
    ↓
Generate Response
    ↓
Check Output
    ↓
Evaluate Response
    ↓
Approve Response
        OR
Connect to Human
```

Evaluation therefore becomes part of the complete application workflow rather than being treated as a separate activity.

---

# 16. Practical Implementation

The practical implementation used the Groq API with the model:

```text
openai/gpt-oss-20b
```

The implementation demonstrated:

- Single-answer evaluation.
- Rubric-based evaluation.
- Expert-answer comparison.
- Accuracy calculation.
- Structured evaluation results.

The course examples use OpenAI API concepts, while the practical implementation uses Groq as the API provider.

---

# 17. Practical Results

### Single-Answer Evaluation

```text
Total tests: 5
Passed: 5
Failed: 0
Accuracy: 100%
```

### Rubric Evaluation

```text
Based on context: Y
Unsupported information: N
Conflicts with context: N
Answers question: Y
```

### Expert-Answer Comparison

```text
Evaluation category: A
```

The practical tests successfully demonstrated the three evaluation approaches.

---

# 18. Key Learning Outcomes

After completing this topic, I learned how to:

- Evaluate LLM responses with a single correct answer.
- Create development test cases.
- Identify hard test cases.
- Improve prompts based on evaluation results.
- Perform regression testing.
- Calculate response accuracy.
- Evaluate open-ended responses using rubrics.
- Compare generated responses with expert answers.
- Check responses for factual consistency and unsupported information.
- Monitor LLM systems over time.
- Include evaluation as part of an end-to-end LLM application.
- Build LLM applications responsibly.