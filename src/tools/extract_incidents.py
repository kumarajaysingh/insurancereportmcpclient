from pydantic import BaseModel
from src.ollama_client import chat_json
from src.prompts import INCIDENT_SYSTEM, INCIDENT_USER


class IncidentResult(BaseModel):
    incident: bool
    summary: str
    severity: str  # none | low | medium | high


async def extract_incidents(article_text: str) -> IncidentResult:
    data = await chat_json(
        INCIDENT_SYSTEM,
        INCIDENT_USER.format(text=article_text[:4000]),
    )
    return IncidentResult(
        incident=bool(data.get("incident", False)),
        summary=str(data.get("summary", "")),
        severity=str(data.get("severity", "none")),
    )
