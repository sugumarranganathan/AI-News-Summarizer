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

                "news": "No news found.",

                "summary": "No summary available.",

                "translation": "செய்தி கிடைக்கவில்லை.",

                "image": "",

                "url": "",

                "source": "",

                "published": ""

            }

        # ===========================================
        # Build News Text
        # ===========================================

        news_text = f"""
Title:
{article.get('title', '')}

Description:
{article.get('description', '')}

Content:
{article.get('content', '')}
"""

        # ===========================================
        # Step 2 : Summarizer
        # ===========================================

        summary_result = await summarizer.run(
            task=news_text
        )

        summary = summary_result.messages[-1].content

        # ===========================================
        # Step 3 : Translator
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

            "published": article.get("published", "")

        }

    except Exception as e:

        return {

            "news": "",

            "summary": "",

            "translation": "",

            "image": "",

            "url": "",

            "source": "",

            "published": "",

            "error": str(e)

        }
