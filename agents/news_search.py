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
    Generate multiple search
    queries like Google.
    """

    query = normalize_query(query)

    queries = [

        query

    ]

    lower = query.lower()

    # ----------------------------------------------

    if lower == "tamil nadu":

        queries.extend([

            "Tamil Nadu",

            "Chennai",

            "Tamil Nadu Politics",

            "Tamil Nadu Government",

            "Tamil Nadu Latest",

        ])

    # ----------------------------------------------

    elif lower == "india":

        queries.extend([

            "India Politics",

            "India Economy",

            "India Breaking",

            "New Delhi",

        ])

    # ----------------------------------------------

    elif lower == "chennai":

        queries.extend([

            "Tamil Nadu",

            "Greater Chennai",

        ])

    # ----------------------------------------------

    elif lower == "artificial intelligence":

        queries.extend([

            "Artificial Intelligence",

            "Generative AI",

            "OpenAI",

            "Google AI",

        ])

    # ----------------------------------------------

    elif lower == "cricket":

        queries.extend([

            "India Cricket",

            "ICC",

        ])

    # ----------------------------------------------

    elif lower == "business":

        queries.extend([

            "Business",

            "Stock Market",

            "Economy",

        ])

    # ----------------------------------------------

    elif lower == "sports":

        queries.extend([

            "Sports",

            "Cricket",

            "Football",

            "Olympics",

        ])

    # ----------------------------------------------

    elif lower == "technology":

        queries.extend([

            "Technology",

            "Artificial Intelligence",

            "Google",

            "Microsoft",

        ])

    # ----------------------------------------------

    elif lower == "world":

        queries.extend([

            "World",

            "International",

        ])

    # ----------------------------------------------

    unique_queries = []

    seen = set()

    for item in queries:

        item = item.strip()

        if not item:

            continue

        if item.lower() in seen:

            continue

        unique_queries.append(

            item

        )

        seen.add(

            item.lower()

        )

    return unique_queries

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

