"""
====================================================
AI News Summarizer & Tamil Translator
FastAPI Main Application

Author : Sugumar R
====================================================
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from agents.workflow import run_workflow

# ====================================================
# FastAPI App
# ====================================================

app = FastAPI(
    title="AI News Summarizer",
    description="Multi-Agent AI News Summarizer & Tamil Translator",
    version="1.0.0"
)

# ====================================================
# Static Files
# ====================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# ====================================================
# Templates
# ====================================================

templates = Jinja2Templates(
    directory="templates"
)

# ====================================================
# Home Page
# ====================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

# ====================================================
# AI Workflow API
# ====================================================

@app.post("/summarize")
async def summarize(data: dict):

    topic = data.get("topic", "").strip()

    if topic == "":

        return {

            "news": "Please enter a news topic.",

            "summary": "",

            "translation": "",

            "image": "",

            "url": "",

            "source": "",

            "published": ""

        }

    result = await run_workflow(topic)

    return result

# ====================================================
# Health Check
# ====================================================

@app.get("/health")
async def health():

    return {

        "status": "running",

        "application": "AI News Summarizer",

        "version": "1.0.0"

    }

# ====================================================
# Run Application
# ====================================================

if __name__ == "__main__":

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
