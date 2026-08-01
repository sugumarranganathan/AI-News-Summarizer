"""
====================================================
Groq Model Configuration
AutoGen 0.7.5

Author : Sugumar R
====================================================
"""

import os

from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

# ====================================================
# Load Environment Variables
# ====================================================

load_dotenv()

# ====================================================
# Groq API Key
# ====================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. "
        "Please set it in your environment variables or .env file."
    )

# ====================================================
# Groq Model Client
# ====================================================

model_client = OpenAIChatCompletionClient(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    include_name_in_message=False,
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "family": "unknown"
    }
)
