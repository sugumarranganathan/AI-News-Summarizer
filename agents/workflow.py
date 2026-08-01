"""
====================================================
Multi-Agent Workflow

News Search
      ↓
Summarizer
      ↓
Translator

Author : Sugumar R
====================================================
"""

from agents.news_search import search_news
from agents.summarizer import summarizer
from agents.translator import translator


async def run_workflow(topic: str):

    try:

        # ===========================================
        # Step 1 : Search News
        # ===========================================

        article = search_news(topic)

        if not article:

            return {

                "news": "❌ No news found.",

                "summary": "No summary available.",

                "translation": "செய்தி கிடைக்கவில்லை.",

                "image": "",

                "url": "",

                "source": "",

                "published_date": "",

                "published_time": "",

                "published_ago": ""

            }

        # ===========================================
        # News Display (Professional Format)
        # ===========================================

        news_text = f"""
📰 <strong>{article.get('title', '')}</strong>

<p>{article.get('description', '')}</p>

<p>{article.get('content', '')}</p>
"""

        # ===========================================
        # Text for AI Summarizer
        # ===========================================

        ai_input = f"""
Title:
{article.get('title', '')}

Description:
{article.get('description', '')}

Content:
{article.get('content', '')}
"""

        # ===========================================
        # Step 2 : AI Summary
        # ===========================================

        summary_result = await summarizer.run(
            task=ai_input
        )

        summary = summary_result.messages[-1].content

        # ===========================================
        # Step 3 : Tamil Translation
        # ===========================================

        tamil_result = await translator.run(
            task=summary
        )

        tamil = tamil_result.messages[-1].content

        # ===========================================
        # Final Response
        # ===========================================

        return {

            "news": news_text,

            "summary": summary,

            "translation": tamil,

            "image": article.get("image", ""),

            "url": article.get("url", ""),

            "source": article.get("source", ""),

            "published_date": article.get("published_date", ""),

            "published_time": article.get("published_time", ""),

            "published_ago": article.get("published_ago", "")

        }

    except Exception as e:

        print("Workflow Error :", str(e))

        return {

            "news": "",

            "summary": "",

            "translation": "",

            "image": "",

            "url": "",

            "source": "",

            "published_date": "",

            "published_time": "",

            "published_ago": "",

            "error": str(e)

        }
