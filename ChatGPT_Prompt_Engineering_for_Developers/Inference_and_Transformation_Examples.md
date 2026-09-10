# Inference and Transformation Examples
---

# 1. Inferring

Inferring means using information provided in a text to determine or derive information that may not be directly stated.

LLMs can be used for tasks such as sentiment analysis, emotion detection, classification, topic identification, and extracting important information.

---

## 1.1 Sentiment Classification

### Input Text

> The lamp arrived quickly and was easy to assemble. When a part was missing, the company sent a replacement immediately. I am very happy with the product and the customer service.

### Prompt

```text
Determine the sentiment of the following review.

Review:
"The lamp arrived quickly and was easy to assemble. When a part was missing, the company sent a replacement immediately. I am very happy with the product and the customer service."

Respond with only one word: positive or negative.
```

### Expected Output

```text
positive
```

### Observation

The model infers the overall sentiment from the customer's positive statements about the product and customer service.

---

## 1.2 Emotion Identification

### Input Text

> I was excited when my package arrived, but I became frustrated when I discovered that the product was damaged.

### Prompt

```text
Identify the emotions expressed in the following text.

Return a maximum of five emotions.
Use lowercase words separated by commas.

Text:
"I was excited when my package arrived, but I became frustrated when I discovered that the product was damaged."
```

### Expected Output

```text
excitement, frustration
```

### Observation

The prompt asks the model to infer emotions from the meaning of the text.

---

## 1.3 Anger Detection

### Input Text

> The delivery was late, but the support team apologized and resolved the issue quickly.

### Prompt

```text
Determine whether the customer is angry.

Respond with only:
yes
or
no

Text:
"The delivery was late, but the support team apologized and resolved the issue quickly."
```

### Expected Output

```text
no
```

### Observation

The model considers the overall context rather than only looking at the negative statement about the late delivery.

---

## 1.4 Extracting Information from Text

### Input Text

> I purchased a Lumina bedroom lamp because I needed an affordable lamp with additional storage.

### Prompt

```text
Extract the item purchased and the company/brand name.

Return the result as JSON with these keys:
- Item
- Brand

If any information is missing, use "unknown".

Text:
"I purchased a Lumina bedroom lamp because I needed an affordable lamp with additional storage."
```

### Expected Output

```json
{
  "Item": "bedroom lamp",
  "Brand": "Lumina"
}
```

### Observation

This demonstrates extracting specific information from unstructured text and returning it in a structured format.

---

## 1.5 Multiple Inference Tasks

### Prompt

```text
Analyze the following customer review and return:

1. Sentiment: positive or negative
2. Anger: yes or no
3. Item purchased
4. Brand

Return the result as JSON.

Review:
"The Lumina lamp arrived quickly and was easy to assemble. A small part was missing, but the company quickly sent a replacement. I am happy with the product and service."
```

### Expected Output

```json
{
  "Sentiment": "positive",
  "Anger": "no",
  "Item": "lamp",
  "Brand": "Lumina"
}
```

### Observation

A single prompt can perform multiple inference tasks when the instructions are clearly specified.

---

## 1.6 Topic Inference

### Input Text

> A recent survey showed significant differences in employee satisfaction across government organizations. NASA reported a very high satisfaction level, while the Social Security Administration reported a much lower level.

### Prompt

```text
Identify the main topics discussed in the following text.

Return a list of relevant topics.

Text:
"A recent survey showed significant differences in employee satisfaction across government organizations. NASA reported a very high satisfaction level, while the Social Security Administration reported a much lower level."
```

### Expected Output

```text
["NASA", "government organizations", "employee satisfaction", "Social Security Administration"]
```

### Observation

The model identifies important topics and entities discussed in the text.

---

## 1.7 Topic Detection and Alert

### Prompt

```text
Determine whether each topic appears in the text.

Topics:
- NASA
- local government
- engineering
- employee satisfaction
- federal government

Text:
"A survey compared employee satisfaction across federal government organizations. NASA reported a high satisfaction level."

Return 1 if the topic appears and 0 if it does not.
```

### Expected Output

```text
NASA: 1
local government: 0
engineering: 0
employee satisfaction: 1
federal government: 1
```

### Observation

Classification can be used to detect whether specific topics are present in a piece of text.

---

# 2. Transforming

Transforming means taking existing information and changing it into another language, tone, format, or corrected version while preserving its meaning.

LLMs can perform translation, tone transformation, format conversion, and grammar/spelling correction.

---

## 2.1 Translation

### Input

```text
The meeting will start at 10 AM tomorrow.
```

### Prompt

```text
Translate the following sentence from English to Spanish.

Text:
"The meeting will start at 10 AM tomorrow."
```

### Expected Output

```text
La reunión comenzará a las 10 de la mañana mañana.
```

### Observation

The original information is transformed from one language into another.

---

## 2.2 Formal and Informal Transformation

### Input

```text
Hey, can you check this standing lamp design and tell me what you think?
```

### Prompt

```text
Rewrite the following message in a professional business tone.

Text:
"Hey, can you check this standing lamp design and tell me what you think?"
```

### Expected Output

```text
Could you please review the standing lamp design and share your feedback?
```

### Observation

The meaning remains the same, but the tone changes from casual to professional.

---

## 2.3 Text to HTML

### Input

```text
Employees:
John - Developer
Sarah - Designer
Mike - Tester
```

### Prompt

```text
Convert the following employee information into an HTML table.

Include:
- A table heading
- Column headers
- Employee names
- Job roles

Text:
"Employees:
John - Developer
Sarah - Designer
Mike - Tester"
```

### Expected Output

```html
<table>
  <caption>Employees</caption>
  <tr>
    <th>Name</th>
    <th>Role</th>
  </tr>
  <tr>
    <td>John</td>
    <td>Developer</td>
  </tr>
  <tr>
    <td>Sarah</td>
    <td>Designer</td>
  </tr>
  <tr>
    <td>Mike</td>
    <td>Tester</td>
  </tr>
</table>
```

### Observation

Unstructured text is transformed into HTML markup.

---

## 2.4 Text to JSON

### Input

```text
Name: Gloriya
Course: BSc IT
Year: 3
```

### Prompt

```text
Convert the following information into a JSON object.

Use these keys:
- name
- course
- year

Text:
"Name: Gloriya
Course: BSc IT
Year: 3"
```

### Expected Output

```json
{
  "name": "Gloriya",
  "course": "BSc IT",
  "year": 3
}
```

### Observation

The same information can be transformed into a structured data format such as JSON.

---

## 2.5 Grammar and Spelling Correction

### Input

```text
The product have many good feature and it work very well.
```

### Prompt

```text
Proofread and correct the following sentence.

Fix grammar and spelling errors while keeping the original meaning.

If there are no errors, respond with "No errors found."

Text:
"The product have many good feature and it work very well."
```

### Expected Output

```text
The product has many good features and it works very well.
```

### Observation

The model transforms incorrect text into a grammatically correct version while preserving its meaning.

---

# 3. Structured Response Generation

LLMs can be instructed to return information in a specific structure. This makes the output easier to read, compare, process, or use in applications.

### Prompt

```text
Analyze the following product review.

Return the response in this exact structure:

Sentiment: positive or negative
Anger: yes or no
Product: product name
Brand: brand name
Reason: one short sentence

Review:
"The Lumina lamp arrived quickly and was easy to assemble. The company also replaced a missing part quickly."
```

### Expected Output

```text
Sentiment: positive
Anger: no
Product: lamp
Brand: Lumina
Reason: The customer was satisfied with the product and support service.
```

### Observation

Specifying the output structure helps produce consistent and organized responses.

---

# 4. Inference vs Transformation

| Inferring                     | Transforming                             |
| ----------------------------- | ---------------------------------------- |
| Derives information from text | Changes the form of existing information |
| Sentiment classification      | Translation                              |
| Emotion detection             | Tone adjustment                          |
| Topic identification          | Format conversion                        |
| Information extraction        | Grammar correction                       |
| Anger detection               | Text to JSON/HTML                        |

---

# 5. Key Learnings

* **Inferring** allows an LLM to derive information from provided text.
* Inferring can be used for sentiment analysis, emotion detection, classification, topic identification, and information extraction.
* **Transforming** changes existing text into another language, tone, format, or corrected version.
* Clear instructions make the expected result easier for the model to follow.
* Output constraints such as JSON, lists, tables, or specific labels make responses more consistent.
* A single prompt can combine multiple inference or transformation tasks.
* Structured responses are useful when information needs to be processed or reused later.

---

# 6. Conclusion

Inferring and transforming are useful prompt engineering techniques for working with information.

Inferring focuses on **understanding and deriving information from text**, while transforming focuses on **changing existing information into a different form**.

By providing clear instructions, context, constraints, and an expected output format, LLMs can produce more useful and consistent results.
