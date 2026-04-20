from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.tools.extract_incidents import extract_incidents
from src.tools.analyze_sentiment import analyze_sentiment
from src.tools.detect_rival_ads import detect_rival_ads

app = FastAPI(title="Insurance Report MCP Client")


class ArticleRequest(BaseModel):
    article_text: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/extract-incidents")
async def api_extract_incidents(body: ArticleRequest):
    try:
        result = await extract_incidents(body.article_text)
        return result.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze-sentiment")
async def api_analyze_sentiment(body: ArticleRequest):
    try:
        result = await analyze_sentiment(body.article_text)
        return result.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/detect-rival-ads")
async def api_detect_rival_ads(body: ArticleRequest):
    try:
        result = await detect_rival_ads(body.article_text)
        return result.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
