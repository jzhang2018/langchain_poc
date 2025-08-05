# generate_playbook.py

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

def get_generate_playbook_prompt():
    system_msg = (
        "You are a DevOps/IaC assistant that writes clean, production-ready Ansible YAML files "
        "for Linux infrastructure automation. Your output will be parsed and validated, so strictly return valid YAML."
    )
    user_msg = (
        "Write an idiomatic Ansible playbook to resolve a disk full issue on a Red Hat Enterprise Linux 9 system. "
        "The playbook must:\n"
        "- Be safe and avoid deleting any user or system-critical data\n"
        "- Use Ansible best practices\n"
        "- Clean up logs, journal, cache, and orphaned temp files\n"
        "- Include inline comments where helpful"
        "- IMPORTANT: ⚠️ “Do **not** wrap your response with triple backticks '```' or quadruple backticks '````'. Output only raw YAML without any markdown formatting or code fences of any kind.\n"
        "- ALWAYS validate your YAML before returning it using the validate_yaml tool.\n"
        "- If you’re unsure about YAML structure or syntax, use validate_yaml to confirm it is correct.\n"
        "- Only return YAML that has passed validation."
        "- Input to the tool must be plain YAML as a string."
        "- When calling a tool with YAML input, always format the input using a block scalar (|) for multiline "
        "   values under Action Input. Example:\n"
        " Action: validate_yaml\n"
        " Action Input: |\n"
        "   - name: Resolve disk full issue on RHEL 9\n"
        "     hosts: all\n"
        "     tasks:\n"
        "       - name: Clean up logs\n"
        "         command: rm -rf /var/log/*\n"
        "- After the YAML is validated successfully with validate_yaml, use that exact version as the final output and DO NOT regenerate or modify it\n"
        "- Stop the chain once validate_yaml returns 'YAML is valid'"
    )

    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_msg),
        HumanMessagePromptTemplate.from_template(user_msg)
    ])

    return prompt
