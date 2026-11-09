# Cisco & Zoom Documentation for Knowledge Base / Embeddings

This repository contains Markdown versions of Cisco and Zoom documentation, scraped/downloaded for use in RAG / embedding knowledge bases.

## Contents

- **zoom/**: ~218 Markdown files from Zoom Developer Docs (`developers.zoom.us/docs/*.md`). Sourced from the official `llms.txt` index. These are LLM-ready docs covering APIs, SDKs, AI Services, Meeting SDK, Video SDK, Chat, Phone, etc.
- **cisco/**: ~80 Markdown pages crawled from Cisco DevNet documentation using [Scrapling](https://scrapling.readthedocs.io/), focusing on Meraki API, NX-OS, IOS XE, Catalyst Center / DNA Center, and related developer docs.

## How it was generated

- Zoom: Direct download of `.md` endpoints listed in `https://developers.zoom.us/llms.txt`.
- Cisco: Scrapling `ContentSpider` with HTTP fetcher, starting from key DevNet hubs, limited to 80 pages for practicality.

## Usage for Embeddings

These files are clean Markdown suitable for chunking and embedding (e.g., with OpenAI, SentenceTransformers, LlamaIndex, LangChain, etc.).

Example structure:
- Preserve URL metadata if available in JSONL (`cisco/cisco_docs.jsonl`).
- Chunk by headings or fixed size with overlap.

## Expanding the corpus

To crawl more:
```bash
pip install "scrapling[rag]"
# Then customize ContentSpider start_urls, max_pages, and rules.
```

Deadline note: This is an initial dump meeting the weekend deadline. Full "all" Cisco/Zoom docs are enormous; this prioritizes developer-focused content ideal for embedding.

Generated with Scrapling and direct MD fetches.

## Update: Architecture / Solution / Platform Docs (2026-11-09)

Added high-level documents from Zoom Technical Library (library.zoom.com) to address the need for solution, architecture, and platform materials (beyond web portal / API docs):

- `zoom/technical-library/architecture/` — Architecture and Design overview, BCDR Whitepaper, Cloud Architecture Diagram, Zoom Contact Center Architecture
- `zoom/technical-library/ai/` — AI Whitepaper suite (models, diagrams, data governance, security framework, features)
- `zoom/technical-library/platform/` — Zoom Node explainer (hybrid), Technical Library overview

These are LLM-ready Markdown files. Partner portal access can still unlock additional partner-specific solution guides if needed.
