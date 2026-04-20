from pydantic import BaseModel
from src.ollama_client import chat_json
from src.prompts import SENTIMENT_SYSTEM, SENTIMENT_USER


class SentimentResult(BaseModel):
    score: float       # -1.0 to 1.0
    label: str         # positive | negative | neutral
    reasoning: str


async def analyze_sentiment(article_text: str) -> SentimentResult:
    data = await chat_json(
        SENTIMENT_SYSTEM,
        SENTIMENT_USER.format(text=article_text[:4000]),
    )
    score = float(data.get("score", 0.0))
    score = max(-1.0, min(1.0, score))
    return SentimentResult(
        score=score,
        label=str(data.get("label", "neutral")),
        reasoning=str(data.get("reasoning", "")),
    )
