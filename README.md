# Outreach Agent

[![CI](https://github.com/kogunlowo123/outreach-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/outreach-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Sales | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Sales outreach agent that creates personalized email sequences, manages multi-channel cadences, optimizes send timing, A/B tests messaging, and tracks engagement metrics.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `create_sequence` | Create a personalized email outreach sequence |
| `personalize_message` | Personalize an outreach message using prospect research |
| `schedule_send` | Schedule outreach send at optimal time for the recipient |
| `track_engagement` | Track email opens, clicks, and replies for a sequence |
| `ab_test_messaging` | Run A/B test on subject lines or email body variations |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/outreach/execute` | Execute primary action |
| `POST` | `/api/v1/outreach/analyze` | Run analysis |
| `GET` | `/api/v1/outreach/metrics` | Get metrics |
| `PUT` | `/api/v1/outreach/configure` | Configure settings |
| `POST` | `/api/v1/outreach/report` | Generate report |

## Features

- Outreach
- Analytics
- Automation

## Integrations

- Salesforce
- Hubspot
- Outreach
- Apollo
- Linkedin Sales Navigator

## Architecture

```
outreach-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── outreach_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Sales Engagement + LLM**

---

Built as part of the Enterprise AI Agent Platform.
