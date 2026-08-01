// ======================================================
// AI News Summarizer
// Version 3.1
// script.js
// ======================================================

// ======================================================
// Elements
// ======================================================

const topic = document.getElementById("topic");

const searchBtn = document.getElementById("searchBtn");

const refreshBtn = document.getElementById("refreshBtn");

refreshBtn.addEventListener("click", nextNews);

const clearBtn = document.getElementById("clearBtn");

const loading = document.getElementById("loading");

const news = document.getElementById("news");

const summary = document.getElementById("summary");

const translation = document.getElementById("translation");

const image = document.getElementById("newsImage");

const source = document.getElementById("source");

const published = document.getElementById("published");

const articleLink = document.getElementById("articleLink");

// ======================================================
// Current Search State
// ======================================================

let currentTopic = "";

let currentPage = 1;

// ======================================================
// Events
// ======================================================

searchBtn.addEventListener("click", () => {

    currentTopic = topic.value.trim();

    currentPage = 1;

    searchNews();

});

refreshBtn.addEventListener("click", nextNews);

clearBtn.addEventListener("click", clearPage);

topic.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {

        currentTopic = topic.value.trim();

        currentPage = 1;

        searchNews();

    }

});

// ======================================================
// Search News
// ======================================================

async function searchNews() {

    if (currentTopic === "") {

        alert("Please enter a news topic.");

        return;

    }

    loading.classList.remove("hidden");

    news.innerHTML = `🔎 Searching News #${currentPage}...`;

    summary.innerHTML = "🤖 Generating AI Summary...";

    translation.innerHTML = "🌍 Translating into Tamil...";

    image.src = "https://placehold.co/1200x500?text=Loading...";

    source.innerHTML = "📰 Searching...";

    published.innerHTML = "";

    articleLink.href = "#";

    try {

        const response = await fetch("/summarize", {

            method: "POST",

            cache: "no-store",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                topic: currentTopic,

                page: currentPage

            })

        });

        const data = await response.json();

        if (data.error) {

            throw new Error(data.error);

        }

        // ======================================
        // News
        // ======================================

        news.innerHTML = data.news || "No news found.";

        // ======================================
        // Summary
        // ======================================

        summary.innerHTML = data.summary || "";

        // ======================================
        // Translation
        // ======================================

        translation.innerHTML = data.translation || "";

        // ======================================
        // Image
        // ======================================

        if (data.image) {

            image.src = data.image;

        }

        else {

            image.src = "https://placehold.co/1200x500?text=No+Image";

        }

        // ======================================
        // Source
        // ======================================

        source.innerHTML = `📰 ${data.source}`;

        // ======================================
        // Published
        // ======================================

        published.innerHTML =

        `📅 ${data.published_date}<br>
         🕒 ${data.published_time}<br>
         🟢 Published ${data.published_ago}`;

        // ======================================
        // Link
        // ======================================

        articleLink.href = data.url || "#";

    }

    catch (error) {

        console.error(error);

        news.innerHTML = "❌ Unable to fetch news.";

        summary.innerHTML = "";

        translation.innerHTML = "";

        image.src = "https://placehold.co/1200x500?text=Error";

        source.innerHTML = "📰 Error";

        published.innerHTML = "";

        articleLink.href = "#";

    }

    finally {

        loading.classList.add("hidden");

    }

}

// ======================================================
// Next News
// ======================================================

function nextNews() {

    if (currentTopic === "") {

        alert("Search a topic first.");

        return;

    }

    currentPage++;

    searchNews();

}

// ======================================================
// Clear
// ======================================================

function clearPage() {

    currentTopic = "";

    currentPage = 1;

    topic.value = "";

    news.innerHTML = "Latest news will appear here...";

    summary.innerHTML = "AI summary will appear here...";

    translation.innerHTML = "தமிழ் மொழிபெயர்ப்பு இங்கே தோன்றும்...";

    image.src = "https://placehold.co/1200x500?text=AI+News";

    source.innerHTML = "📰 Source";

    published.innerHTML = "📅 Published Date";

    articleLink.href = "#";

}

// ======================================================
// Copy Text
// ======================================================

function copyText(id) {

    const text = document.getElementById(id).innerText;

    navigator.clipboard.writeText(text);

    alert("Copied Successfully!");

}

// ======================================================
// Dark Mode
// ======================================================

const themeBtn = document.getElementById("themeBtn");

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {

        themeBtn.innerHTML = "☀️";

    }

    else {

        themeBtn.innerHTML = "🌙";

    }

});
