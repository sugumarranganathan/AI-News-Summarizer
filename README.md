# 🤖 AI News Summarizer & Tamil Translator

> **A Multi-Agent AI application that searches the latest news, generates AI-powered summaries, and translates them into natural Tamil using AutoGen, Groq, FastAPI, and GNews API.**

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![AutoGen](https://img.shields.io/badge/AutoGen-Multi--Agent-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-red)
![GNews](https://img.shields.io/badge/GNews-API-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

AI News Summarizer & Tamil Translator is an intelligent **Multi-Agent AI application** that helps users understand the latest news in seconds.

Instead of reading lengthy news articles, users simply enter a topic such as:

- AI
- Tesla
- OpenAI
- Cricket
- India
- Stock Market
- Technology

The application automatically:

- 🔎 Searches the latest news
- 🤖 Generates an AI-powered summary
- 🌍 Translates the summary into natural Tamil
- 📰 Displays the original article, news image, source, publication date & time
- 🔗 Provides a direct link to the original article

---

# ✨ Key Features

- 🔎 Search latest news by keyword
- 🤖 AI-powered news summarization
- 🌍 Natural Tamil translation
- 📰 Latest news image
- 🔗 Direct article link
- 📅 Published date & time
- ⏰ "Published X hours ago"
- 🤖 Multi-Agent Workflow visualization
- 🌙 Dark / Light Mode
- 📋 Copy Summary
- 📱 Responsive Design
- ⚡ FastAPI Backend
- ☁️ Render Deployment Ready

---

# 🤖 Multi-Agent Architecture

```
                     👤 User
                        │
                        ▼
               📰 News Search Agent
          (Search latest news from GNews)
                        │
                        ▼
              🤖 Summarizer Agent
          (Generate AI Summary)
                        │
                        ▼
           🌍 Tamil Translator Agent
        (Translate Summary into Tamil)
                        │
                        ▼
              ⚙ Workflow Manager
                        │
                        ▼
                  🚀 FastAPI API
                        │
                        ▼
                 💻 Web Interface
```

---

# 🤖 AI Agents

| Agent | Responsibility | Input | Output |
|--------|---------------|-------|--------|
| 📰 **News Search Agent** | Searches the latest news using GNews API and retrieves article details | User Search Topic | Latest News Article |
| 🤖 **Summarizer Agent** | Reads the complete article and generates AI-powered key highlights | News Article | AI Summary |
| 🌍 **Tamil Translator Agent** | Converts the AI summary into natural and professional Tamil | AI Summary | Tamil Translation |

---

# 🔄 Agent Communication

| Step | From | To | Communication |
|------|------|----|---------------|
| 1 | 👤 User | 📰 News Search Agent | Sends search topic |
| 2 | 📰 News Search Agent | 🤖 Summarizer Agent | Sends latest news article |
| 3 | 🤖 Summarizer Agent | 🌍 Tamil Translator Agent | Sends AI summary |
| 4 | 🌍 Tamil Translator Agent | ⚙ Workflow Manager | Sends Tamil translation |
| 5 | ⚙ Workflow Manager | 🚀 FastAPI | Combines all responses |
| 6 | 🚀 FastAPI | 💻 Frontend | Displays final result |

---

# 📊 AI News Summarizer vs Ordinary News App

| Feature | 📰 Ordinary News App | 🤖 AI News Summarizer |
|---------|----------------------|------------------------|
| **📰 News Reading** | Users read the complete article manually. | AI extracts and presents the most important information in seconds. |
| **🤖 AI Summary** | Usually unavailable. | Automatically generates a concise summary with key highlights. |
| **🌍 Language Support** | Mostly available only in the original language. | Instantly translates news into natural Tamil. |
| **⚙ Multi-Agent Processing** | No AI workflow behind the scenes. | Dedicated News Search, Summarizer, and Translator Agents collaborate to deliver the final result. |
| **⏱ Time Saving** | Reading one article may take 5–10 minutes. | Understand the complete story in less than a minute. |
| **🎨 User Experience** | Primarily displays articles from publishers. | Displays news image, source, publish date & time, AI summary, Tamil translation, and article link together. |
| **💡 Smart Information Delivery** | Focuses on displaying news. | Helps users quickly understand news using AI, making it ideal for students, professionals, and busy readers. |

---

# 🖥️ Technology Stack

| Category | Technology |
|----------|------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | FastAPI |
| AI Framework | AutoGen |
| LLM | Groq (Llama 3.3 70B) |
| News API | GNews API |
| Templates | Jinja2 |
| Deployment | Render |
| Environment Variables | Python Dotenv |

---

# 📂 Project Structure

```text
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
├── render.yaml
├── .env.example
├── README.md
└── LICENSE
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-News-Summarizer.git

cd AI-News-Summarizer
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file.

```env
GNEWS_API_KEY=YOUR_GNEWS_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## 5️⃣ Run the Application

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

# 🌐 Deploy on Render

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

### Environment Variables

```
GNEWS_API_KEY
GROQ_API_KEY
```

---

# 🖥️ Application Workflow

```
User
   │
   ▼
Enter News Topic
   │
   ▼
News Search Agent
(Search latest article)
   │
   ▼
Summarizer Agent
(Generate AI Summary)
   │
   ▼
Tamil Translator Agent
(Translate Summary)
   │
   ▼
Workflow Manager
   │
   ▼
FastAPI Backend
   │
   ▼
Modern Web Interface
```

---

# 📸 Application Output

The application displays:

- 📰 Latest News
- 🖼️ News Image
- 📅 Published Date
- 🕒 Published Time
- ⏰ Published "X Hours Ago"
- 🤖 AI Summary
- 🌍 Tamil Translation
- 🔗 Read Full Article
- ⚡ Multi-Agent Workflow Status

---


---

# 👨‍💻 Developed by

**R. Sugumar, M.B.A.,**

**MBA | AI & Multi-Agent Application Developer**

### Skills

- Multi-Agent AI Systems
- AutoGen
- FastAPI
- Groq LLM
- Python
- Prompt Engineering
- AI Application Development

---



