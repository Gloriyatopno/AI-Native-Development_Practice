# OpenAI API – Practical Integration

**Topic:** OpenAI API – Practical Integration  

## Learning Resource

OpenAI Python API – Bootcamp & Integrations – Udemy

> The course teaches OpenAI API concepts. Since Groq provides a free API option, the practical implementation uses Groq API while following the same general request/response flow.

---

## Objective

The objective of this task was to:

- Create a reusable API function.
- Accept user input.
- Send input to a language model.
- Process the model response.
- Handle API errors.
- Keep API keys secure using environment variables.

---

## Project Structure

```text
OpenAI_API_Practical_Integration/
├── llm_api.py
├── test_api.py
├── API_Practical_Notes.md
├── requirements.txt
├── .env
└── .gitignore
```

---

## API Request and Response Flow

```text
User Input
    ↓
Reusable Python Function
    ↓
Groq API Client
    ↓
Language Model
    ↓
API Response
    ↓
Extract Response Text
    ↓
Display Output
```

---

## Reusable API Function

The file `llm_api.py` contains the reusable function:

```python
get_model_response(user_prompt)
```

This function:

1. Accepts a prompt.
2. Checks whether the prompt is empty.
3. Creates the Groq API client.
4. Sends the prompt to the model.
5. Receives the model response.
6. Returns the response text.

---

## Prompt Construction

The request contains two message roles.

### System Message

The system message defines the assistant's behavior.

Example:

```text
You are a helpful AI assistant. Give clear and simple answers.
```

### User Message

The user message contains the actual input.

Example:

```text
Explain Python functions in simple words.
```

---

## Model Response Processing

The response text is extracted using:

```python
response.choices[0].message.content
```

The extracted text is returned by the reusable function.

---

## API Parameters Used

### Model

```python
model="openai/gpt-oss-20b"
```

This model is accessed through Groq API.

### Temperature

```python
temperature=0.7
```

Controls the creativity and variation of the response.

### Maximum Tokens

```python
max_tokens=300
```

Limits the maximum length of the generated response.

---

## Error Handling

The implementation uses `try` and `except` to handle errors.

Example:

```python
try:
    answer = get_model_response(prompt)
    print(answer)

except Exception as error:
    print("Error:", error)
```

The code also checks for:

- Missing API key.
- Empty user prompt.
- API request errors.

---

## API Key Security

The API key is stored in the `.env` file:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

The key is loaded using:

```python
load_dotenv()
```

The key is accessed using:

```python
os.getenv("GROQ_API_KEY")
```

The `.env` file is included in `.gitignore` so the secret is not uploaded to GitHub.

---

## Test Inputs and Outputs

### Test Input 1

```text
What is an API?
```

### Output

The model returned a clear explanation of an API and explained how different software applications communicate with each other.

---

### Test Input 2

```text
Explain Python functions in simple words.
```

### Output

The model explained that a function is a reusable block of code that performs a specific task. It also explained inputs, outputs, and function calls.

---

### Test Input 3

```text
Give one example of machine learning.
```

### Output

The model provided spam email detection as an example. It explained how a model learns patterns from emails labelled as spam or not spam.

---

## Technologies Used

- Python
- Groq API
- Python-dotenv
- Environment variables
- Git and GitHub
- Visual Studio Code

---

## Learning Outcome

After completing this task, I learned how to:

- Create a reusable API module.
- Separate API logic from testing logic.
- Construct prompts.
- Send requests to a language model.
- Process model responses.
- Handle basic errors.
- Protect API keys using environment variables.

---

## Conclusion

This task demonstrated practical integration of a language model API with Python. The reusable API function can be used in other applications such as chatbots, content-generation tools, summarizers, and question-answering systems.