# Question & Answer with LangChain — Learning Notes

## Topic

Question & Answer with LangChain

---

## 1. Question & Answer over Documents

Question answering over documents allows an LLM to answer questions using information supplied in external documents.

This makes an LLM more useful because it can work with information that was not part of its original training data.

---

## 2. Document Loading

The sample data was stored in a CSV file containing outdoor clothing products and their descriptions.

The CSV documents were loaded using LangChain's `CSVLoader`.

Each CSV row was treated as a document containing product information.

---

## 3. Vector Representation

To find relevant information, the document text was converted into numerical vector representations.

In this implementation, TF-IDF was used to create the vectors.

These vectors were used to compare the similarity between a user's question and the supplied documents.

---

## 4. Similarity Search

When a question is received:

1. The question is converted into a vector.
2. The question vector is compared with the document vectors.
3. The most similar documents are retrieved.
4. The retrieved documents provide relevant context for the LLM.

---

## 5. Relevant Context

Only the most relevant retrieved documents are provided to the LLM as context.

The LLM is instructed to answer using the supplied catalog information.

If the required information is not available, the application is designed to state that the information is not available in the supplied catalog.

---

## 6. Question Answering Workflow

The implemented workflow is:

```text
CSV Documents
      ↓
Vector Representation
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
ChatGroq
      ↓
Answer
```
---

## 7. Testing
Three questions were tested against the outdoor clothing catalog.
```text
Test 1
Question:

Which product provides UPF 50+ sun protection?

Answer:

SunGuard Hiking Shirt.

Result: Passed

Test 2
Question:

Which clothing item is designed for heavy rain and windy mountain conditions?

Answer:

Alpine Shield Jacket.

Result: Passed

Test 3
Question:

Which product is suitable for cold-weather hiking and provides insulation?

Answer:

Explorer Fleece.

Result: Passed
```
---

## 8. Key Learning Outcomes

- Learned how document-based question answering works.

- Loaded sample data from a CSV file.

- Created numerical representations of documents.

- Used similarity search to retrieve relevant information.

- Passed retrieved context to an LLM.

- Tested multiple questions against supplied information.

- Built a basic retrieval-based Q&A workflow.
---

## 9. Files in This Practice
```text
Question_and_Answer_LangChain/
├── qa_over_documents.py
├── OutdoorClothingCatalog.csv
├── test_questions.md
├── learning_notes.md
├── requirements.txt
├── .env
└── .gitignore
```