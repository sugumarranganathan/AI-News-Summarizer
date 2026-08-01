import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def search_news(topic):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}"
        f"&language=en"
        f"&sortBy=publishedAt"
        f"&pageSize=1"
        f"&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    if data["status"] != "ok":
        return "Unable to fetch news."

    articles = data.get("articles", [])

    if len(articles) == 0:
        return "No news found."

    article = articles[0]

    title = article.get("title", "")

    description = article.get("description", "")

    content = article.get("content", "")

    return f"""
Title:
{title}

Description:
{description}

Content:
{content}
"""
