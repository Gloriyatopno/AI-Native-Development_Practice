# RAG Pipeline — Q&A Test Cases

## Test 1: Model Information

**Question:** What model does the AI Text Assistant use?

**Expected Answer:** GPT-OSS-20B.

**Initial Result:** The answer was not found with the top 3 retrieved sections.

**Improvement:** Increased retrieval from 3 to 5 sections.

**Final Result:** Passed. The correct model information was retrieved and used to generate the answer.

---

## Test 2: API Key Protection

**Question:** How does the application protect its API credentials?

**Expected Answer:** Credentials are stored in the `GROQ_API_KEY` environment variable.

**Result:** Passed. The system retrieved the relevant context and generated the correct answer.

---

## Retrieval Quality Observation

Retrieval quality improved after increasing the number of retrieved sections from 3 to 5. The model-information section was included in the retrieved context, allowing the LLM to answer correctly.