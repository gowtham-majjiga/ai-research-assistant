# AI Research Assistant

An evidence-first multi-source research assistant built around query decomposition, provider routing, retrieval, caching, deduplication, deterministic relevance ranking, and a Streamlit research interface.

## Why this project is interesting

Instead of treating an LLM as the whole application, the system separates the engineering concerns around a research workflow:

```text
User Question
      ↓
Query Planner
      ↓
Provider Router
   ↙        ↘
Wikipedia   arXiv
   ↘        ↙
  Retrieval + Cache
        ↓
 Deduplication
        ↓
 Relevance Ranking
        ↓
 Structured Evidence
        ↓
 Streamlit UI
```

## Features

- Multi-source retrieval from Wikipedia and arXiv
- Query decomposition for compound questions
- Provider routing based on query intent
- Six-hour local response cache
- Duplicate-source elimination
- Transparent relevance scoring
- Failure isolation between providers
- Network timeouts
- Structured research results
- Unit tests for planning, ranking, and caching
- Docker-ready deployment

## Tech stack

Python · Streamlit · REST APIs · XML parsing · pytest · Docker

## Run locally

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

## Test

```bash
pytest -q
```

## Docker

```bash
docker build -t ai-research-assistant .
docker run -p 8501:8501 ai-research-assistant
```

## Example questions

- Compare retrieval-augmented generation with fine-tuning.
- What are transformer architectures and their applications?
- Research database indexing algorithms.
- Compare CNN and LSTM approaches.

## Project structure

```text
├── app.py
├── app/
│   ├── cache.py
│   ├── models.py
│   ├── planner.py
│   ├── retrieval.py
│   ├── ranking.py
│   └── pipeline.py
├── tests/
├── docs/
│   ├── architecture.md
│   └── design-decisions.md
├── Dockerfile
├── .env.example
├── requirements.txt
└── README.md
```

## Engineering notes

The application is deliberately modular. A future LLM synthesis component can consume the ranked evidence without changing the retrieval layer, and additional sources can be added behind the same document contract.

## Important

Do not commit API keys, personal credentials, or local cache files.
