# tools/yaml_validator.py

from langchain.tools import tool
import yaml, re

@tool
def validate_yaml(content: str) -> str:
    """Validate a YAML string and return a success or error message."""
    print("\n🔥🔥 validate_yaml was called! 🔥🔥")
    try:
        yaml.safe_load(strip_code_fences(content))
        return "YAML is valid."
    except yaml.YAMLError as e:
        return f"YAML validation error: {str(e)}"

def strip_code_fences(text: str) -> str:
    print("🔥🔥 strip_code_fences was called! 🔥🔥")
    # Strip leading/trailing whitespace and all 3- or 4-backtick code blocks
    cleaned = re.sub(r"^`{3,4}\s*\n", "", text.strip())  # opening fence
    cleaned = re.sub(r"\n`{3,4}$", "", cleaned)          # closing fence
    return cleaned