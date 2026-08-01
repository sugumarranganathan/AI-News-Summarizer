"""
====================================================
GNews Search Agent

Purpose:
    Search latest news using GNews API.

Features
---------
✔ Search Intelligence
✔ Query Normalization
✔ Query Expansion
✔ Smart Keyword Mapping

Author : Sugumar R
====================================================
"""

# ====================================================
# Import Libraries
# ====================================================

import os
import re
import requests

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from zoneinfo import ZoneInfo

from dotenv import load_dotenv


# ====================================================
# Load Environment Variables
# ====================================================

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")


# ====================================================
# Validate API Key
# ====================================================

if not GNEWS_API_KEY:

    raise ValueError(

        "GNEWS_API_KEY not found in .env file."

    )


# ====================================================
# Search Intelligence
# ====================================================

SEARCH_ALIASES = {

    # ----------------------------------------------
    # India
    # ----------------------------------------------

    "india": "India",

    "bharat": "India",

    # ----------------------------------------------
    # Tamil Nadu
    # ----------------------------------------------

    "tamilnadu": "Tamil Nadu",

    "tamil nadu": "Tamil Nadu",

    "tn": "Tamil Nadu",

    # ----------------------------------------------
    # Cities
    # ----------------------------------------------

    "madras": "Chennai",

    "bombay": "Mumbai",

    "bangalore": "Bengaluru",

    "calcutta": "Kolkata",

    # ----------------------------------------------
    # Countries
    # ----------------------------------------------

    "usa": "United States",

    "us": "United States",

    "uk": "United Kingdom",

    "uae": "United Arab Emirates",

    # ----------------------------------------------
    # Politics
    # ----------------------------------------------

    "pm": "Prime Minister",

    "cm": "Chief Minister",

    # ----------------------------------------------
    # Technology
    # ----------------------------------------------

    "ai": "Artificial Intelligence",

}


# ====================================================
# Ignore Words
# ====================================================

REMOVE_WORDS = {

    "news",

    "latest",

    "today",

    "headline",

    "headlines",

    "breaking",

    "live",

    "update",

    "updates",

}


# ====================================================
# Normalize User Query
# ====================================================

def normalize_query(query: str):

    """
    Convert user query into
    search-friendly format.
    """

    if not query:

        return ""

    query = query.lower().strip()

    query = re.sub(

        r"\s+",

        " ",

        query

    )

    words = []

    for word in query.split():

        if word in REMOVE_WORDS:

            continue

        word = SEARCH_ALIASES.get(

            word,

            word

        )

        words.append(

            word

        )

    query = " ".join(

        words

    )

    return query.strip()




# ====================================================
# Expand Search Query
# ====================================================

def expand_query(query: str):

    """
    Google-like Search Intelligence
    """

    query = normalize_query(query)

    queries = [query]

    lower = query.lower()

    # =================================================
    # Location
    # =================================================

    if "tamil nadu" in lower:

        queries.extend([
            "Tamil Nadu",
            "Chennai",
            "Tamil Nadu Politics",
            "Tamil Nadu Government",
            "Tamil Nadu Latest"
        ])

    if "chennai" in lower:

        queries.extend([
            "Chennai",
            "Greater Chennai",
            "Tamil Nadu"
        ])

    if "india" in lower:

        queries.extend([
            "India",
            "India Politics",
            "India Economy",
            "New Delhi"
        ])

    if "world" in lower:

        queries.extend([
            "World",
            "International"
        ])

    # =================================================
    # Cinema
    # =================================================

    if any(word in lower for word in [
        "cinema",
        "movie",
        "film",
        "kollywood",
        "actor",
        "actress"
    ]):

        queries.extend([
            "Tamil Cinema",
            "Kollywood",
            "Tamil Movie",
            "Cinema",
            "Film"
        ])

    # =================================================
    # Politics
    # =================================================

    if any(word in lower for word in [
        "politics",
        "government",
        "election",
        "cm",
        "pm",
        "minister"
    ]):

        queries.extend([
            "Politics",
            "Election",
            "Government"
        ])

    # =================================================
    # Cricket
    # =================================================

    if "cricket" in lower:

        queries.extend([
            "Cricket",
            "India Cricket",
            "ICC",
            "IPL"
        ])

    # =================================================
    # Sports
    # =================================================

    if "sports" in lower:

        queries.extend([
            "Sports",
            "Cricket",
            "Football",
            "Tennis",
            "Olympics"
        ])

    # =================================================
    # Business
    # =================================================

    if any(word in lower for word in [
        "business",
        "economy",
        "stock",
        "share",
        "market"
    ]):

        queries.extend([
            "Business",
            "Economy",
            "Stock Market",
            "Sensex",
            "Nifty"
        ])

    # =================================================
    # Technology
    # =================================================

    if any(word in lower for word in [
        "technology",
        "tech",
        "ai",
        "artificial intelligence"
    ]):

        queries.extend([
            "Technology",
            "Artificial Intelligence",
            "OpenAI",
            "Google AI",
            "Microsoft AI"
        ])

    # =================================================
    # Weather
    # =================================================

    if any(word in lower for word in [
        "weather",
        "rain",
        "cyclone",
        "storm"
    ]):

        queries.extend([
            "Weather",
            "Rain",
            "Cyclone",
            "IMD"
        ])

    # =================================================
    # Health
    # =================================================

    if any(word in lower for word in [
        "health",
        "hospital",
        "medical",
        "covid",
        "diabetes"
    ]):

        queries.extend([
            "Health",
            "Medical",
            "Hospital"
        ])

    # =================================================
    # Education
    # =================================================

    if any(word in lower for word in [
        "education",
        "school",
        "college",
        "university",
        "exam"
    ]):

        queries.extend([
            "Education",
            "School",
            "College",
            "University"
        ])

    # =================================================
    # Remove duplicates
    # =================================================

    unique = []

    seen = set()

    for item in queries:

        item = item.strip()

        if not item:

            continue

        key = item.lower()

        if key in seen:

            continue

        seen.add(key)

        unique.append(item)

    return unique
# ====================================================
# Format Date & Time
# ====================================================

def format_datetime(date_string: str):

    """
    Convert UTC time into IST
    and calculate relative time.
    """

    try:

        utc = datetime.fromisoformat(

            date_string.replace(

                "Z",

                "+00:00"

            )

        )

        ist = utc.astimezone(

            ZoneInfo(

                "Asia/Kolkata"

            )

        )

        published_date = ist.strftime(

            "%d %b %Y"

        )

        published_time = ist.strftime(

            "%I:%M %p IST"

        )

        now = datetime.now(

            ZoneInfo(

                "Asia/Kolkata"

            )

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
# Build GNews URL
# ====================================================

def build_url(

    query: str,

    page: int,

    from_date: str

):

    return (

        "https://gnews.io/api/v4/search"

        f"?q={query}"

        "&lang=en"

        "&country=in"

        "&max=10"

        "&sortby=publishedAt"

        f"&page={page}"

        f"&from={from_date}"

        f"&apikey={GNEWS_API_KEY}"

    )


# ====================================================
# Fetch Articles
# ====================================================

def fetch_articles(

    query: str,

    page: int = 1

):

    from_date = (

        datetime.now(

            timezone.utc

        )

        - timedelta(

            days=1

        )

    ).strftime(

        "%Y-%m-%dT%H:%M:%SZ"

    )

    url = build_url(

        query,

        page,

        from_date

    )

    print("=" * 70)

    print("Searching :", query)

    print("Page :", page)

    print("From :", from_date)

    print(

        "URL :",

        url.replace(

            GNEWS_API_KEY,

            "********"

        )

    )

    print("=" * 70)

    try:

        response = requests.get(

            url,

            timeout=20

        )

        print(

            "HTTP Status :",

            response.status_code

        )

        response.raise_for_status()

        data = response.json()

        articles = data.get(

            "articles",

            []

        )

        print(

            "Articles Found :",

            len(

                articles

            )

        )

        return articles

    except requests.exceptions.HTTPError as e:

        print(

            "HTTP Error :",

            e

        )

        return []

    except requests.exceptions.ConnectionError:

        print(

            "Connection Error"

        )

        return []

    except requests.exceptions.Timeout:

        print(

            "Request Timeout"

        )

        return []

    except Exception as e:

        print(

            "Unexpected Error :",

            str(e)

        )

        return []

# ====================================================
# Search Articles
# ====================================================

def search_articles(

    topic: str,

    page: int = 1

):

    """
    Search multiple related queries
    and return unique latest articles.
    """

    queries = expand_query(

        topic

    )

    print("=" * 70)

    print("Original Search :", topic)

    print("Expanded Queries")

    for query in queries:

        print("•", query)

    print("=" * 70)

    all_articles = []

    for query in queries:

        articles = fetch_articles(

            query,

            page

        )

        if articles:

            all_articles.extend(

                articles

            )

    if not all_articles:

        print("No articles found.")

        return []

    # ====================================================
# Calculate Relevance Score
# ====================================================

def calculate_score(article, query):

    score = 0

    title = article.get("title", "").lower()

    description = article.get("description", "").lower()

    content = article.get("content", "").lower()

    query_words = query.lower().split()

    for word in query_words:

        if word in title:

            score += 20

        if word in description:

            score += 10

        if word in content:

            score += 5

    return score

    # ----------------------------------------
    # Remove Duplicate Articles
    # ----------------------------------------

    unique_articles = {}

    for article in all_articles:

        url = article.get(

            "url"

        )

        if url:

            unique_articles[url] = article

    articles = list(

        unique_articles.values()

    )

    # ----------------------------------------
    # Sort Latest First
    # ----------------------------------------

    articles.sort(

        key=lambda article:

        article.get(

            "publishedAt",

            ""

        ),

        reverse=True

    )

    print("=" * 70)

    print(

        "Total Articles :",

        len(

            articles

        )

    )

    print("=" * 70)

    return articles

# ====================================================
# Search News
# ====================================================

def search_news(
    topic: str,
    page: int = 1
):

    """
    Return the latest news article.
    """

    articles = search_articles(
        topic,
        page
    )

    if not articles:

        return None

    for article in articles:

    article["score"] = calculate_score(

        article,

        topic

    )

articles.sort(

    key=lambda article: (

        article["score"],

        article.get(

            "publishedAt",

            ""

        )

    ),

    reverse=True

)

article = articles[0]

    published = format_datetime(

        article.get(

            "publishedAt",

            ""

        )

    )

    result = {

        "title": article.get(

            "title",

            ""

        ),

        "description": article.get(

            "description",

            ""

        ),

        "content": article.get(

            "content",

            ""

        ),

        "url": article.get(

            "url",

            ""

        ),

        "image": article.get(

            "image"

        ) or "https://placehold.co/1200x500?text=No+Image",

        "source": article.get(

            "source",

            {}

        ).get(

            "name",

            "Unknown"

        ),

        "published_date": published["date"],

        "published_time": published["time"],

        "published_ago": published["ago"]

    }

    return result



