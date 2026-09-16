# Connecting Applications with LLMs

## Topic

Connecting Applications with LLMs

## Learning Resource

OpenAI Python API – Bootcamp & Integrations

> **Note:** The course explains the OpenAI API and older Completion API examples.  
> For practical implementation, this project uses Groq as a free alternative API.  
> The general concepts of authentication, requests, responses, models, and parameters remain similar.

---

# 1. What Is an API?

API stands for **Application Programming Interface**.

An API allows two software applications to communicate with each other.

For example:

1. A Python application sends a question.
2. The API sends the question to an AI model.
3. The AI model generates a response.
4. The API returns the response to the Python application.
5. The Python application displays the answer.

### Basic API Flow

```text
User Input
    ↓
Python Application
    ↓
LLM API
    ↓
AI Model
    ↓
API Response
    ↓
Displayed Output
```

---

# 2. What Is an LLM?

LLM stands for **Large Language Model**.

An LLM is an AI model trained on a large amount of text and code.

It can perform tasks such as:

- Answering questions
- Summarizing text
- Translating languages
- Generating code
- Explaining concepts
- Creating content
- Extracting information
- Changing the tone of text

Examples of LLM-based services include ChatGPT and other AI model APIs.

---

# 3. OpenAI API Concepts

The course explains the OpenAI API, which allows applications to communicate with OpenAI models.

The main concepts are:

1. API account
2. API key
3. Model
4. Prompt
5. API request
6. API response
7. Response processing
8. API parameters

The same general concepts can be applied to other LLM APIs, such as Groq.

---

# 4. API Authentication

API authentication verifies that an application is allowed to use an API.

An **API key** is a secret credential used for authentication.

### Important Security Rules

- Never share your API key.
- Never upload your API key to GitHub.
- Never hardcode secret keys directly in Python files.
- Store the key in a `.env` file.
- Add `.env` to `.gitignore`.
- Do not include the API key in screenshots or documentation.

### Example `.env` File

```env
GROQ_API_KEY=your_secret_api_key
```

The key is loaded in Python using the `python-dotenv` package.

---

# 5. Python API Integration

The general process of connecting Python with an LLM API is:

1. Install the required package.
2. Load the API key securely.
3. Create the API client.
4. Accept user input.
5. Send the input to the model.
6. Receive the API response.
7. Extract the response text.
8. Display the result.
9. Handle possible errors.

### General Flow

```text
Install Packages
    ↓
Load API Key
    ↓
Create API Client
    ↓
Accept User Input
    ↓
Send API Request
    ↓
Receive API Response
    ↓
Extract Response Text
    ↓
Display Output
```

---

# 6. Packages Used

This project uses the following Python packages.

## 6.1 Groq

The `groq` package is used to communicate with the Groq API.

It allows a Python application to send prompts to an LLM and receive responses.

## 6.2 python-dotenv

The `python-dotenv` package loads environment variables from a `.env` file.

It helps keep API keys separate from the main Python code.

### Installation Command

```bash
pip install groq python-dotenv
```

The packages can also be installed using the project’s `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

# 7. Creating the API Client

The API key is loaded from the `.env` file.

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
```

### Explanation

- `os` is used to access environment variables.
- `load_dotenv()` loads values from the `.env` file.
- `os.getenv()` reads the API key.
- `Groq()` creates the API client.

In this project, Groq is used as a free alternative API for practicing the general LLM request and response process.

---

# 8. Sending an API Request

The application sends a request using the model name and messages.

```python
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is."
        }
    ],
    temperature=0.7,
    max_tokens=300
)
```

## Important Request Parameters

| Parameter | Meaning |
|---|---|
| `model` | Specifies which AI model to use |
| `messages` | Contains the conversation messages |
| `temperature` | Controls randomness and creativity |
| `max_tokens` | Limits the generated response length |

---

# 9. Receiving and Processing the Response

The API response contains information about the generated answer.

The generated text can be extracted using:

```python
answer = response.choices[0].message.content
```

The answer can then be displayed using:

```python
print(answer)
```

### Complete Response Flow

```python
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain Python."
        }
    ]
)

answer = response.choices[0].message.content

print(answer)
```

---

# 10. Message Roles

Chat-based APIs commonly use different message roles.

## 10.1 System

The `system` role defines the behavior or instructions for the AI.

Example:

```python
{
    "role": "system",
    "content": "You are a helpful assistant."
}
```

## 10.2 User

The `user` role contains the question or instruction from the user.

Example:

```python
{
    "role": "user",
    "content": "Explain Python."
}
```

## 10.3 Assistant

The `assistant` role represents the AI’s response.

Conversation history can contain previous assistant messages so that the model can understand earlier parts of the conversation.

### Example

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "What is Python?"
    },
    {
        "role": "assistant",
        "content": "Python is a programming language."
    },
    {
        "role": "user",
        "content": "What is it used for?"
    }
]
```

---

# 11. Text Completion API

A Completion API takes an input prompt and generates a continuation.

The name **completion** comes from the idea that the model completes the given text with probable output.

### Example

```text
Input:
Write a Python function to add two numbers:

Output:
def add(a, b):
    return a + b
```

The course discussed two older types of completion models:

- Text completion models
- Code completion models

Text completion models were designed for natural language.

Code completion models were optimized for generating programming code.

The course used older model examples such as:

```text
text-davinci-003
code-davinci-002
```

These are historical course examples and should not be copied directly into the current project.

---

# 12. Important Completion API Parameters

## 12.1 Model

The `model` parameter specifies which AI model should process the request.

Example:

```python
model="openai/gpt-oss-20b"
```

The model name depends on the API provider and the models currently available.

---

## 12.2 Prompt or Messages

The prompt or messages contain the instructions given to the model.

A clear prompt is very important because it strongly affects the quality of the response.

Example:

```text
Explain machine learning in simple words with one example.
```

A more specific prompt usually gives a more focused response.

---

## 12.3 Temperature

Temperature controls how random or creative the response is.

- `0` → more predictable and focused
- Higher values → more creative and varied responses

Example:

```python
temperature=0.7
```

### Suitable Uses

A lower temperature can be useful for:

- SQL queries
- Calculations
- Structured responses
- Tasks with a clear correct answer

A higher temperature can be useful for:

- Story writing
- Brainstorming
- Creative writing
- Generating different ideas

---

## 12.4 Max Tokens

`max_tokens` controls the maximum number of tokens generated in the response.

Example:

```python
max_tokens=300
```

The prompt tokens and generated tokens must fit within the model’s context limit.

---

## 12.5 Top P

`top_p` controls token selection using probability mass.

It is also known as **nucleus sampling**.

The course recommends changing either:

- `temperature`

or

- `top_p`

instead of changing both at the same time.

---

## 12.6 N

The `n` parameter specifies how many completions should be generated for one prompt.

For example:

```python
n=2
```

This requests two possible responses.

Generating multiple responses can use more tokens and may increase API usage.

---

## 12.7 Frequency Penalty

The frequency penalty reduces repeated words and phrases.

It can be useful when the model keeps repeating the same sentence or idea.

Example:

```python
frequency_penalty=0.5
```

Very high values may reduce the quality of the response.

---

## 12.8 Presence Penalty

The presence penalty encourages the model to introduce new words or topics.

Example:

```python
presence_penalty=0.5
```

Very high values may cause the model to move away from the main topic.

---

## 12.9 Stop Sequences

A stop sequence tells the model when to stop generating.

Example:

```python
stop=[";"]
```

In the course’s SQL project, a semicolon was considered a useful stop sequence because SQL queries commonly end with a semicolon.

---

# 13. Playground

The course introduced the OpenAI Playground as a place to experiment with:

- Prompts
- Temperature
- Maximum length
- Stop sequences
- Frequency penalty
- Presence penalty
- Different models

The Playground helps users understand how changing prompts and parameters affects model output.

For this project, the practical implementation is completed in VS Code using Python.

---

# 14. OpenAI API Call and Request Handling

The course demonstrated the following process:

1. Prepare the prompt.
2. Select a model.
3. Send the API request.
4. Receive the response.
5. Extract the generated text.
6. Clean or process the response.
7. Use the result in the application.

### General API Request Flow

```text
Prepare Prompt
    ↓
Select Model
    ↓
Send API Request
    ↓
Receive Response
    ↓
Extract Generated Text
    ↓
Process Response
    ↓
Display or Use Result
```

In the course’s NLP-to-SQL project, the generated SQL query was cleaned and then executed against a database.

For the current project, the response is displayed directly to the user.

---

# 15. Error Handling

API requests may fail because of:

- Missing API key
- Invalid API key
- Internet connection problems
- Incorrect model name
- API rate limits
- Service errors
- Invalid request parameters

The application uses `try-except` to handle errors.

```python
try:
    answer = get_model_response(user_input)
    print(answer)

except Exception as error:
    print("Error:", error)
```

Error handling prevents the application from crashing immediately when an API request fails.

---

# 16. Practical Project

## Project File

```text
api_integration.py
```

## Project Features

- Loads the API key securely.
- Creates a Groq API client.
- Accepts user input.
- Sends the prompt to the LLM.
- Displays the model response.
- Continues accepting questions.
- Stops when the user types `exit`.
- Handles API errors.

## Example Output

```text
Connecting Applications with LLMs
Type 'exit' to stop.

You: Explain what an API is.

AI: An API is a way for two software applications to communicate.

You: What is the difference between AI and machine learning?

AI: AI is the broader concept of creating intelligent systems.
Machine learning is one method used to achieve AI.

You: exit

Goodbye!
```

---

# 17. Learning Outcome

After completing this task, I learned how to:

- Understand the purpose of an LLM API.
- Understand the basic API request and response flow.
- Configure API authentication.
- Store API keys securely.
- Use environment variables.
- Connect Python with an LLM API.
- Send user prompts to a model.
- Receive model responses.
- Extract response text.
- Display AI-generated answers.
- Use parameters such as temperature and max tokens.
- Understand message roles.
- Handle API errors.
- Run the project using VS Code.
- Use Groq as a practical alternative to OpenAI.

---

# 18. Conclusion

An LLM API allows Python applications to use the capabilities of an AI model.

The basic process is:

```text
User Input
    ↓
API Request
    ↓
AI Model
    ↓
API Response
    ↓
Extract Response
    ↓
Display Output
```

The course examples use the OpenAI Completion API, while this practical project uses Groq as a free alternative API.

The main concepts of authentication, requests, responses, models, parameters, and response processing remain the same.

The most important learning is that a Python application can communicate with an LLM through an API and use the generated response in a real application.