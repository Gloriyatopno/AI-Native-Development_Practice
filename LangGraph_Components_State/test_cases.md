
# LangGraph Workflow — Test Cases

## Test 1: Single Tool Call

**Question:** How much does a toy poodle weigh?

**Expected result:** 7 pounds.

**Actual result:** Passed. The graph called `average_dog_weight`, received the observation, and returned the final answer.

## Test 2: Multiple Tool Calls

**Question:** I have a Border Collie and a Scottish Terrier. What is their combined weight?

**Expected result:** 57 pounds.

**Actual result:** Passed. The graph retrieved both weights, called `calculate` with `37 + 20`, and returned 57 pounds.

## Conclusion

Both tests passed. The workflow demonstrated state management, LLM and tool nodes, conditional routing, and returning tool observations to the LLM.
