---
title: "Semantic Search from Scratch"
subtitle: "Build a Working Semantic Search Engine with Pure Python and NumPy"
author: "Ahmed Adawy"
version: "1.0"
category: "Artificial Intelligence"
tags: ["AI", "Semantic Search", "Embeddings", "NumPy", "Python", "RAG"]
language: "en"
license: "MIT"
difficulty: "Intermediate"
---

# Semantic Search from Scratch

## Build a Working Semantic Search Engine with Pure Python and NumPy

Modern AI systems can retrieve information by meaning rather than by exact keyword matches. Under the hood, one of the fundamental ideas behind this capability is surprisingly simple:

**represent information as vectors, measure similarity, and rank the results.**

In this capsule, we will build that core idea ourselves using Python and NumPy.

We will deliberately avoid vector databases, machine-learning frameworks, and high-level retrieval libraries. The objective is not to build a production search platform. The objective is to understand the mechanism that those systems build upon.

By the end, you will have a small semantic-search engine that can turn documents into vectors, compare a query against those vectors, and return the most relevant documents.

---

# 1. From Keywords to Meaning

Traditional keyword search looks for matching words.

Suppose our documents contain:

- "Python is a programming language."
- "NumPy provides fast numerical operations."
- "Neural networks learn patterns from data."

A keyword search for:

> programming language

can easily find the first document because the words occur directly.

But semantic search aims at a different question:

> Which documents are conceptually closest to this query?

This distinction becomes important when the query and the document use different words to express related ideas.

The key technique is to represent text as a numerical vector.

Instead of thinking of a sentence only as text:

```text
Python is a programming language.
```

we eventually want a representation that looks conceptually like:

```text
[0.21, -0.08, 0.73, 0.14, ...]
```

The individual dimensions are not normally meaningful to a human. What matters is the geometry of the resulting vectors.

Similar meanings should produce vectors that are close according to an appropriate similarity measure.

---

# 2. Vectors as Representations

A vector is simply an ordered collection of numbers.

In NumPy:

```python
import numpy as np

vector = np.array([0.2, 0.7, -0.1, 0.4])

print(vector)
```

We can perform mathematical operations on vectors directly.

For example:

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])

print(a + b)
print(a * b)
```

The important idea is that a vector gives us a mathematical object that we can compare.

Once documents and queries are represented as vectors, semantic retrieval becomes a geometry problem.

---

# 3. Measuring Similarity

One of the most common similarity measures for embeddings is **cosine similarity**.

The formula is:

\[
\cos(\theta) =
\frac{A \cdot B}
{\|A\|\|B\|}
\]

where:

- \(A \cdot B\) is the dot product.
- \(\|A\|\) is the magnitude of vector \(A\).
- \(\|B\|\) is the magnitude of vector \(B\).

The result is related to the angle between the two vectors.

For normalized vectors:

- a value close to `1` indicates strong directional similarity,
- a value close to `0` indicates little directional similarity,
- a value close to `-1` indicates opposite direction.

Let's implement it ourselves.

```python
import numpy as np


def cosine_similarity(a, b):
    numerator = np.dot(a, b)
    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return numerator / denominator
```

Test it:

```python
a = np.array([1.0, 0.0, 1.0])
b = np.array([1.0, 0.0, 1.0])
c = np.array([-1.0, 0.0, -1.0])

print(cosine_similarity(a, b))
print(cosine_similarity(a, c))
```

The first comparison should produce a value close to `1`, while the second should be close to `-1`.

---

# 4. Where Do Embeddings Come From?

At this point we have vectors, but an important question remains:

**How do we turn text into meaningful vectors?**

A real semantic-search system normally uses an embedding model.

An embedding model receives text and produces a high-dimensional numerical representation:

```text
text
  |
  v
embedding model
  |
  v
vector
```

For example:

```text
"Python is used for machine learning"
                |
                v
[0.12, -0.44, 0.81, ...]
```

The model learns a representation in which semantically related text tends to occupy nearby regions of the vector space.

In this capsule, however, we will not download or depend on an embedding model.

Instead, we will construct a small deterministic demonstration embedding so that the complete retrieval pipeline remains transparent.

This distinction matters:

**our demonstration embedding is educational, not a replacement for a trained language model.**

---

# 5. A Tiny Embedding Demonstration

We can create a simple vocabulary and represent text using word-frequency vectors.

```python
import numpy as np


VOCABULARY = [
    "python",
    "programming",
    "machine",
    "learning",
    "data",
    "neural",
    "network",
    "database",
]


def embed(text):
    words = text.lower().split()
    vector = np.zeros(len(VOCABULARY), dtype=float)

    for word in words:
        if word in VOCABULARY:
            index = VOCABULARY.index(word)
            vector[index] += 1.0

    return vector
```

Now:

```python
text = "Python programming"
print(embed(text))
```

This gives us a vector representation.

But notice the limitation immediately.

The system does not actually understand language.

It only knows whether vocabulary terms appear.

That is exactly why modern embedding models are powerful: they learn representations that capture relationships beyond literal word overlap.

---

# 6. Building a Document Index

Now we can create a small collection of documents.

```python
documents = [
    "Python is a programming language.",
    "NumPy provides numerical operations for Python.",
    "Machine learning models learn patterns from data.",
    "Neural networks are used in modern AI systems.",
    "Databases store and retrieve structured information.",
]
```

We embed every document:

```python
document_vectors = [
    embed(document)
    for document in documents
]
```

Conceptually, our index now looks like:

```text
Document 1 -> Vector 1
Document 2 -> Vector 2
Document 3 -> Vector 3
Document 4 -> Vector 4
Document 5 -> Vector 5
```

A real vector database adds sophisticated indexing, persistence, filtering, and performance optimizations.

But the mathematical foundation is still vector comparison.

---

# 7. Searching the Index

We can now create a search function.

```python
def search(query, documents, document_vectors, top_k=3):
    query_vector = embed(query)

    scored = []

    for document, vector in zip(documents, document_vectors):
        score = cosine_similarity(query_vector, vector)
        scored.append((score, document))

    scored.sort(reverse=True)

    return scored[:top_k]
```

Run it:

```python
results = search(
    "Python programming",
    documents,
    document_vectors,
    top_k=3,
)

for score, document in results:
    print(f"{score:.4f}  {document}")
```

We have now implemented the basic retrieval loop:

```text
Query
  |
  v
Query Vector
  |
  v
Compare Against Document Vectors
  |
  v
Similarity Scores
  |
  v
Sort
  |
  v
Top-K Results
```

That is the heart of semantic retrieval.

---

# 8. Why This Is Not Yet True Semantic Search

Our example is intentionally simple.

A word-frequency vector cannot understand that:

```text
"car"
```

and

```text
"automobile"
```

can refer to closely related concepts.

It also struggles with:

- synonyms,
- context,
- word order,
- polysemy,
- paraphrasing,
- long-range relationships.

A trained embedding model addresses these limitations by learning a representation from large amounts of language data.

The production architecture becomes:

```text
Documents
    |
    v
Embedding Model
    |
    v
Dense Vectors
    |
    v
Vector Index


User Query
    |
    v
Embedding Model
    |
    v
Query Vector
    |
    v
Similarity Search
    |
    v
Top-K Documents
```

Our NumPy implementation is therefore a conceptual microscope: it exposes the mechanism without hiding it behind libraries.

---

# 9. Ranking Results

Similarity gives every document a score.

Suppose we receive:

```text
0.92  Document A
0.71  Document B
0.44  Document C
0.18  Document D
```

The search engine can rank documents from highest similarity to lowest.

This is where retrieval becomes useful to downstream AI systems.

For example, a RAG pipeline can take the top documents and place them into the context supplied to a language model.

The overall flow becomes:

```text
User Question
      |
      v
Query Embedding
      |
      v
Vector Search
      |
      v
Relevant Documents
      |
      v
Prompt Construction
      |
      v
Language Model
      |
      v
Generated Answer
```

Semantic search is therefore not merely a standalone feature.

It can become the retrieval layer of a larger AI system.

---

# 10. The Importance of Top-K Retrieval

Returning every document is usually unnecessary.

Instead, we select the most relevant `k` results.

For example:

```python
top_k = 5
```

means:

> return only the five highest-scoring documents.

This has two benefits.

First, it reduces the amount of irrelevant information passed downstream.

Second, when semantic search is used with an LLM, fewer but more relevant documents can make the final context more focused.

However, `top_k` is not a magic number.

A larger value can improve recall but increase noise and computational cost.

A smaller value can improve precision but may exclude useful evidence.

Production systems often tune retrieval parameters experimentally.

---

# 11. A Complete Minimal Example

Here is the complete educational implementation in one place.

```python
import numpy as np


VOCABULARY = [
    "python",
    "programming",
    "machine",
    "learning",
    "data",
    "neural",
    "network",
    "database",
]


def embed(text):
    words = text.lower().split()
    vector = np.zeros(len(VOCABULARY), dtype=float)

    for word in words:
        if word in VOCABULARY:
            vector[VOCABULARY.index(word)] += 1.0

    return vector


def cosine_similarity(a, b):
    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return np.dot(a, b) / denominator


def search(query, documents, top_k=3):
    query_vector = embed(query)

    scored = []

    for document in documents:
        document_vector = embed(document)
        score = cosine_similarity(query_vector, document_vector)
        scored.append((score, document))

    scored.sort(reverse=True)

    return scored[:top_k]


documents = [
    "Python is a programming language.",
    "NumPy provides numerical operations for Python.",
    "Machine learning models learn patterns from data.",
    "Neural networks are used in modern AI systems.",
    "Databases store and retrieve structured information.",
]


results = search(
    "Python programming",
    documents,
    top_k=3,
)


for score, document in results:
    print(f"{score:.4f}  {document}")
```

This is deliberately small.

Its value is not production performance.

Its value is that every major operation is visible.

---

# 12. From This Prototype to Production

A production semantic-search system would replace several parts of our demonstration.

### Our prototype

```text
Simple vocabulary
       |
       v
Word-count vectors
       |
       v
Cosine similarity
       |
       v
Linear scan
```

### A production system

```text
Embedding Model
       |
       v
Dense Embeddings
       |
       v
Vector Database / ANN Index
       |
       v
Similarity Search
       |
       v
Filtering + Ranking
       |
       v
Retrieved Context
```

Typical production improvements include:

- stronger embedding models,
- normalized embeddings,
- approximate nearest-neighbor indexes,
- metadata filtering,
- document chunking,
- hybrid keyword + vector search,
- reranking,
- caching,
- evaluation datasets,
- retrieval quality metrics.

The important point is that these improvements do not erase the underlying mathematics.

They build on it.

---

# 13. What We Actually Built

Let's step back.

We started with plain text.

Then we created numerical representations.

We implemented cosine similarity.

We indexed documents.

We embedded a query.

We calculated similarity scores.

We ranked the results.

And finally, we connected retrieval to the architecture of a RAG system.

The complete conceptual chain is:

```text
Text
  â†“
Vector Representation
  â†“
Vector Similarity
  â†“
Ranking
  â†“
Retrieval
  â†“
Context
  â†“
AI Application
```

That chain is one of the foundational ideas behind modern retrieval-based AI systems.

---

# 14. Final Perspective

The most important lesson is not the specific Python code.

It is the mental model.

When you see a modern AI product advertising semantic search, vector search, embeddings, or RAG, you should be able to recognize the architecture hiding underneath the abstraction.

At its core, the system is doing something remarkably concrete:

**represent information numerically, compare representations, and retrieve the most relevant information.**

Production systems make this process dramatically more sophisticated.

But the foundation remains mathematical.

And once you understand that foundation, the black box becomes much less mysterious.

---

# Exercises

## Exercise 1 â€” Add More Vocabulary

Extend `VOCABULARY` with at least five additional concepts and test new queries.

## Exercise 2 â€” Normalize the Embeddings

Modify `embed()` so that non-zero vectors are normalized.

Compare the retrieval scores before and after normalization.

## Exercise 3 â€” Add Metadata

Represent each document as a dictionary containing:

```python
{
    "text": "...",
    "category": "...",
    "source": "..."
}
```

Modify the search function so that results include their metadata.

## Exercise 4 â€” Add a Similarity Threshold

Modify the search function to discard documents whose similarity score is below a configurable threshold.

## Exercise 5 â€” Think Like a Systems Engineer

Imagine that the document collection grows from five documents to five million.

Ask yourself:

> Would scanning every vector still be practical?

That question leads directly to approximate nearest-neighbor search and vector indexing.

---

# Conclusion

You have now built a miniature retrieval system from first principles.

It is intentionally simple, but the architecture exposes the essential idea:

**text â†’ vectors â†’ similarity â†’ ranking â†’ retrieval**

That foundation appears repeatedly in modern AI engineering, from semantic search to recommendation systems and Retrieval-Augmented Generation.

The next step is to replace our educational embedding function with a real embedding model and connect the retrieval layer to a production-oriented RAG pipeline.

Once you understand the small system, the large systems become easier to reason about.
