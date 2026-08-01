"""
====================================================
AI News Summarizer & Tamil Translator
FastAPI Main Application

Author : Sugumar R
====================================================
"""

import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from agents.workflow import run_workflow

# ====================================================
# FastAPI App
# ====================================================

app = FastAPI(

    title="AI News Summarizer & Tamil Translator",

    description="Multi-Agent AI News Summarizer using AutoGen, Groq and GNews",

    version="3.1.0"

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

        request=request,

        name="index.html",

        context={}

    )

# ====================================================
# AI News Workflow API
# ====================================================

@app.post("/summarize")
async def summarize(data: dict):

    # ---------------------------------------
    # User Input
    # ---------------------------------------

    topic = data.get("topic", "").strip()

    page = int(data.get("page", 1))

    # ---------------------------------------
    # Validation
    # ---------------------------------------

    if topic == "":

        return JSONResponse(

            status_code=400,

            content={

                "error": "Please enter a news topic."

            }

        )

    # ---------------------------------------
    # Run Multi-Agent Workflow
    # ---------------------------------------

    try:

        result = await run_workflow(

            topic=topic,

            page=page

        )

        return JSONResponse(

            status_code=200,

            content=result

        )

    except Exception as e:

        print("=" * 60)
        print("APPLICATION ERROR")
        print(str(e))
        print("=" * 60)

        return JSONResponse(

            status_code=500,

            content={

                "error": str(e)

            }

        )

# ====================================================
# Health Check
# ====================================================

@app.get("/health")
async def health():

    return {

        "status": "running",

        "application": "AI News Summarizer",

        "version": "3.1.0",

        "workflow": "News → Summarizer → Translator"

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
