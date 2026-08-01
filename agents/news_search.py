"""
====================================================
GNews Search Agent

Author : Sugumar R
====================================================
"""

import os
import requests
from dotenv import load_dotenv

# ====================================================
# Load Environment Variables
# ====================================================

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")


# ====================================================
# Search Latest News
# ====================================================

def search_news(topic: str):

    # Check API Key
    if not GNEWS_API_KEY:
        print("ERROR: GNEWS_API_KEY not found.")
        return None

    try:

        url = (
            "https://gnews.io/api/v4/search"
            f"?q={topic}"
            "&lang=en"
            "&country=in"
            "&max=1"
            f"&apikey={GNEWS_API_KEY}"
        )

        print("=" * 60)
        print("Searching Topic :", topic)
        print("Request URL :", url.replace(GNEWS_API_KEY, "********"))
        print("=" * 60)

        response = requests.get(url, timeout=20)

        print("HTTP Status :", response.status_code)

        response.raise_for_status()

        data = response.json()

        print("API Response :", data)

        articles = data.get("articles", [])

        if not articles:

            print("No articles returned from GNews.")

            return None

        article = articles[0]

        result = {

            "title": article.get("title", ""),

            "description": article.get("description", ""),

            "content": article.get("content", ""),

            "url": article.get("url", ""),

            "image": article.get("image", ""),

            "published": article.get("publishedAt", ""),

            "source": article.get("source", {}).get("name", "")

        }

        print("=" * 60)
        print("News Found Successfully")
        print("Title :", result["title"])
        print("=" * 60)

        return result

    except requests.exceptions.HTTPError as e:

        print("HTTP Error :", e)

        try:
            print("Response :", response.text)
        except:
            pass

        return None

    except requests.exceptions.ConnectionError:

        print("Connection Error")

        return None

    except requests.exceptions.Timeout:

        print("Request Timeout")

        return None

    except Exception as e:

        print("Unexpected Error :", str(e))

        return None
