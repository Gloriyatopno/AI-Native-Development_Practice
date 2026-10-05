```markdown
# LangChain — Evaluation & Agents Learning Notes

## Date

28.09.2026

## Topic

Evaluation & Agents in LangChain

## Learning Resource

LangChain for LLM Application Development — DeepLearning.AI

---

## 1. Evaluation

Evaluation is important when developing LLM applications because it helps determine whether an application is producing useful and accurate results.

Evaluation can also help compare different implementations and determine whether a change improves or reduces performance.

---

## 2. Test Data

Evaluation requires test examples containing questions and expected answers.

The implementation used three examples:

- What is 2 + 2? → 4
- What planet is known as the Red Planet? → Mars
- What is the capital of France? → Paris

---

## 3. Manual Evaluation

The predicted answers were inspected and compared with the expected answers.

Two predictions were correct and one prediction was intentionally incorrect.

---

## 4. LLM-Assisted Evaluation

An LLM was used to evaluate the predicted answers.

The evaluator judged the answers based on meaning rather than exact wording.

Example:

Expected answer:

```text
Mars

Predicted answer:

Mars is known as the Red Planet.
These answers use different wording but have the same meaning, so the prediction was graded as a pass.
```
---

## 5. Evaluation Result
```text
Total examples: 3
Passed: 2
Failed: 1
Evaluation score: 67%
The incorrect Paris/Berlin prediction was correctly identified as a failure.
```
---

## 6. Agents
An agent uses an LLM as a reasoning engine.

Instead of always responding directly, an agent can decide whether it should use an available tool to solve a task.
```text
Basic flow:

User Question
      ↓
LLM Agent
      ↓
Decide which action/tool is needed
      ↓
Tool
      ↓
Tool Result
      ↓
Final Answer
```
---

## 7. Tools
Tools are functions that an agent can call when they are useful for answering a question.
```text
Two custom tools were implemented:

calculate_percentage
get_today_date
The agent was given access to both tools.
```
---

## 8. Agent Decision-Making
The agent successfully selected different tools based on the question.
```text
For a percentage calculation:

Question → calculate_percentage → Result → Final Answer
For today's date:

Question → get_today_date → Result → Final Answer
This demonstrates that the agent can choose an appropriate action instead of using the same operation for every question.
```
---

## 9. Custom Tool
- A custom date tool was implemented to return the current date.

- The tool contains a description explaining when it should be used.

- The agent used this description to select the tool for a date-related question.
---

## 10. Key Learning Outcomes
- Learned why LLM applications need evaluation.

- Created question and answer test cases.

- Performed manual evaluation.

- Used LLM-assisted evaluation.

- Compared expected and predicted answers semantically.

- Learned how agents use LLMs as reasoning engines.

- Created and used custom tools.

- Observed agent tool selection and decision-making.

- Built and tested a basic LangChain agent.
---

## 11. Files in This Practice
```text
Evaluation_and_Agents/
├── evaluation_demo.py
├── agent_demo.py
├── test_cases.md
├── learning_notes.md
├── requirements.txt
├── .env
└── .gitignore
```