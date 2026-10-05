# LangChain Fundamentals — Learning Notes


## Topic
LangChain Fundamentals

---

## 1. What is LangChain?

LangChain is an open-source framework for building applications powered by Large Language Models (LLMs).

It provides reusable components for:

- Models
- Prompt templates
- Output parsers
- Chains and workflows
- Other LLM application components

The main idea is to make LLM application development more modular and easier to reuse.

---

## 2. Direct API Usage

A direct API call sends a prompt directly to the LLM provider.

Example flow:

User Prompt → Groq API → LLM Response

In this project, a direct Groq API call was tested before using LangChain.

Example:

```text
Prompt:
What is an API? Explain it in one simple sentence.

Response:
An API is a set of rules that lets different software programs talk to each other.
```
---

## 3. LangChain Model
LangChain provides an abstraction for interacting with chat-based LLMs.
````markdown
This project uses:

```text
ChatGroq
Model: openai/gpt-oss-20b
Temperature: 0.0
The LangChain model was successfully connected to Groq and used to generate responses.
```
---

## 4. Prompt Templates
A prompt template is a reusable prompt containing input variables.

```text
Example:

Translate the text delimited by triple backticks
into a style that is {style}.

text: 
The template contains two variables:

style
text
The same template can be reused with different styles and different text.

Example uses:

Translate a customer message into calm American English.

Convert a service reply into polite English Pirate style.

This is more reusable than creating separate prompt strings each time.
```
---

## 5. Output Parsers
LLMs normally return text.


For example, an LLM may return JSON-looking output as a string:

{
    "gift": "True",
    "delivery_days": "2",
    "price_value": "..."
}
This is still a string until it is parsed.

LangChain's StructuredOutputParser can parse the output into a Python dictionary.
```text

Example:

LLM response → StructuredOutputParser → Python dictionary
After parsing, dictionary values can be accessed using keys such as:

gift
delivery_days
price_value

```
---

## 6. Basic LangChain Workflow
The practical workflow implemented in this task is:

```text
Input Text
    ↓
ChatPromptTemplate
    ↓
ChatGroq
    ↓
LLM Response
    ↓
StructuredOutputParser
    ↓
Python Dictionary
This demonstrates how multiple LangChain components can work together.
```
---

## 7. Direct API vs LangChain

```text
| Direct API | LangChain |
|---|---|
| Prompt is created manually | Prompt templates are reusable |
| API call is handled directly | Model interaction uses LangChain abstractions |
| Output is returned as text | Output can be parsed into structured data |
| More manual glue code | Components can be composed and reused |
| Useful for simple requests | Useful for larger LLM workflows | |
```
---

## 8. Key Learning Outcomes
- Learned the purpose of LangChain.

- Connected a Groq LLM using LangChain.

- Created reusable prompt templates.

- Used prompt variables such as style and text.

- Reused a single prompt template for different inputs.

- Used ResponseSchema and StructuredOutputParser.

- Converted LLM output into a Python dictionary.

- Compared direct API calls with LangChain.

- Built a basic LangChain workflow.

## 9. Files in This Practice

```text
LangChain_Fundamentals/
├── langchain_fundamentals.py
├── learning_notes.md
├── requirements.txt
├── .env
└── .gitignore
The .env file contains the API key and is excluded from Git using .gitignore.

Save it.
```
