# insurancereportmcpclient — Architecture

## Purpose

MCP (Model Context Protocol) server that exposes LLM-powered tools for news analysis. The backend service calls these tools; they in turn call a locally-hosted Ollama instance running `llama3:8b`.

## Directory Structure

```
insurancereportmcpclient/
├── src/
│   ├── main.py              # MCP server entry point
│   ├── ollama_client.py     # Ollama HTTP wrapper
│   ├── prompts.py           # All system/user prompt templates
│   └── tools/
│       ├── extract_incidents.py   # Detect Guardian Insurance incidents
│       ├── analyze_sentiment.py   # Sentiment score + label
│       └── detect_rival_ads.py    # Rival insurer ad detection
├── requirements.txt
├── Dockerfile
└── ARCHITECTURE.md
```

## Tools

| Tool | Input | Output |
|---|---|---|
| `extract_incidents` | article text | `{incident: bool, summary: str, severity: low/medium/high}` |
| `analyze_sentiment` | article text | `{score: float -1..1, label: positive/negative/neutral, reasoning: str}` |
| `detect_rival_ads` | article text | `{is_rival_ad: bool, competitor: str, ad_summary: str}` |

## LLM

- **Model:** llama3:8b via Ollama REST API (`http://ollama:11434`)
- All prompts request structured JSON output
- Temperature set to 0 for deterministic extraction
