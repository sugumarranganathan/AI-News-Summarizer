# AI News Summarizer & Tamil Translator

> **Multi-Agent AI News Summarizer & Tamil Translator using AutoGen, Groq, FastAPI, GNews API, HTML, CSS, and JavaScript.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?logo=fastapi)
![AutoGen](https://img.shields.io/badge/AutoGen-0.7.5-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-red)
![GNews](https://img.shields.io/badge/GNews-API-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

AI News Summarizer & Tamil Translator is a **Multi-Agent AI web application** that searches the latest news using the **GNews API**, summarizes the article using **Groq Llama 3.3** through **AutoGen**, and translates the AI-generated summary into **Tamil**.

The application provides a clean, responsive dashboard built with **FastAPI**, **HTML**, **CSS**, and **JavaScript**.

---

# Features

- 🔍 Search any latest news topic
- 📰 Fetch latest news from GNews API
- 🤖 AI-powered news summarization
- 🌍 Tamil translation using AI
- 📸 News image preview
- 🔗 Read Full Article link
- 📅 Published date
- 📰 News source information
- 🌙 Dark / Light Mode
- 📋 Copy Summary
- 📱 Fully Responsive UI
- ⚡ FastAPI Backend
- 🤖 Multi-Agent Architecture

---

# 🏗️ Project Architecture

```
                User

                  │

                  ▼

          Search News Topic

                  │

                  ▼

        FastAPI Backend

                  │

                  ▼

        Multi-Agent Workflow

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

   GNews Search        Groq LLM

        │

        ▼

 Latest News Article

        │

        ▼

 Summarizer Agent

        │

        ▼

 Translator Agent

        │

        ▼

 JSON Response

        │

        ▼

 Beautiful Web UI
```

---

# 🤖 Multi-Agent Workflow

```
User

 │

 ▼

📰 News Search Agent

 │

 ▼

🤖 Summarizer Agent

 │

 ▼

🌍 Tamil Translator Agent

 │

 ▼

📱 Web Dashboard
```

---

# 👨‍💻 Agents

## 📰 News Search Agent

**Responsibility**

- Search latest news
- Retrieve article
- Extract metadata

**Input**

```
Tesla
```

**Output**

```
Latest News Article
```

---

## 🤖 Summarizer Agent

**Responsibility**

- Read article
- Understand article
- Generate concise summary
- Produce exactly 5 bullet points

---

## 🌍 Translator Agent

**Responsibility**

- Translate English summary
- Preserve meaning
- Generate easy-to-read Tamil

---

# 💻 Technology Stack

| Category | Technology |
|----------|------------|
| Frontend | HTML5 |
| Styling | CSS3 |
| Scripting | JavaScript |
| Backend | FastAPI |
| AI Framework | AutoGen |
| LLM | Groq Llama 3.3 |
| News Provider | GNews API |
| Template Engine | Jinja2 |
| HTTP | Requests |
| Environment | Python Dotenv |

---

# 📁 Folder Structure

```
AI-News-Summarizer/

│
├── agents/
│   ├── model.py
│   ├── news_search.py
│   ├── summarizer.py
│   ├── translator.py
│   └── workflow.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .env
├── README.md


# 📷 User Interface

### Home Page

- Search latest news
- AI-powered dashboard
- Modern glassmorphism UI

---

### Results

- News Image
- Latest News
- AI Summary
- Tamil Translation
- Source
- Published Date
- Read Full Article

---

# 📌 Example Search Topics

```
Artificial Intelligence

Tesla

OpenAI

Microsoft

Google

SpaceX

Cricket

IPL

India

Tamil Nadu
```

---

# 🔄 Workflow

```
User Search

      │

      ▼

GNews API

      │

      ▼

Latest Article

      │

      ▼

Summarizer Agent

      │

      ▼

Translator Agent

      │

      ▼

Frontend
```

---

# 📊 API Endpoint

## Home

```
GET /
```

---

## Summarize News

```
POST /summarize
```

Example Request

```json
{
    "topic":"Tesla"
}
```

Example Response

```json
{
    "news":"...",

    "summary":"...",

    "translation":"...",

    "image":"...",

    "url":"...",

    "source":"Reuters",

    "published":"2026-08-01"
}


----

# 👨‍💻 Author

**R. Sugumar. M.B.A.,**

| AI Developer | Multi-Agent AI Enthusiast

