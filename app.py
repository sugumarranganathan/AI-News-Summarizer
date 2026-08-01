"""
AI News Summarizer & Tamil Translator
Main Application

Author: Sugumar R
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(
    title="AI News Summarizer",
    description="Multi-Agent AI News Summarizer & Tamil Translator",
    version="1.0.0"
)

# -----------------------------
# Static Files
# -----------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# -----------------------------
# HTML Templates
# -----------------------------
templates = Jinja2Templates(directory="templates")

# -----------------------------
# Home Page
# -----------------------------
@app.post("/summarize")
async def summarize(data: dict):

    topic = data["topic"]

    # Step 1
    latest_news = search_news(topic)

    # Step 2
    result1 = await summarizer.run(
        task=latest_news
    )

    summary = result1.messages[-1].content

    # Step 3
    result2 = await translator.run(
        task=summary
    )

    tamil = result2.messages[-1].content

    return {

        "news": latest_news,

        "summary": summary,

        "translation": tamil

    }
# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/summarize")
async def summarize(data: dict):

    topic = data.get("topic", "")

    # Placeholder response
    # AutoGen + Groq integration will be added later.

    return JSONResponse(
        {
            "status": "success",
            "topic": topic,
            "news": "Latest news will appear here.",
            "summary": "AI summary will appear here.",
            "translation": "தமிழ் மொழிபெயர்ப்பு இங்கே தோன்றும்."
        }
    )

# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

