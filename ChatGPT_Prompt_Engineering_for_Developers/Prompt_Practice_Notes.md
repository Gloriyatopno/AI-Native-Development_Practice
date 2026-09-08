# Prompt Engineering Practice Notes

---

## 1. What is Prompt Engineering?

Prompt engineering is the process of designing and refining prompts to get useful, accurate, and consistent responses from an AI model.

A good prompt gives the model clear instructions, sufficient context, and information about the expected output.

---

## 2. Principles of Effective Prompting

### Principle 1: Write Clear and Specific Instructions

A prompt should clearly explain what we want the model to do.

### Vague Prompt

```text
Tell me about JavaScript.
```

### Improved Prompt

```text
Explain JavaScript promises in simple language.
Include their purpose and two small code examples.
```

The improved prompt gives the model a specific task and expected content.

---

## 3. Providing Sufficient Context

Context helps the model understand the situation, purpose, and audience of the task.

### Example

```text
I am a beginner learning JavaScript.
Explain promises using simple terminology and a small example.
```

Because the prompt tells the model that the user is a beginner, the response can be adapted to a beginner-friendly level.

---

## 4. Using Delimiters

Delimiters help clearly separate different parts of a prompt, especially instructions and input data.

### Example

```text
Summarize the following review:

"""
The product arrived quickly, but the packaging was damaged.
"""
```

Common delimiters include:

* `""" """`
* ` `
* `< >`
* `<tag></tag>`
* `:`

Using delimiters makes it easier for the model to identify the input text.

---

## 5. Specifying the Output Format

We can tell the model exactly how we want the response to be structured.

### Example

```text
Extract the following information from the text and return it as JSON:
- Name
- Price
- Category
```

Expected structure:

```json
{
  "name": "Example Product",
  "price": 500,
  "category": "Electronics"
}
```

Specifying the format helps produce consistent and organized results.

---

## 6. Few-Shot Prompting

Few-shot prompting means providing examples of the expected input and output.

### Example

```text
Input: Happy with the delivery.
Output: Positive

Input: Product arrived late.
Output: Negative

Input: The packaging was excellent.
Output:
```

The examples help the model understand the expected pattern.

---

## 7. Giving the Model Time to Think

For tasks that require multiple steps, we can specify the steps the model should follow.

### Example

```text
First identify the main problem.
Then analyze the possible causes.
Finally, provide the best solution.
```

Breaking a task into steps can make complex tasks more structured.

For evaluation tasks, it can also be useful to ask the model to work out its own solution before evaluating another solution.

---

# 8. Iterative Prompt Development

A prompt does not always produce the desired result on the first attempt.

We can improve the prompt based on the model's output.

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
Get Better Output
     ↓
Repeat
```

### Example

#### First Prompt

```text
Write a product description for this chair.
```

#### Improved Prompt

```text
Write a product description for furniture retailers.
Focus on the materials used to construct the chair.
Keep the description under 50 words.
Return the description in HTML inside a <div>.
```

The improved prompt provides:

* Target audience
* Specific focus
* Length restriction
* Output format

---

# 9. Summarizing

Prompting can be used to summarize text while controlling the length and focus of the response.

### Basic Summary

```text
Summarize the following review.
```

### Summary with Length Constraint

```text
Summarize the following review in at most 30 words.
```

The length can be controlled using:

* Words
* Sentences
* Characters

---

## 10. Focusing a Summary

We can tell the model which topic to focus on.

### Example

```text
Summarize the review below in at most 30 words.
Focus on shipping and delivery information.
```

Adding a focus helps the model prioritize relevant information.

---

# 11. Summarizing vs. Extracting

### Summarizing

Summarizing means condensing the overall content while keeping the important information.

Example:

```text
Summarize this review in at most 30 words.
```

### Extracting

Extraction means returning only the information related to a particular topic.

Example:

```text
Extract only the information related to shipping and delivery
from the review below. Limit the response to 30 words.
```

### Difference

| Summarizing                  | Extracting                                        |
| ---------------------------- | ------------------------------------------------- |
| Condenses the overall text   | Returns only relevant information                 |
| Can include multiple topics  | Focuses on a specific topic                       |
| Useful for general summaries | Useful when only specific information is required |

---

# 12. Hallucinations

AI models can sometimes generate information that sounds believable but is actually false.

This is called a **hallucination**.

For example, a model may generate details about a product, company, person, or fact that does not actually exist.

Therefore, important information should be verified instead of automatically assuming that every AI-generated statement is correct.

---

# 13. General Prompt Structure

A useful prompt can contain several components:

```text
ROLE / CONTEXT
        ↓
CLEAR TASK
        ↓
INPUT / DATA
        ↓
CONSTRAINTS
        ↓
EXPECTED OUTPUT
        ↓
EXAMPLES (if needed)
```

### Example

```text
I am a beginner learning JavaScript.

Explain JavaScript promises in simple language.

Include:
1. What a promise is
2. Why promises are used
3. Two small code examples

Use headings and bullet points.
```

This prompt provides context, a clear task, constraints, and an expected structure.

---

# 14. Key Takeaways

* Write prompts with **clear and specific instructions**.
* Provide **sufficient context**.
* Use **delimiters** to separate input from instructions.
* Specify the **desired output format**.
* Use **examples** when a particular pattern is required.
* Break complex tasks into **clear steps**.
* Improve prompts through **iterative prompt development**.
* Use **length constraints** when summarizing.
* Specify the **focus and audience** when necessary.
* Use **extraction** when only specific information is required.
* Be aware that AI models can produce **hallucinations**.
* A well-structured prompt generally provides better control over the output.

---

## Conclusion

Effective prompt engineering is not just about asking a question. It involves clearly communicating the task, providing the right context, specifying constraints and output format, and refining the prompt based on the results.

The main idea learned today is:

> **Clearer prompts → Better control over AI responses**
