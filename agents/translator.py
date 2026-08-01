from autogen_agentchat.agents import AssistantAgent

translator = AssistantAgent(
    name="Translator",
    model_client=model_client,
    system_message="""
Translate the summary into Tamil.

Do not change the meaning.
"""
)
