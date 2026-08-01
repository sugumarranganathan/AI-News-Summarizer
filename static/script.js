// ======================================================
// AI News Summarizer
// script.js
// ======================================================

// ======================================================
// Elements
// ======================================================

const topic = document.getElementById("topic");
const searchBtn = document.getElementById("searchBtn");

const loading = document.getElementById("loading");

const news = document.getElementById("news");
const summary = document.getElementById("summary");
const translation = document.getElementById("translation");

const image = document.getElementById("newsImage");
const source = document.getElementById("source");
const published = document.getElementById("published");
const articleLink = document.getElementById("articleLink");

// ======================================================
// Search Button
// ======================================================

searchBtn.addEventListener("click", searchNews);

// ======================================================
// Press Enter
// ======================================================

topic.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {

        searchNews();

    }

});

// ======================================================
// Search News
// ======================================================

async function searchNews() {

    const query = topic.value.trim();

    if (query === "") {

        alert("Please enter a news topic.");

        return;

    }

    loading.classList.remove("hidden");

    // Loading Messages

    news.innerHTML = "🔎 Searching latest news...";

    summary.innerHTML = "🤖 AI is generating summary...";

    translation.innerHTML = "🌍 Translating into Tamil...";

    image.src = "https://placehold.co/1200x500?text=Loading...";

    source.innerHTML = "📰 Searching...";

    published.innerHTML = "";

    articleLink.href = "#";

    try {

        const response = await fetch("/summarize", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                topic: query

            })

        });

        const data = await response.json();

        // ===========================================
        // News
        // ===========================================

        news.innerHTML = data.news || "No news found.";

        summary.innerHTML = data.summary || "";

        translation.innerHTML = data.translation || "";

        // ===========================================
        // News Image
        // ===========================================

        if (data.image) {

            image.src = data.image;

        }

        else {

            image.src = "https://placehold.co/1200x500?text=No+Image";

        }

        // ===========================================
        // Source
        // ===========================================

        source.innerHTML = `📰 ${data.source || "Unknown Source"}`;

        // ===========================================
        // Published Date & Time
        // ===========================================

        published.innerHTML = `
            📅 ${data.published_date || ""}<br>
            🕒 ${data.published_time || ""}<br>
            🟢 Published ${data.published_ago || ""}
        `;

        // ===========================================
        // Article Link
        // ===========================================

        if (data.url) {

            articleLink.href = data.url;

        }

        else {

            articleLink.href = "#";

        }

    }

    catch (error) {

        console.error(error);

        news.innerHTML = "❌ Unable to fetch latest news.";

        summary.innerHTML = "Please try again.";

        translation.innerHTML = "மீண்டும் முயற்சிக்கவும்.";

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
