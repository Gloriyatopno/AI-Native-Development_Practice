# LangChain — Memory & Chains Learning Notes

## Date

24.09.2026

## Topic

Memory & Chains

## Learning Resource

LangChain for LLM Application Development — DeepLearning.AI

---

## 1. Memory in LangChain

LLMs are stateless by themselves. They do not automatically remember previous messages in a conversation.

LangChain provides memory components that store previous conversation information and provide it as context to the LLM.

---

## 2. ConversationBufferMemory

`ConversationBufferMemory` stores the conversation history.

Example workflow:

```text
User: Hi, my name is Gloriya.
AI: Hello, Gloriya!

User: What is 1 + 1?
AI: 2

User: What is my name?
AI: Gloriya
```
---

## 3. ConversationBufferWindowMemory
ConversationBufferWindowMemory keeps only a limited number of recent conversation exchanges.
```text
In the implementation:

k = 1
This means only the most recent conversation exchange is retained.

This helps prevent the memory from growing indefinitely.
```
---

## 4. Manually Saving Context
LangChain memory can also be updated explicitly using conversation input and output.
```text
Example:

Input: Hi
Output: What's up?

Input: Not much, just learning LangChain.
Output: That's great!
The saved context can then be loaded from memory.
```
---

## 5. Chains
A chain combines multiple components so that an LLM application can perform operations in sequence.

A basic chain can combine:
```text
Prompt → LLM → Response
Chains are useful because they reduce repeated glue code and allow multiple operations to be connected.
```
---

## 6. LLM Chain
An LLM chain combines a prompt with an LLM.
```text
Example:

Product
   ↓
Prompt
   ↓
LLM
   ↓
Company Name
In the practical implementation, a product description was passed to the chain and the LLM generated a company name.
```
---

## 7. Simple Sequential Chain
A SimpleSequentialChain connects multiple chains in sequence.
```text
Example:

Product
   ↓
Chain 1
   ↓
Company Name
   ↓
Chain 2
   ↓
Company Description
The output from the first chain becomes the input to the second chain.

This was successfully implemented using a product called "Queen Size Sheet Set".
```
---

## 8. Multi-Step LLM Workflow
A multi-step workflow connects several LLM operations to process information step by step.

```text
The implemented workflow was:

Customer Review
       ↓
Chain 1
       ↓
Summary
       ↓
Chain 2
       ↓
Sentiment
       ↓
Chain 3
       ↓
Customer Response
The workflow successfully:

Summarized the customer review.

Identified the sentiment as Positive.

Generated a polite customer-service response using the previous results.

This demonstrates how multiple LLM operations can be connected into one workflow.
```
---

## 9. Key Learning Outcomes

- Learned how conversational memory works in LangChain.

- Implemented ConversationBufferMemory.

- Implemented ConversationBufferWindowMemory.

- Learned how conversation history is stored and reused.

- Learned the purpose of chains.

- Implemented an LLM chain.

- Implemented a simple sequential chain.

- Connected multiple LLM operations.

- Built and tested a multi-step LLM workflow.

- Learned how the output of one step can be used by a later step.

---

## 10. Files in This Practice
```text
Memory_and_Chain/
├── memory_demo.py
├── chains_demo.py
├── multi_step_workflow.py
├── requirements.txt
├── .env
├── .gitignore
└── learning_notes.md
```