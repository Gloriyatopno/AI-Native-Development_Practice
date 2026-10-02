# AI Text Assistant

A simple Flask web application that integrates a Large Language Model (LLM) using the Groq API. Users can enter questions or requests and receive AI-generated responses directly on the webpage.

## Live Demo

https://ai-native-development-practice.onrender.com

## Features

* Accepts user prompts through a web interface.
* Connects to the Groq API.
* Generates AI responses using the GPT-OSS-20B model.
* Converts Markdown responses into formatted HTML.
* Displays responses with support for headings, lists, bold text, and tables.
* Handles empty input and API errors.
* Uses environment variables to protect API credentials.

## Technologies Used

* Python
* Flask
* Groq API
* GPT-OSS-20B
* HTML
* CSS
* Markdown
* python-dotenv

## Application Architecture

User Input → Flask Application → Groq API → LLM Response → Markdown Conversion → Webpage

## Project Structure

```text
First_LLM_Feature_Application/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Gloriyatopno/AI-Native-Development_Practice/tree/main/First_LLM_Feature_Application
```

Navigate to the project folder:

```bash
cd First_LLM_Feature_Application
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your own Groq API key.

Never upload your `.env` file to GitHub.

### 4. Run the application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## Testing

The following manual tests were performed:

| Test | Description               | Result |
| ---- | ------------------------- | ------ |
| 1    | Normal AI request         | Passed |
| 2    | Different type of request | Passed |
| 3    | Empty input validation    | Passed |
| 4    | API error handling        | Passed |

## API Integration

The course covers OpenAI API integration concepts. This practical implementation uses Groq because it offers a free API option. Groq provides an OpenAI-compatible API interface, while this application uses the Groq Python SDK.

## Future Improvements

* Deploy the application online.
* Improve the user interface.
* Add loading indicators.
* Add conversation history.
* Improve response security and error handling.

## Learning Outcomes

* Integrated an LLM into a Flask application.
* Connected user input to an external AI API.
* Processed and displayed generated responses.
* Practiced debugging and testing an application.
* Applied API key management using environment variables.
