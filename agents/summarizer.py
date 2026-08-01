from autogen_agentchat.agents import AssistantAgent

summarizer = AssistantAgent(
    name="Summarizer",
    model_client=model_client,
    system_message="""
You are an expert news summarizer.

Summarize the news into exactly 5 bullet points.
"""
)
