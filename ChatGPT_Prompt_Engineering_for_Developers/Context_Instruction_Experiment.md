# Context and Instruction Experiment

---

## Objective

The purpose of this experiment is to observe how adding **context** and **clear instructions** can change the quality and usefulness of an AI response.

---

# Experiment 1: Without Context

### Prompt

```text
Explain databases.
```

### Expected Response

The AI may provide a general explanation of databases.

However, the response may not be appropriate for a particular learner because the prompt does not specify:

* Who the explanation is for
* What level of knowledge the user has
* Which aspects should be covered
* How the answer should be structured

---

# Experiment 2: Adding Context

### Prompt

```text
I am a BSc IT student and a beginner in database concepts.

Explain databases in simple language.
```

### Expected Improvement

The AI now knows that the explanation should be suitable for a beginner.

The response can therefore use simpler terminology and avoid unnecessarily advanced concepts.

---

# Experiment 3: Adding Clear Instructions

### Prompt

```text
I am a BSc IT student and a beginner in database concepts.

Explain databases in simple language.

Include:
1. What a database is
2. Why databases are used
3. What a DBMS is
4. One simple real-world example

Use headings and bullet points.
Keep the explanation under 200 words.
```

### Expected Improvement

This prompt gives the AI:

* **Context:** BSc IT student and beginner
* **Task:** Explain databases
* **Required information:** Four specific points
* **Format:** Headings and bullet points
* **Constraint:** Maximum 200 words

The response should therefore be more focused, organized, and appropriate for the intended audience.

---

# Experiment Comparison

| Prompt   | Context | Clear Instructions | Constraints | Expected Control |
| -------- | ------- | ------------------ | ----------- | ---------------- |
| Prompt 1 | No      | No                 | No          | Low              |
| Prompt 2 | Yes     | Partially          | No          | Medium           |
| Prompt 3 | Yes     | Yes                | Yes         | High             |

---

# Experiment 4: Changing the Audience

The same topic can produce different responses depending on the audience specified in the prompt.

### Prompt for a Beginner

```text
Explain APIs to a beginner who has basic knowledge of JavaScript.

Use simple language and one real-world example.
```

### Prompt for a Developer

```text
Explain REST APIs to a junior web developer.

Focus on HTTP methods, endpoints, request/response structure,
and status codes. Include a simple example.
```

### Observation

Although both prompts are about APIs, the expected responses are different because the **audience and required level of detail** are different.

---

# Experiment 5: Changing the Output Instructions

### Prompt Without Format

```text
Explain the benefits of Git.
```

### Prompt With Format

```text
Explain the benefits of Git.

Return the answer using:
- A short definition
- Five benefits
- One practical example

Use bullet points and simple language.
```

### Observation

The second prompt gives the AI a specific structure, making the response easier to read and more consistent.

---

# Overall Observations

From these experiments, I observed that:

1. Adding **context** helps the AI understand the situation and intended audience.
2. Adding **clear instructions** makes the task more specific.
3. Adding **constraints** gives better control over the response.
4. Specifying the **output format** makes the response more organized.
5. Changing the **audience** can change the level and style of the response.
6. A structured prompt generally provides more control than a vague prompt.

---

# Conclusion

This experiment demonstrated that prompt quality can be improved by gradually adding relevant information.

The basic pattern observed was:

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
More Controlled Response
```

> **Context tells the AI the situation, instructions tell it what to do, and constraints tell it how to do it.**
