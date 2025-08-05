# generate_inventory.py

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

def get_generate_inventory_prompt():
    system_msg = (
        "You are a DevOps/Iac assistant that writes clean, production-ready Ansible inventory files in YAML format. "
        "Follow the Ansible inventory syntax strictly. Do not include anything other than valid YAML content."
    )

    user_msg = (
        "Generate an Ansible inventory file in YAML format. The inventory should define:\n"
        "- A host named `rhel9-a3`\n"
        "- Belonging to a group called `linux`\n"
        "- With the variable `ansible_user: iacuser`\n"
        "- IMPORTANT: Do **not** wrap your response with triple backticks '```' or quadruple backticks '````'. "
            "Output only raw YAML without any markdown formatting or code fences of any kind.\n"
        "- ALWAYS validate your YAML by calling 'validate_yaml' tool before returning it.\n"
        "- If you’re unsure about YAML structure or syntax, use validate_yaml to confirm it is correct.\n"
        "- Only return YAML that has passed validation."
        "- Input to the tool must be plain YAML as a string."
        "- When calling a tool with YAML input, always format the input using a block scalar (|) for multiline "
        "   values under Action Input. Example:\n"
        " Action: validate_yaml\n"
        " Action Input: |\n"
        "   all:\n"
        "     children:\n"
        "       linux:\n"
        "         hosts:\n"
        "           rhel9-a3:\n"
        "             ansible_user: iacuser"
        "- After the YAML is validated successfully with validate_yaml, use that exact version as the final output and DO NOT regenerate or modify it\n"
        "- Stop the chain once validate_yaml returns 'YAML is valid'"
    )

    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_msg),
        HumanMessagePromptTemplate.from_template(user_msg)
    ])

    return prompt
