from .openai_client import OpenAIClient
import json


class NLPParser:
    def __init__(self, open_ai_client: OpenAIClient):
        self.openai = open_ai_client
        self.system_prompt = """
You are an intelligent command parser for a Git automation CLI tool.

Your job is to:
- Convert user natural language input into a structured list of actions.
- Each action must be a dictionary with the following keys:
    - "action": (one of these strings only) ["add_all", "commit", "get_branch", "create_branch", "checkout_branch", "pull", "push"]
    - "params": dictionary of parameters required for that action.
    - "raw_input": the original user text.

Strictly follow this format:
[
    {
        "action": "<action_name>",
        "params": {
            "<parameter_key>": "<parameter_value>"
        },
        "raw_input": "<original user input>"
    },
    ...
]

Rules:
- Only use the allowed actions listed.
- If no parameters are needed for an action, use an empty "params" dictionary.
- Always return a valid JSON list. No explanations, no extra text.
- Assume default remote is "origin" if user says "push" or "pull" without specifying remote.
- If user asks for multiple operations, generate multiple action dictionaries in order.
"""

    def parse(self, user_input: str) -> list:
        raw_response = self.openai.chat(user_message=user_input,
                                        system_prompt=self.system_prompt)
        try:
            actions_list = json.loads(raw_response)
            return actions_list
        except json.JSONDecodeError:
            raise ValueError("Failed to parse GPT response!")
