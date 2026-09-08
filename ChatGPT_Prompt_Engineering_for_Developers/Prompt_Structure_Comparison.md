# Prompt Structure Comparison

---

## 1. Basic Prompt vs. Structured Prompt

### Basic Prompt

```text
Explain Python functions.
```

### Structured Prompt

```text
I am a beginner learning Python.

Explain Python functions in simple language.

Include:
1. What a function is
2. Why functions are useful
3. The basic syntax
4. One simple example

Use headings and bullet points.
Keep the explanation beginner-friendly.
```

### Comparison

| Feature               | Basic Prompt  | Structured Prompt          |
| --------------------- | ------------- | -------------------------- |
| Context               | Not provided  | Beginner learning Python   |
| Task                  | General       | Clearly defined            |
| Required information  | Not specified | Four specific points       |
| Output structure      | Not specified | Headings and bullet points |
| Audience              | Unknown       | Beginner                   |
| Control over response | Low           | High                       |

### Result

The structured prompt gives the AI more information about the task, audience, content, and expected format. Therefore, it provides better control over the response.

---

# 2. Simple Summary vs. Controlled Summary

### Basic Prompt

```text
Summarize this review.
```

### Structured Prompt

```text
Summarize the review below in at most 30 words.

Focus only on shipping and delivery.

"""
The product arrived two days late. The packaging was damaged,
but the product itself worked well. The customer was happy with
the product quality but unhappy with the delivery delay.
"""
```

### Comparison

| Feature          | Basic Prompt  | Structured Prompt     |
| ---------------- | ------------- | --------------------- |
| Task             | Summarize     | Summarize             |
| Length           | Not specified | Maximum 30 words      |
| Focus            | General       | Shipping and delivery |
| Input separation | No            | Uses delimiter        |
| Output control   | Low           | Higher                |

### Result

The structured prompt is more useful when we need a summary with a specific length and topic focus.

---

# 3. Single Instruction vs. Few-Shot Prompt

### Single Instruction

```text
Classify the following comment as Positive, Negative, or Neutral:

"The delivery was excellent."
```

### Few-Shot Prompt

```text
Classify each comment as Positive, Negative, or Neutral.

Input: "The delivery was excellent."
Output: Positive

Input: "The product arrived damaged."
Output: Negative

Input: "The product is available in three colors."
Output: Neutral

Input: "The packaging was excellent."
Output:
```

### Comparison

| Feature              | Single Instruction | Few-Shot Prompt     |
| -------------------- | ------------------ | ------------------- |
| Categories           | Provided           | Provided            |
| Examples             | None               | Multiple examples   |
| Pattern demonstrated | No                 | Yes                 |
| Consistency          | May vary           | More clearly guided |

### Result

Few-shot prompting gives the model examples of the expected input-output pattern, making the desired behavior clearer.

---

# 4. Overall Comparison

A prompt can become more effective by gradually adding useful information.

```text
Basic Prompt
     ↓
Add Context
     ↓
Add Clear Instructions
     ↓
Add Constraints
     ↓
Specify Output Format
     ↓
Add Examples if Needed
```

### Example

#### Level 1 — Basic

```text
Explain SQL.
```

#### Level 2 — Add Context

```text
I am a beginner learning SQL.
Explain SQL.
```

#### Level 3 — Clear Instructions

```text
I am a beginner learning SQL.

Explain what SQL is and why it is used.
```

#### Level 4 — Add Constraints

```text
I am a beginner learning SQL.

Explain what SQL is and why it is used.
Use simple language and keep the explanation under 150 words.
```

#### Level 5 — Specify Output Format

```text
I am a beginner learning SQL.

Explain what SQL is and why it is used.
Use simple language and keep the explanation under 150 words.

Use:
- A short definition
- Three main uses
- One simple SQL example
```

---

# Key Findings

From comparing different prompt structures:

1. **Context** helps the model understand the situation and audience.
2. **Clear instructions** define exactly what needs to be done.
3. **Constraints** control aspects such as length and scope.
4. **Output formats** make responses more organized and predictable.
5. **Examples** demonstrate the desired pattern.
6. Adding relevant information to a prompt generally gives us greater control over the response.

---

## Conclusion

A basic prompt can be useful for simple tasks, but structured prompts are more effective when the task requires specific information, formatting, length, audience, or behavior.

The main lesson is:

> **A well-structured prompt gives the AI clearer instructions and provides greater control over the final response.**
