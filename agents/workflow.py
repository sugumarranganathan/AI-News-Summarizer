"""
Multi-Agent Workflow

News Search
      ↓
Summarizer
      ↓
Translator
"""

from agents.news_search import search_news
from agents.summarizer import summarizer
from agents.translator import translator


async def run_workflow(topic: str):

    # -----------------------------
    # Step 1 : Search News
    # -----------------------------

    article = search_news(topic)

    if article is None:

        return {

            "news": "No news found.",

            "summary": "No summary available.",

            "translation": "செய்தி கிடைக்கவில்லை."

        }

    # -----------------------------
    # Format News
    # -----------------------------

    news_text = f"""
Title:
{article['title']}

Description:
{article['description']}

Content:
{article['content']}
"""

    # -----------------------------
    # Step 2 : Summarize
    # -----------------------------

    result1 = await summarizer.run(
        task=news_text
    )

    summary = result1.messages[-1].content

    # -----------------------------
    # Step 3 : Translate
    # -----------------------------

    result2 = await translator.run(
        task=summary
    )

    tamil = result2.messages[-1].content

    # -----------------------------
    # Return
    # -----------------------------

    return {

        "news": news_text,

        "summary": summary,

        "translation": tamil,

        "image": article["image"],

        "url": article["url"],

        "source": article["source"],

        "published": article["published"]

    }
