"""
====================================================
GNews Search Agent

Author : Sugumar R
====================================================
"""

import os
import requests

from datetime import datetime, timedelta, timezone
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

            value = diff.days

            unit = "day"

        elif diff.seconds >= 3600:

            value = diff.seconds // 3600

            unit = "hour"

        elif diff.seconds >= 60:

            value = diff.seconds // 60

            unit = "minute"

        else:

            return {

                "date": published_date,

                "time": published_time,

                "ago": "Just now"

            }

        return {

            "date": published_date,

            "time": published_time,

            "ago": f"{value} {unit}{'' if value == 1 else 's'} ago"

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

def search_news(topic: str, page: int = 1):

    if not GNEWS_API_KEY:

        print("ERROR : GNEWS_API_KEY not found.")

        return None

    try:

        # ----------------------------------------
        # Search only recent news (Last 24 Hours)
        # ----------------------------------------

        from_date = (

            datetime.now(timezone.utc)

            - timedelta(days=1)

        ).strftime("%Y-%m-%dT%H:%M:%SZ")

        url = (

            "https://gnews.io/api/v4/search"

            f"?q={topic}"

            "&lang=en"

            "&country=in"

            "&max=1"

            f"&page={page}"

            "&sortby=publishedAt"

            f"&from={from_date}"

            f"&apikey={GNEWS_API_KEY}"

        )

        print("=" * 70)

        print("Topic :", topic)

        print("Page :", page)

        print("Recent From :", from_date)

        print("URL :", url.replace(GNEWS_API_KEY, "********"))

        print("=" * 70)

        response = requests.get(

            url,

            timeout=20

        )

        print("HTTP Status :", response.status_code)

        response.raise_for_status()

        data = response.json()

        articles = data.get("articles", [])

        if not articles:

            print("No recent articles found.")

            return None

        article = articles[0]

        published = format_datetime(

            article.get("publishedAt", "")

        )

        result = {

            "title": article.get("title", ""),

            "description": article.get("description", ""),

            "content": article.get("content", ""),

            "url": article.get("url", ""),

            "image": article.get("image")
                     or "https://placehold.co/1200x500?text=No+Image",

            "source": article.get("source", {}).get("name", "Unknown"),

            "published_date": published["date"],

            "published_time": published["time"],

            "published_ago": published["ago"]

        }

        print("=" * 70)

        print("Latest News Found")

        print("Title :", result["title"])

        print("Source :", result["source"])

        print("Date :", result["published_date"])

        print("Time :", result["published_time"])

        print("Ago :", result["published_ago"])

        print("=" * 70)

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
