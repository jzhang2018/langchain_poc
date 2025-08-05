# iac_agent/agent.py

from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.yaml_validator import validate_yaml
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

def get_agent_executor():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    tools = [
      Tool(
          name="validate_yaml",
          func=validate_yaml,
          description=(
            "Use this tool to validate YAML strings. "
            "You MUST use this before returning any YAML output (e.g., Ansible playbooks or inventory files). "
            "Input should be a raw YAML string. The tool will confirm if the syntax is valid or raise detailed errors. "
            "Only return YAML that has been validated."
          )
      )
    ]

    agent_executor = initialize_agent(
        tools=tools,
        tool_choice="validate_yaml",  # <-- this forces tool call
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True
    )

    return agent_executor
