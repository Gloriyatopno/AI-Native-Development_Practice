# Before and After Prompt Examples

---

## 1. Learning JavaScript

### Before: Vague Prompt

```text
Explain JavaScript.
```

### Problem

The prompt is too broad. It does not specify:

* The learner's level
* What topic to explain
* How detailed the explanation should be
* The expected format

### After: Improved Prompt

```text
I am a beginner learning JavaScript.

Explain JavaScript promises in simple language.
Explain:
1. What a promise is
2. Why promises are used
3. The three states of a promise

Include two small code examples.
Use headings and bullet points.
```

### Why It Is Better

The improved prompt provides:

* **Context:** Beginner learning JavaScript
* **Task:** Explain promises
* **Specific requirements:** Three concepts and two examples
* **Output structure:** Headings and bullet points

---

## 2. Summarizing a Review

### Before: Vague Prompt

```text
Summarize this review.
```

### Problem

The prompt does not specify:

* How long the summary should be
* Which information is important
* Who the summary is for

### After: Improved Prompt

```text
Summarize the review below in at most 30 words.

Focus only on shipping and delivery information.

"""
The product arrived two days late. The packaging was damaged,
but the product itself worked well. The customer was happy with
the product quality but unhappy with the delivery delay.
"""
```

### Why It Is Better

The improved prompt specifies:

* **Task:** Summarize
* **Length:** Maximum 30 words
* **Focus:** Shipping and delivery
* **Input:** Clearly separated using delimiters

---

## 3. Extracting Specific Information

### Before: Vague Prompt

```text
Tell me about this product review.
```

### Problem

The model does not know which information is required.

### After: Improved Prompt

```text
Extract only the information related to the product's price
from the review below.

Return the answer in one sentence.

"""
The headphones cost $80. They have good sound quality and
comfortable ear cushions. Delivery took three days.
"""
```

### Why It Is Better

The improved prompt clearly defines:

* **What to extract:** Price
* **What to ignore:** Other information
* **Output format:** One sentence
* **Input:** Separated using delimiters

---

## 4. Writing a Product Description

### Before: Vague Prompt

```text
Write a description for this chair.
```

### Problem

The model does not know:

* Who the audience is
* What information to focus on
* How long the description should be
* What format to use

### After: Improved Prompt

```text
Write a product description for furniture retailers.

Focus on the materials used to construct the chair.
Keep the description under 50 words.

Return the description in HTML inside a <div> element.
```

### Why It Is Better

The improved prompt provides:

* **Audience:** Furniture retailers
* **Focus:** Materials
* **Constraint:** Maximum 50 words
* **Output format:** HTML inside a `<div>`

---

## 5. Classifying Customer Feedback

### Before: Vague Prompt

```text
Classify this feedback.
```

### Problem

The prompt does not define the categories or show the expected pattern.

### After: Improved Prompt

```text
Classify each customer comment as Positive, Negative, or Neutral.

Examples:

Input: "The delivery was very fast."
Output: Positive

Input: "The product arrived damaged."
Output: Negative

Input: "The product is available in three sizes."
Output: Neutral

Now classify:

Input: "The packaging was excellent."
Output:
```

### Why It Is Better

The improved prompt:

* Defines the possible categories
* Provides examples
* Shows the expected input/output pattern
* Gives the model a clear task

This is an example of **few-shot prompting**.

---

# Comparison Summary

| Example                | Main Improvement                                   |
| ---------------------- | -------------------------------------------------- |
| Learning JavaScript    | Added context, specific task, and output structure |
| Summarizing a Review   | Added length and topic focus                       |
| Extracting Information | Specified exactly what information to extract      |
| Product Description    | Added audience, focus, length, and format          |
| Customer Feedback      | Added categories and examples                      |

---

# General Pattern

A vague prompt can often be improved by adding:

```text
Context
+
Clear Task
+
Input / Data
+
Constraints
+
Expected Output
+
Examples (if needed)
```

## Key Lesson

A good prompt does not simply ask **"What should the AI do?"**

It also explains:

* **Who** the task is for
* **What** the AI should do
* **Which information** it should use
* **What constraints** it should follow
* **How** the final answer should be formatted

> **The more clearly we communicate the task and requirements, the more control we have over the AI's response.**
