# LLM Evaluation Test Cases

## 1. Purpose

These test cases are used to evaluate LLM responses and check whether the generated outputs are correct, complete, and consistent with the expected information.

The evaluation practice covers:

- Single-answer evaluation
- Expected vs generated answers
- Hard test cases
- Regression testing
- Rubric-based evaluation
- Expert-answer comparison

---

## 2. Single-Answer Evaluation

When there is one clear correct answer, the generated response can be compared directly with the ideal answer.

### Test Cases

| Test | Question | Ideal Answer |
|---|---|---|
| 1 | What is the capital of France? | Paris |
| 2 | What is 5 + 7? | 12 |
| 3 | What planet do humans live on? | Earth |
| 4 | What language is commonly used for web page structure? | HTML |
| 5 | What does CPU stand for? | Central Processing Unit |

### Evaluation Result

- Total test cases: 5
- Passed: 5
- Failed: 0
- Accuracy: 100%

---

## 3. Hard Test Cases

Hard test cases help identify situations where a prompt may not produce the expected output.

Examples:

### Test Case 1 — Budget Product Search

**Customer message:**

> What TVs can I buy on a budget?

**Expected behavior:**

The system should identify TV products that match the available product information.

---

### Test Case 2 — Multiple Product Categories

**Customer message:**

> Show me the SmartX ProPhone, FotoSnap DSLR Camera, and TVs.

**Expected behavior:**

The system should identify the relevant products and categories instead of returning unrelated products.

---

### Test Case 3 — Product Subset

**Customer message:**

> Which products would be useful for a videographer?

**Expected behavior:**

The system should identify relevant camera products.

---

### Test Case 4 — No Matching Product

**Customer message:**

> Do you have a hot tub time machine?

**Expected behavior:**

The system should return an empty result when no matching product exists.

---

## 4. Regression Testing

Regression testing checks whether a prompt improvement fixes difficult cases without breaking previously working cases.

### Process

1. Run the original test cases.
2. Identify a difficult or incorrect case.
3. Improve the prompt.
4. Run the difficult case again.
5. Run the previous test cases again.
6. Compare the results.

### Goal

A prompt improvement should solve the target problem while maintaining the performance of existing test cases.

---

## 5. Rubric-Based Evaluation

Some LLM responses do not have one exact correct wording.

For these cases, a rubric can be used to evaluate the response.

### Example

**Customer question:**

> What is the SmartX ProPhone price and does it support 5G?

**Available context:**

```json
{
  "product": "SmartX ProPhone",
  "price": 799,
  "features": [
    "6.5-inch OLED",
    "128GB",
    "48MP camera",
    "5G"
  ]
}
```

**Assistant response:**

> The SmartX ProPhone costs $799 and supports 5G.

### Evaluation Criteria

| Criterion | Expected |
|---|---|
| Based only on provided context | Yes |
| Contains unsupported information | No |
| Conflicts with context | No |
| Answers the customer's question | Yes |

### Evaluation Result

```text
Based on context: Y
Unsupported information: N
Conflicts with context: N
Answers question: Y
```

---

## 6. Expert-Answer Comparison

For open-ended responses, the generated answer can also be compared with an expert or ideal answer.

### Example

**Question:**

> Which product is more highly rated: SmartX ProPhone or FotoSnap DSLR Camera?

**Context:**

```json
{
  "SmartX ProPhone": {
    "rating": 4.5
  },
  "FotoSnap DSLR Camera": {
    "rating": 4.7
  }
}
```

**Expert answer:**

> The FotoSnap DSLR Camera is more highly rated, with a rating of 4.7 compared with 4.5 for the SmartX ProPhone.

**Assistant answer:**

> The FotoSnap DSLR Camera has the higher rating at 4.7, while the SmartX ProPhone has a rating of 4.5.

### Evaluation

The assistant answer is factually consistent with the expert answer and the supplied context.

**Result: A — Correct and fully supported by the context.**

---

## 7. Evaluation Methods Used

### Single Right Answer

Used when there is one expected answer.

```text
Generated Answer
       ↓
Compare with Ideal Answer
       ↓
Pass / Fail
       ↓
Calculate Accuracy
```

### No Single Right Answer

Used when multiple valid responses are possible.

```text
Question + Context
        ↓
Generated Response
        ↓
Rubric / Expert Evaluation
        ↓
Check Accuracy, Completeness,
Consistency and Context
```

---

## 8. Key Learning

LLM evaluation is important because a response that sounds correct is not necessarily correct.

Evaluation can be used to:

- Measure model performance.
- Detect incorrect responses.
- Check whether responses follow provided context.
- Identify unsupported information.
- Check whether all parts of a question are answered.
- Compare responses with ideal or expert answers.
- Test prompt improvements.
- Perform regression testing.
- Monitor system performance over time.

---

## 9. Evaluation Summary

The practical evaluation demonstrated three approaches:

1. **Single-answer evaluation** — compare generated answers with expected answers and calculate accuracy.
2. **Rubric-based evaluation** — evaluate open-ended responses against specific criteria.
3. **Expert-answer comparison** — compare generated responses with an ideal answer while focusing on factual consistency rather than exact wording.