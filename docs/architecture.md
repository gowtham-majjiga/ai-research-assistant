# Architecture

## Goal

Build a small, inspectable research system where retrieval failures do not terminate the entire workflow and ranking is deterministic.

## Pipeline

1. Normalize and decompose the user's question.
2. Route each subquery to Wikipedia and/or arXiv.
3. Retrieve source documents with request timeouts.
4. Cache successful public-source responses for six hours.
5. Deduplicate documents.
6. Score relevance using query coverage, title overlap, snippet length, and provider signals.
7. Return a structured result containing the query, subqueries, ranked evidence, and retrieval errors.
8. Streamlit renders the result and source links.

## Reliability choices

- Each provider is isolated behind a retrieval function.
- A failed provider is recorded instead of crashing the full research run.
- Network calls have explicit timeouts.
- Cache corruption is treated as a cache miss.
- Secrets are never required for public-source mode.

## Extension points

A model-backed synthesis layer can be added after ranking without changing the retrieval contracts. Additional providers can implement the same document schema.
