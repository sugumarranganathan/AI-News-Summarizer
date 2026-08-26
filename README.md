# 🤖 AI News Summarizer & Tamil Translator

https://ai-news-summarizer-cqzh.onrender.com/

> **A Multi-Agent AI application that searches the latest news, generates AI-powered summaries, and translates them into natural Tamil using AutoGen, Groq, FastAPI, and GNews API.**

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![AutoGen](https://img.shields.io/badge/AutoGen-Multi--Agent-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-red)
![GNews](https://img.shields.io/badge/GNews-API-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Problem Statement

In today's digital era, millions of news articles are published every day across different news platforms. Users often struggle to stay informed because reading complete news articles requires significant time and effort. Most traditional news applications simply display articles without helping users quickly understand the key information.

Several challenges exist with conventional news platforms:

- 📰 News articles are often long and time-consuming to read.
- ⏳ Busy professionals and students have limited time to read complete articles.
- 🌍 Many users prefer consuming news in their native language rather than English.
- 📚 Information overload makes it difficult to identify the most important updates.
- 🔍 Users need to visit multiple websites to search for relevant news.
- 🤖 Traditional news applications do not provide AI-powered summaries or intelligent content processing.
- ⚙️ Existing systems lack an automated workflow for searching, summarizing, and translating news.

Therefore, there is a need for an intelligent AI-based solution that can automatically search the latest news, generate concise summaries, translate them into regional languages, and present all essential information through a single user-friendly interface.

---

# 💡 Proposed Solution

The **AI News Summarizer & Tamil Translator** addresses these challenges by implementing a **Multi-Agent AI Architecture**. Instead of relying on a single AI model for all tasks, the application divides the workflow into specialized AI agents, each responsible for a specific task.

The workflow operates as follows:

1. **📰 News Search Agent**
   - Searches the latest news using the GNews API.
   - Retrieves the most relevant article along with its title, description, content, image, source, publication date, and article URL.

2. **🤖 Summarizer Agent**
   - Reads the complete news article.
   - Generates a concise AI-powered summary highlighting the most important information.

3. **🌍 Tamil Translator Agent**
   - Translates the AI-generated summary into natural and professional Tamil.
   - Preserves the meaning and readability of the original summary.

4. **⚙️ Workflow Manager**
   - Coordinates communication between all AI agents.
   - Combines their outputs into a structured response.
   - Sends the final result to the FastAPI backend.

5. **FastAPI Backend**
   - Processes the request.
   - Returns the complete response to the web application.

6. **💻 Modern Web Interface**
   - Displays:
     - 📰 Latest News
     - 🖼️ News Image
     - 📅 Published Date & Time
     - 🏢 News Source
     - 🤖 AI Summary
     - 🌍 Tamil Translation
     - 🔗 Original Article Link

---

#  Solution Benefits

- ✅ Automatically searches the latest news.
- ✅ Saves users significant reading time through AI-generated summaries.
- ✅ Provides natural Tamil translations for regional users.
- ✅ Uses a modular Multi-Agent architecture for better scalability and maintainability.
- ✅ Presents all important news information in a single interface.
- ✅ Reduces information overload by highlighting only the key points.
- ✅ Demonstrates a practical real-world implementation of Agentic AI using AutoGen.

---

# 🔄 Multi-Agent Solution Workflow

```text
                👤 User
                    │
        Search News Topic
                    │
                    ▼
      📰 News Search Agent
      (Retrieve Latest News)
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
      ⚙️ Workflow Manager
 (Combine Agent Responses)
                    │
                    ▼
         🚀 FastAPI Backend
                    │
                    ▼
         💻 Web Application
```

---

## 🌟 Outcome

The **AI News Summarizer & Tamil Translator** transforms traditional news reading into an intelligent AI-assisted experience by combining **news retrieval, AI summarization, and multilingual translation** within a **Multi-Agent architecture**. This enables users to understand important news quickly, efficiently, and in their preferred language while demonstrating the practical application of **Agentic AI** in a real-world scenario.

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



