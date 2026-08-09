# AI Research Assistant

A multi-source research assistant that decomposes complex questions, retrieves evidence from public research sources, and produces cited, structured summaries.

## Highlights
- Query decomposition and multi-step research workflow
- Wikipedia and arXiv retrieval
- Source prioritization and evidence extraction
- Local caching to reduce repeated requests
- Streaming responses through a lightweight UI
- Modular architecture designed for additional sources

## Architecture

```text
User Query
   ↓
Query Planner
   ↓
Source Router ──→ Wikipedia
   │
   └────────────→ arXiv
   ↓
Content Extraction
   ↓
Evidence Ranking
   ↓
Answer Generation
   ↓
Cited Research Summary
```

## Tech Stack
Python · LangGraph · LLMs · Streamlit · REST APIs · Caching

## Project structure

```text
ai-research-assistant/
├── app/
│   ├── planner.py
│   ├── retrieval.py
│   ├── ranking.py
│   └── pipeline.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## Running locally

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

> Configure your own model/API credentials through environment variables. Do not commit secrets.

## Engineering decisions
The system separates planning, retrieval, ranking, and generation so each stage can be tested independently and new sources can be added without rewriting the complete pipeline.

## Status
Portfolio project — source code and integrations can be extended with additional research providers.
