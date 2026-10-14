
# ReAct Agent — Test Cases

## Test 1: Single Tool Call

**Question:** How much does a toy poodle weigh?

**Expected tool:** `average_dog_weight`

**Expected result:** 7 pounds.

**Pass criteria:** The agent calls the correct tool, receives its observation, and returns the correct final answer.

**Actual result:** Record after testing.

## Test 2: Multiple Tool Calls

**Question:** I have two dogs, a border collie and a Scottish Terrier. What is their combined weight?

**Expected tool sequence:**
1. `average_dog_weight` for the Border Collie.
2. `average_dog_weight` for the Scottish Terrier.
3. `calculate` for `37 + 20`.

**Expected result:** 57 pounds.

**Pass criteria:** The agent uses the observations, performs the calculation, and returns the correct final answer.

**Actual result:** Record after testing.

## Test 3: Unknown Tool

**Purpose:** Verify that the runtime does not execute a tool name that is not in the tools dictionary.

**Pass criteria:** The runtime reports the unknown tool and stops safely if an unknown action is requested.


**Actual result:** Passed. The agent called `average_dog_weight` and returned 7 pounds.

**Actual result:** Passed. The agent looked up both dog weights, called `calculate` with `37 + 20`, and returned 57 pounds.

