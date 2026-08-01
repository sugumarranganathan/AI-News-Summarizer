"""
====================================================
GNews Search Agent

Author : Sugumar R
====================================================
"""

import os
import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

# ====================================================
# Load Environment Variables
# ====================================================

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")


# ====================================================
# Format Date & Time
# ====================================================

def format_datetime(date_string):

    try:

        utc = datetime.fromisoformat(
            date_string.replace("Z", "+00:00")
        )

        ist = utc.astimezone(
            ZoneInfo("Asia/Kolkata")
        )

        published_date = ist.strftime("%d %b %Y")

        published_time = ist.strftime("%I:%M %p IST")

        now = datetime.now(
            ZoneInfo("Asia/Kolkata")
        )

        diff = now - ist

        if diff.days > 0:

            published_ago = f"{diff.days} day(s) ago"

        elif diff.seconds >= 3600:

            published_ago = f"{diff.seconds // 3600} hour(s) ago"

        elif diff.seconds >= 60:

            published_ago = f"{diff.seconds // 60} minute(s) ago"

        else:

            published_ago = "Just now"

        return {

            "date": published_date,

            "time": published_time,

            "ago": published_ago

        }

    except Exception:

        return {

            "date": "",

            "time": "",

            "ago": ""

        }


# ====================================================
# Search Latest News
# ====================================================

def search_news(topic: str):

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

        articles = data.get("articles", [])

        if not articles:

            print("No articles returned from GNews.")

            return None

        article = articles[0]

        # ===========================================
        # Format Published Date & Time
        # ===========================================

        published = format_datetime(
            article.get("publishedAt", "")
        )

        result = {

            "title": article.get("title", ""),

            "description": article.get("description", ""),

            "content": article.get("content", ""),

            "url": article.get("url", ""),

            "image": article.get("image", ""),

            "source": article.get("source", {}).get("name", ""),

            "published_date": published["date"],

            "published_time": published["time"],

            "published_ago": published["ago"]

        }

        print("=" * 60)
        print("News Found Successfully")
        print("Title :", result["title"])
        print("Published :", result["published_date"])
        print("Time :", result["published_time"])
        print("Ago :", result["published_ago"])
        print("=" * 60)

        return result

    except requests.exceptions.HTTPError as e:

        print("HTTP Error :", e)

        try:
            print(response.text)
        except Exception:
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
