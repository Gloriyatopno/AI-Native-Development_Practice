from llm_api import get_model_response


def main():
    test_prompts = [
        "What is an API?",
        "Explain Python functions in simple words.",
        "Give one example of machine learning."
    ]

    for prompt in test_prompts:
        print("User:", prompt)

        try:
            answer = get_model_response(prompt)
            print("AI:", answer)

        except Exception as error:
            print("Error:", error)

        print("-" * 50)


if __name__ == "__main__":
    main()