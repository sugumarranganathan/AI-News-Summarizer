"""
News Summarizer Agent
"""

from autogen_agentchat.agents import AssistantAgent

from agents.model import model_client

summarizer = AssistantAgent(

    name="Summarizer",

    model_client=model_client,

    system_message="""
You are an expert News Summarizer.

Summarize the news in:

• Exactly 5 bullet points

Keep it short.

Don't add extra information.
"""

)
