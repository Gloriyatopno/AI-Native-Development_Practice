# Evaluation & Agents — Test Cases

## Evaluation Tests

### Test 1
Question: What is 2 + 2?

Expected Answer: 4

Predicted Answer: The answer is 4.

Result: PASS

### Test 2
Question: What planet is known as the Red Planet?

Expected Answer: Mars

Predicted Answer: Mars is known as the Red Planet.

Result: PASS

### Test 3
Question: What is the capital of France?

Expected Answer: Paris

Predicted Answer: The capital of France is Berlin.

Result: FAIL

### Evaluation Summary

Total examples: 3

Passed: 2

Failed: 1

Evaluation Score: 67%

The evaluation used an LLM to compare the meaning of expected and predicted answers rather than requiring exact string matching.

---

## Agent Tests

### Test 1

Question: What is 25% of 300?

Selected Tool: calculate_percentage

Tool Arguments:

```text
number = 300
percentage = 25
Final Answer: 25% of 300 is 75.

Result: PASS
```

### Test 2
```text
Question: What is today's date?

Selected Tool: get_today_date

Final Answer: 2026-10-05

Result: PASS
```