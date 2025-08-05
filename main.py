# main.py

from iac_agent.agent import get_agent_executor
from prompts.generate_inventory import get_generate_inventory_prompt
from prompts.generate_playbook import get_generate_playbook_prompt
# import sys
# import os

# # Add root project directory to path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    # Choose which prompt you want to send (as a user message)
    inventory_prompt = get_generate_inventory_prompt()
    playbook_prompt = get_generate_playbook_prompt()

    # Format prompt into messages (ChatMessages)
    playbook_msg = playbook_prompt.format_messages()
    inventory_msg = inventory_prompt.format_messages()
    
    # Convert message content into a plain string to send via agent
    playbook = playbook_msg[-1].content  # Take the final user prompt
    inventory = inventory_msg[-1].content
    print("Playbook prompt 👉👉\n", playbook)
    print("Inventory prompt 👉👉\n", inventory)

    # Send to agent (with memory, tools, etc.) - feedack loop
    agent_executor = get_agent_executor()
    playbook_response = agent_executor.invoke({"input": playbook})
    inventory_response = agent_executor.invoke({"input": inventory})

    print("\nAgent Response for playbook 👋👋\n")
    print(playbook_response["output"])

    print("\nAgent Response for inventory👋👋\n")
    print(inventory_response["output"])

if __name__ == "__main__":
    main()
