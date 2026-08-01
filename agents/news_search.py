"""
====================================================
GNews Search Agent

Purpose:
    Search latest news using GNews API.

Features
--------
✔ Google-like Search
✔ Query Normalization
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

from dotenv import load_dotenv

from datetime import (
    datetime,
    timedelta,
    timezone,
)

from zoneinfo import ZoneInfo


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

        "GNEWS_API_KEY not found in .env"

    )


# ====================================================
# Search Alias Dictionary
# ====================================================

SEARCH_ALIASES = {

    # India

    "india": "India",

    "bharat": "India",

    # Tamil Nadu

    "tamilnadu": "Tamil Nadu",

    "tn": "Tamil Nadu",

    # Cities

    "madras": "Chennai",

    "bombay": "Mumbai",

    "bangalore": "Bengaluru",

    "calcutta": "Kolkata",

    # Countries

    "usa": "United States",

    "us": "United States",

    "uk": "United Kingdom",

    "uae": "United Arab Emirates",

    # Politics

    "pm": "Prime Minister",

    "cm": "Chief Minister",

    # Technology

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

def normalize_query(query: str) -> str:

    """
    Normalize the user search query.

    Example

    Tamilnadu news
            ↓
    Tamil Nadu

    AI latest news
            ↓
    Artificial Intelligence
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

        words.append(

            SEARCH_ALIASES.get(

                word,

                word

            )

        )

    query = " ".join(

        words

    )

    return query.strip()

# ====================================================
# Expand Search Query
# ====================================================

def expand_query(query: str) -> list:

    """
    Expand user query into multiple
    related search queries.
    """

    query = normalize_query(query)

    queries = [

        query

    ]

    lower = query.lower()

    # ====================================================
    # Location
    # ====================================================

    if "tamil nadu" in lower:

        queries.extend([

            "Tamil Nadu",

            "Chennai",

            "Tamil Nadu Politics",

            "Tamil Nadu Government",

            "Tamil Nadu Latest",

        ])

    if "chennai" in lower:

        queries.extend([

            "Chennai",

            "Greater Chennai",

            "Tamil Nadu",

        ])

    if "india" in lower:

        queries.extend([

            "India",

            "India Politics",

            "India Economy",

            "New Delhi",

        ])

    if "world" in lower:

        queries.extend([

            "World",

            "International",

        ])

    # ====================================================
    # Entertainment
    # ====================================================

    if any(word in lower for word in [

        "cinema",

        "movie",

        "film",

        "kollywood",

        "actor",

        "actress",

    ]):

        queries.extend([

            "Tamil Cinema",

            "Kollywood",

            "Tamil Movie",

            "Cinema",

            "Film",

        ])

    # ====================================================
    # Politics
    # ====================================================

    if any(word in lower for word in [

        "politics",

        "government",

        "minister",

        "cm",

        "pm",

        "election",

    ]):

        queries.extend([

            "Politics",

            "Election",

            "Government",

        ])

    # ====================================================
    # Sports
    # ====================================================

    if any(word in lower for word in [

        "sports",

        "cricket",

        "football",

        "tennis",

        "ipl",

    ]):

        queries.extend([

            "Sports",

            "Cricket",

            "India Cricket",

            "IPL",

            "ICC",

        ])

    # ====================================================
    # Technology
    # ====================================================

    if any(word in lower for word in [

        "technology",

        "tech",

        "artificial intelligence",

        "ai",

        "openai",

        "google",

    ]):

        queries.extend([

            "Technology",

            "Artificial Intelligence",

            "OpenAI",

            "Google AI",

            "Microsoft AI",

        ])

    # ====================================================
    # Business
    # ====================================================

    if any(word in lower for word in [

        "business",

        "economy",

        "market",

        "stock",

        "share",

    ]):

        queries.extend([

            "Business",

            "Economy",

            "Stock Market",

            "Sensex",

            "Nifty",

        ])

    # ====================================================
    # Weather
    # ====================================================

    if any(word in lower for word in [

        "weather",

        "rain",

        "cyclone",

        "storm",

        "flood",

    ]):

        queries.extend([

            "Weather",

            "Rain",

            "Cyclone",

            "IMD",

        ])

    # ====================================================
    # Health
    # ====================================================

    if any(word in lower for word in [

        "health",

        "medical",

        "hospital",

        "covid",

        "diabetes",

    ]):

        queries.extend([

            "Health",

            "Medical",

            "Hospital",

        ])

    # ====================================================
    # Education
    # ====================================================

    if any(word in lower for word in [

        "education",

        "school",

        "college",

        "university",

        "exam",

    ]):

        queries.extend([

            "Education",

            "School",

            "College",

            "University",

        ])

    # ====================================================
    # Remove Duplicates
    # ====================================================

    unique_queries = []

    seen = set()

    for item in queries:

        item = item.strip()

        if not item:

            continue

        key = item.lower()

        if key in seen:

            continue

        seen.add(key)

        unique_queries.append(item)

    return unique_queries

# ====================================================
# Format Date & Time
# ====================================================

def format_datetime(date_string: str):

    """
    Convert UTC to IST
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

            ago = f"{diff.days} day{'s' if diff.days > 1 else ''} ago"

        elif diff.seconds >= 3600:

            hours = diff.seconds // 3600

            ago = f"{hours} hour{'s' if hours > 1 else ''} ago"

        elif diff.seconds >= 60:

            minutes = diff.seconds // 60

            ago = f"{minutes} minute{'s' if minutes > 1 else ''} ago"

        else:

            ago = "Just now"

        return {

            "date": published_date,

            "time": published_time,

            "ago": ago

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

    """
    Search GNews API
    """

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
# Calculate Relevance Score
# ====================================================

def calculate_score(article, query: str):

    """
    Calculate relevance score.
    Higher score = Better match.
    """

    score = 0

    title = article.get(
        "title",
        ""
    ).lower()

    description = article.get(
        "description",
        ""
    ).lower()

    content = article.get(
        "content",
        ""
    ).lower()

    query_words = normalize_query(
        query
    ).lower().split()

    for word in query_words:

        if word in title:

            score += 20

        if word in description:

            score += 10

        if word in content:

            score += 5

    return score


# ====================================================
# Search Articles
# ====================================================

def search_articles(
    topic: str,
    page: int = 1
):

    """
    Search all expanded queries.
    """

    queries = expand_query(topic)

    print("=" * 70)
    print("Original Search :", topic)
    print("=" * 70)

    print("Expanded Queries")

    for q in queries:

        print("•", q)

    print("=" * 70)

    all_articles = []

    # ------------------------------------------
    # Search Every Query
    # ------------------------------------------

    for q in queries:

        articles = fetch_articles(
            q,
            page
        )

        if articles:

            all_articles.extend(
                articles
            )

    if not all_articles:

        print("No articles found.")

        return []

    # ------------------------------------------
    # Remove Duplicate Articles
    # ------------------------------------------

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

    # ------------------------------------------
    # Calculate Relevance
    # ------------------------------------------

    for article in articles:

        article["score"] = calculate_score(
            article,
            topic
        )

    # ------------------------------------------
    # Sort
    # ------------------------------------------

    articles.sort(

        key=lambda x: (

            x["score"],

            x.get(
                "publishedAt",
                ""
            )

        ),

        reverse=True

    )

    print("=" * 70)

    print(
        "Unique Articles :",
        len(articles)
    )

    if articles:

        print(
            "Best Score :",
            articles[0]["score"]
        )

        print(
            "Best Match :",
            articles[0].get(
                "title",
                ""
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
    Return the best matching news article.
    """

    articles = search_articles(

        topic,

        page

    )

    if not articles:

        print("=" * 70)

        print("No news found.")

        print("=" * 70)

        return None

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

        "image": (

            article.get(

                "image"

            )

            or

            "https://placehold.co/1200x500?text=No+Image"

        ),

        "source": article.get(

            "source",

            {}

        ).get(

            "name",

            "Unknown"

        ),

        "published_date": published["date"],

        "published_time": published["time"],

        "published_ago": published["ago"],

        "score": article.get(

            "score",

            0

        )

    }

    print("=" * 70)

    print("Best Matching Article")

    print("=" * 70)

    print("Title :", result["title"])

    print("Source :", result["source"])

    print("Score :", result["score"])

    print("Published :", result["published_ago"])

    print("=" * 70)

    return result


# ====================================================
# Test
# ====================================================

if __name__ == "__main__":

    while True:

        print()

        topic = input(

            "Search News : "

        ).strip()

        if topic.lower() == "exit":

            break

        news = search_news(

            topic

        )

        print()

        if news:

            print("-" * 70)

            print("TITLE")

            print(news["title"])

            print()

            print("SOURCE")

            print(news["source"])

            print()

            print("DATE")

            print(news["published_date"])

            print(news["published_time"])

            print(news["published_ago"])

            print()

            print("DESCRIPTION")

            print(news["description"])

            print()

            print("URL")

            print(news["url"])

            print("-" * 70)

        else:

            print("No news found.")



