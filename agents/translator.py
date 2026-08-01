"""
Tamil Translator Agent
"""

from autogen_agentchat.agents import AssistantAgent

from agents.model import model_client

translator = AssistantAgent(

    name="Translator",

    model_client=model_client,

    system_message="""
Translate the summary into Tamil.

Rules:

• Keep bullet points

• Keep meaning unchanged

• Easy Tamil

"""

)
