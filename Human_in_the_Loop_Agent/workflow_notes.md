
# Human-in-the-Loop Essay Writer

## Overview
This project uses Flask and LangGraph to research a topic, generate an essay, and pause for human review before final approval.

## Workflow Nodes
1. Research: Uses Tavily to retrieve information about the topic.
2. Write: Uses Groq to generate an essay draft.
3. Human Review: Pauses for approval or revision feedback.
4. Revise: Rewrites the essay using the reviewer's feedback.

## Human-in-the-Loop
LangGraph's `interrupt()` pauses execution and provides the current draft for review. A SQLite checkpointer saves the workflow state. The graph resumes using `Command(resume=decision)` with the same thread configuration.

## State
- `topic`: Essay subject.
- `research`: Retrieved research information.
- `draft`: Current essay draft.
- `review_feedback`: Human feedback.
- `revision_count`: Number of revisions completed.
- `approved`: Whether the essay was approved.
- `status`: Current workflow status.

## Application
The Flask app provides a browser interface to submit a topic, view drafts, request revisions, and approve an essay. Each essay gets its own thread ID.

## Revision Limit
The workflow allows up to two revisions before ending. If the limit is reached without approval, the final status is `revision_limit_reached`.

## Testing
The terminal workflow was tested with a revision request followed by approval. The Flask application was also tested through its browser routes.
