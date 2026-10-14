
# Tools, Persistence and Streaming

## Search Tool
The agent uses the Tavily search tool to retrieve relevant web information. The LLM can request searches and use returned results to formulate an answer.

## Persistence
A file-backed SQLite database stores graph checkpoints. The thread ID identifies the conversation, allowing later interactions to continue from previously saved state.

## Streaming
- Graph-update streaming displays completed workflow steps and their outputs.
- Token streaming displays text chunks from the LLM as they are generated.
- The async streaming example uses `AsyncSqliteSaver` and `astream_events`.

## Multi-Step Workflow
1. Receive a user question.
2. The LLM decides whether to use search.
3. The tool executes and returns observations.
4. The LLM uses those observations to form an answer.
5. Checkpoints save the conversation state.
6. Streaming exposes progress as the workflow runs.

## Database
The SQLite checkpoint database is named `agent_checkpoints.sqlite`. It is local to this project and should not be committed to GitHub.

## Limitations
Search quality depends on the retrieved sources. SQLite is appropriate for this small learning project, not a production multi-user deployment.
