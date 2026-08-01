"""
====================================================
GNews Search Agent

Author : Sugumar R
====================================================
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")


def search_news(topic: str):

    try:

        url = (
            "https://gnews.io/api/v4/search"
            f"?q={topic}"
            "&lang=en"
            "&country=in"
            "&max=1"
            f"&apikey={GNEWS_API_KEY}"
        )

        response = requests.get(url, timeout=15)

        response.raise_for_status()

        data = response.json()

        articles = data.get("articles", [])

        if not articles:

            return None

        article = articles[0]

        return {

            "title": article.get("title", ""),

            "description": article.get("description", ""),

            "content": article.get("content", ""),

            "url": article.get("url", ""),

            "image": article.get("image", ""),

            "published": article.get("publishedAt", ""),

            "source": article.get("source", {}).get("name", "")

        }

    except Exception as e:

        print(f"GNews Error : {e}")

        return None
