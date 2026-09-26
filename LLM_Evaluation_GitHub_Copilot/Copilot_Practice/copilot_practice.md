# GitHub Copilot Practice

## 1. Code Explanation

### Objective
Use GitHub Copilot to explain an existing Python program and understand how its functions and evaluation logic work.

### File Used
`llm_evaluation.py`

### Copilot Prompt
Explain this function in simple terms. Describe what the function does, what its inputs are, what it returns, and how it determines whether the LLM output is correct.

### Result
GitHub Copilot explained the purpose and structure of the LLM evaluation program.

The explanation covered:

- Groq API integration and environment variable handling.
- The purpose of `get_client()` and `generate_response()`.
- Single-answer evaluation using expected and generated answers.
- Case-insensitive exact comparison.
- Rubric-based evaluation for open-ended responses.
- JSON parsing and fallback handling.
- Expert-answer comparison using evaluation categories A–E.
- The role of the `main()` function.
- The purpose of `if __name__ == "__main__":`.

Copilot also identified an important limitation of the evaluation system: an LLM is being used to evaluate another LLM response, so the evaluator can make mistakes or return invalid output.

### Manual Review
The Copilot explanation was reviewed against `llm_evaluation.py`.

The explanation accurately described the main functions, evaluation methods, and program flow. No incorrect code behavior was identified.

### Learning
GitHub Copilot can help explain existing code by describing its purpose, inputs, outputs, logic, and potential limitations. The explanation should still be manually verified against the actual code.

## 2. Code Generation

### Objective
Use GitHub Copilot to generate a Python function based on a clear natural-language requirement.

### Task
Create a function that compares an expected answer with a generated answer.

### Copilot Prompt
Create a Python function called compare_answers that takes an expected answer and a generated answer as inputs. It should normalize both answers by removing leading/trailing whitespace and converting them to lowercase, then return True if they match exactly and False otherwise. Include a few simple examples showing how the function works.

### File Generated
`Copilot_Practice/copilot_code_generation.py`

### Result
Copilot generated the `compare_answers()` function and example test cases.

The generated function:
- Removes leading and trailing whitespace.
- Converts both answers to lowercase.
- Performs an exact comparison.
- Returns `True` when the normalized answers match.
- Returns `False` when they do not match.

### Testing
The generated code was executed successfully.

Example results:

```text
True
True
False

## 3. Debugging

### Objective
Use GitHub Copilot to identify and fix a bug in Python code.

### Buggy Code
The original function attempted to calculate the average of a list without checking whether the list was empty.

### Copilot Prompt
Find the bug in this Python code. Explain why the error occurs and provide a corrected version that safely handles an empty list. Keep the original behavior for non-empty lists.

### Bug Identified
When an empty list is passed, `len(numbers)` is `0`. Dividing the total by zero causes a division-by-zero error.

### Copilot Fix
Copilot added a check for an empty list before performing the division:

```python
if not numbers:
    return 0

## 4. Refactoring

### Objective
Use GitHub Copilot to improve working code without changing its behavior.

### Original Code
The original function used separate variables for the subtotal, discount amount, and final price.

### Copilot Prompt
Refactor this Python function to improve readability and maintainability without changing its behavior or output. Use clear variable names and simplify the code where appropriate.

### File
`Copilot_Practice/copilot_refactoring.py`

### Copilot Changes
Copilot:
- Used clearer parameter names such as `unit_price`, `quantity`, and `discount_percentage`.
- Added type hints.
- Added a descriptive docstring.
- Removed the unnecessary `final_price` variable.
- Kept the same calculation and behavior.

### Testing
The refactored program was executed successfully.

Output:

```text
180.0

## 5. Testing

### Objective
Use GitHub Copilot to generate automated tests for an existing Python function and verify that the tests pass.

### File Tested
`Copilot_Practice/copilot_refactoring.py`

### Copilot Prompt
Generate pytest unit tests for this function. Include tests for normal calculation, zero discount, zero quantity, and a higher discount. Make sure each test has a clear expected result.

### Test File
`Copilot_Practice/test_copilot_refactoring.py`

### Tests Generated
Copilot generated four pytest test cases:

- Normal calculation
- Zero discount
- Zero quantity
- Higher discount

### Test Execution

The tests were run using:

```bash
python -m pytest test_copilot_refactoring.py
 
## 6. Code Review

### Objective
Use GitHub Copilot to review existing code for bugs, edge cases, input validation, readability, and maintainability.

### File Reviewed
`Copilot_Practice/copilot_refactoring.py`

### Copilot Prompt
Review this Python function for bugs, edge cases, readability, maintainability, and input validation. Identify any potential issues and suggest improvements. Do not change the code yet. Explain each finding clearly.

### Copilot Findings

Copilot identified the following potential issues:

1. **Input validation**
   - The function does not validate negative prices, negative quantities, or invalid discount percentages.
   - Copilot suggested validating acceptable input ranges.

2. **Type validation**
   - Python type hints are not enforced at runtime.
   - The function could receive unexpected types even though type hints are provided.

3. **Floating-point money calculations**
   - The function uses `float` values for price calculations.
   - Copilot noted that `Decimal` may be more appropriate for financial calculations where exact precision is important.

4. **Rounding behavior**
   - The function does not define whether the returned price should be rounded to two decimal places.

5. **Test coverage**
   - The existing tests cover valid cases but do not test invalid inputs, floating-point precision, or rounding behavior.

### Readability and Maintainability

Copilot confirmed that the variable names are clear and the calculations are readable. It did not identify a need for further simplification.

### Manual Review

The Copilot findings were reviewed against the actual implementation and existing tests.

There is no immediate bug for the currently tested valid inputs. The identified issues are potential edge cases and design considerations, particularly input validation and monetary precision.

No code changes were made because the purpose of this exercise was to practice code review rather than modify the implementation.

### Learning

GitHub Copilot can review existing code and identify potential bugs, edge cases, validation concerns, and maintainability improvements. However, developers should manually verify Copilot's findings before making changes.