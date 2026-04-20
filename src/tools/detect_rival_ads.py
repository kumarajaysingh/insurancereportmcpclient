from pydantic import BaseModel
from src.ollama_client import chat_json
from src.prompts import RIVAL_AD_SYSTEM, RIVAL_AD_USER


class RivalAdResult(BaseModel):
    is_rival_ad: bool
    competitor: str
    ad_summary: str


async def detect_rival_ads(article_text: str) -> RivalAdResult:
    data = await chat_json(
        RIVAL_AD_SYSTEM,
        RIVAL_AD_USER.format(text=article_text[:4000]),
    )
    return RivalAdResult(
        is_rival_ad=bool(data.get("is_rival_ad", False)),
        competitor=str(data.get("competitor", "")),
        ad_summary=str(data.get("ad_summary", "")),
    )
