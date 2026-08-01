// ======================================================
// AI News Summarizer
// Version 3.1
// script.js
// Part 1
// ======================================================

// ======================================================
// Elements
// ======================================================

const topic = document.getElementById("topic");

const searchBtn = document.getElementById("searchBtn");

const refreshBtn = document.getElementById("refreshBtn");

const clearBtn = document.getElementById("clearBtn");

const themeBtn = document.getElementById("themeBtn");

const loading = document.getElementById("loading");

const news = document.getElementById("news");

const summary = document.getElementById("summary");

const translation = document.getElementById("translation");

const image = document.getElementById("newsImage");

const source = document.getElementById("source");

const published = document.getElementById("published");

const articleLink = document.getElementById("articleLink");

// ======================================================
// Agent Status
// ======================================================

const agentStatus = document.getElementById("agentStatus");

const newsAgent = document.getElementById("newsAgent");

const summaryAgent = document.getElementById("summaryAgent");

const translatorAgent = document.getElementById("translatorAgent");

// ======================================================
// Current Search State
// ======================================================

let currentTopic = "";

let currentPage = 1;

// ======================================================
// Event Listeners
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

themeBtn.addEventListener("click", toggleTheme);

// ======================================================
// Search News
// ======================================================

async function searchNews() {

    if (currentTopic === "") {

        alert("Please enter a news topic.");

        return;

    }

    // ===========================================
    // Show Loading
    // ===========================================

    loading.classList.remove("hidden");

    agentStatus.classList.remove("hidden");

    newsAgent.innerHTML =
        "🔎 News Agent : Searching latest news...";

    summaryAgent.innerHTML =
        "⏳ Summarizer Agent : Waiting...";

    translatorAgent.innerHTML =
        "⏳ Translator Agent : Waiting...";

    news.innerHTML =
        `🔎 Searching News #${currentPage}...`;

    summary.innerHTML =
        "🤖 AI is generating summary...";

    translation.innerHTML =
        "🌍 Translating into Tamil...";

    image.src =
        "https://placehold.co/1200x500?text=Loading...";

    source.innerHTML =
        "📰 Searching...";

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

        // ===========================================
        // Agent Status
        // ===========================================

        newsAgent.innerHTML =
            "✅ News Agent : Completed";

        summaryAgent.innerHTML =
            "🤖 Summarizer Agent : Generating Summary...";

        summary.innerHTML =
            data.summary || "";

        summaryAgent.innerHTML =
            "✅ Summarizer Agent : Completed";

        translatorAgent.innerHTML =
            "🌍 Translator Agent : Translating...";

        translation.innerHTML =
            data.translation || "";

        translatorAgent.innerHTML =
            "✅ Translator Agent : Completed";

        // ===========================================
        // News
        // ===========================================

        news.innerHTML =
            data.news || "No news found.";

        // ===========================================
        // Image
        // ===========================================

        image.src = data.image
            ? data.image
            : "https://placehold.co/1200x500?text=No+Image";

        // ===========================================
        // Source
        // ===========================================

        source.innerHTML =
            `📰 ${data.source || "Unknown Source"}`;

        // ===========================================
        // Published
        // ===========================================

        published.innerHTML =

            `📅 ${data.published_date || ""}<br>
             🕒 ${data.published_time || ""}<br>
             🟢 Published ${data.published_ago || ""}`;

        // ===========================================
        // Article Link
        // ===========================================

        articleLink.href = data.url || "#";

    }

    catch (error) {

        console.error(error);

        news.innerHTML =
            "❌ Unable to fetch latest news.";

        summary.innerHTML =
            "Please try again.";

        translation.innerHTML =
            "மீண்டும் முயற்சிக்கவும்.";

        image.src =
            "https://placehold.co/1200x500?text=Error";

        source.innerHTML =
            "📰 Error";

        published.innerHTML = "";

        articleLink.href = "#";

        newsAgent.innerHTML =
            "❌ News Agent : Failed";

        summaryAgent.innerHTML =
            "❌ Summarizer Agent : Failed";

        translatorAgent.innerHTML =
            "❌ Translator Agent : Failed";

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

        alert("Please search a topic first.");

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

    loading.classList.add("hidden");

    agentStatus.classList.add("hidden");

    newsAgent.innerHTML =
        "⏳ News Agent : Waiting...";

    summaryAgent.innerHTML =
        "⏳ Summarizer Agent : Waiting...";

    translatorAgent.innerHTML =
        "⏳ Translator Agent : Waiting...";

    news.innerHTML =
        "Latest news will appear here...";

    summary.innerHTML =
        "AI summary will appear here...";

    translation.innerHTML =
        "தமிழ் மொழிபெயர்ப்பு இங்கே தோன்றும்...";

    image.src =
        "https://placehold.co/1200x500?text=AI+News";

    source.innerHTML =
        "📰 Source";

    published.innerHTML =
        "📅 Published Date";

    articleLink.href = "#";

}

// ======================================================
// Copy Text
// ======================================================

function copyText(id) {

    const text =
        document.getElementById(id).innerText;

    navigator.clipboard.writeText(text)
        .then(() => {

            alert("✅ Copied Successfully!");

        })
        .catch(() => {

            alert("Unable to copy text.");

        });

}

// ======================================================
// Theme Toggle
// ======================================================

function toggleTheme() {

    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {

        themeBtn.innerHTML = "☀️";

    }

    else {

        themeBtn.innerHTML = "🌙";

    }

}

// ======================================================
// Initial State
// ======================================================

window.onload = function () {

    loading.classList.add("hidden");

    agentStatus.classList.add("hidden");

    currentTopic = "";

    currentPage = 1;

};

