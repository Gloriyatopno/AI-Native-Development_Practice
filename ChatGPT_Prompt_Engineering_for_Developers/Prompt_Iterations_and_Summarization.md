# Prompt Iterations and Summarization
---

# 1. Iterative Prompt Development

Iterative prompt development is the process of repeatedly testing and improving a prompt based on the output produced by the AI.

### Process

```text
Write Prompt
     ↓
Get Output
     ↓
Identify Problems
     ↓
Improve Prompt
     ↓
Test Again
     ↓
Repeat
```

The goal is to gradually make the prompt more precise and produce a better result.

---

# 2. Prompt Iteration Example

## Iteration 1 — Basic Prompt

### Prompt

```text
Write a description for a laptop.
```

### Problem

The prompt is too general. It does not specify:

* Target audience
* Length
* Important features
* Output format

---

## Iteration 2 — Add Context

### Improved Prompt

```text
Write a product description for a laptop.
The description is for college students.
```

### Improvement

The AI now knows the target audience and can focus on features useful to students.

---

## Iteration 3 — Add Clear Instructions

### Improved Prompt

```text
Write a product description for a laptop for college students.

Focus on portability, battery life, performance, and affordability.
Keep the description under 80 words.
```

### Improvement

The prompt now provides:

* Target audience
* Specific topics
* Word limit

---

## Iteration 4 — Specify Output Format

### Final Prompt

```text
Write a product description for a laptop for college students.

Focus on:
- Portability
- Battery life
- Performance
- Affordability

Keep the description under 80 words.

Return:
1. A short product title
2. The product description
3. Three key features as bullet points
```

### Result

The final prompt provides much greater control over the response because it includes context, clear instructions, constraints, and an expected output structure.

---

# 3. Summarization

Summarization means reducing a longer text into a shorter version while keeping the important information.

A prompt can control:

* Length
* Focus
* Audience
* Output format

---

# 4. Basic Summarization

### Prompt

```text
Summarize the following review:

"""
The headphones have excellent sound quality and a comfortable design.
However, the delivery took five days and the packaging was slightly damaged.
The customer is happy with the product but disappointed with the delivery.
"""
```

### Purpose

This produces a short version of the overall review.

---

# 5. Summarization with a Length Constraint

### Prompt

```text
Summarize the following review in at most 30 words:

"""
The headphones have excellent sound quality and a comfortable design.
However, the delivery took five days and the packaging was slightly damaged.
The customer is happy with the product but disappointed with the delivery.
"""
```

### Improvement

The response is now limited to a specific length.

Length can be controlled using:

* Words
* Sentences
* Characters

---

# 6. Summarization with a Specific Focus

### Prompt

```text
Summarize the following review in at most 30 words.

Focus only on shipping and delivery:

"""
The headphones have excellent sound quality and a comfortable design.
However, the delivery took five days and the packaging was slightly damaged.
The customer is happy with the product but disappointed with the delivery.
"""
```

### Improvement

The model is instructed to prioritize information about shipping and delivery instead of summarizing the entire review.

---

# 7. Extraction Instead of Summarization

When only specific information is required, extraction can be more appropriate than summarization.

### Extraction Prompt

```text
Extract only the information related to shipping and delivery
from the following review.

Limit the response to 30 words.

"""
The headphones have excellent sound quality and a comfortable design.
However, the delivery took five days and the packaging was slightly damaged.
The customer is happy with the product but disappointed with the delivery.
"""
```

### Difference

| Summarization                | Extraction                            |
| ---------------------------- | ------------------------------------- |
| Condenses the overall text   | Returns only relevant information     |
| Can include multiple topics  | Focuses on a specific topic           |
| Useful for general summaries | Useful for topic-specific information |

---

# 8. Multiple Texts

The same summarization prompt can be applied to multiple reviews to generate consistent summaries.

### Prompt

```text
Summarize each review in at most 20 words.

Review 1:
The panda plush is soft and well-made, but delivery was slow.

Review 2:
The standing lamp looks attractive and provides good lighting.

Review 3:
The electric toothbrush works well, but the battery takes a long time to charge.

Review 4:
The blender is powerful and easy to clean.
```

### Purpose

Using the same instructions for multiple texts helps produce summaries with a consistent length and structure.

---

# 9. Key Learnings

### Iterative Prompt Development

* A prompt does not need to be perfect on the first attempt.
* Test the prompt and examine the output.
* Identify what is missing or incorrect.
* Add relevant context or instructions.
* Repeat until the output meets the requirements.

### Summarization

* Summarization can reduce long text into concise information.
* Length can be controlled using words, sentences, or characters.
* A specific topic can be provided as the focus.
* Audience and purpose can help determine what information is important.
* Extraction is useful when only specific information is required.
* The same prompt can be applied to multiple texts for consistent summaries.

---

# 10. Overall Conclusion

Improving LLM outputs requires clear instructions and continuous refinement.

The main workflow is:

```text
Initial Prompt
      ↓
Evaluate Output
      ↓
Identify Issues
      ↓
Refine Prompt
      ↓
Better Output
```

> **Good prompt engineering is an iterative process: test, evaluate, refine, and repeat.**
