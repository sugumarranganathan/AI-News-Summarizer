"""
Groq Model Configuration
AutoGen 0.7.5
"""

from google.colab import userdata

from autogen_ext.models.openai import OpenAIChatCompletionClient

# ============================================
# Groq API Key
# ============================================

GROQ_API_KEY = userdata.get("GROQ_API_KEY")

# ============================================
# Model Client
# ============================================

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
