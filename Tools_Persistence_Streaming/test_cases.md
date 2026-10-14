
# Tests — Tools, Persistence and Streaming

## Test 1: Search and Graph Updates
**Question:** What are the latest developments in LangGraph?

**Result:** Passed. The agent called Tavily search, received structured results, and produced an answer with source links.

## Test 2: Persistence
**First interaction:** Search for the official LangGraph documentation and explain what LangGraph does.

**Follow-up:** Based on our previous exchange, what did I ask you to explain?

**Result:** Passed. The second response recalled the first interaction. The saved state contained six messages.

## Test 3: Token Streaming
**Question:** Search for the official LangGraph documentation and summarize what LangGraph does.


**Result:** Passed. The agent executed the search tool, displayed tool events, and generated a final response with source links using the asynchronous streaming workflow.
`streaming_demo.py`.
