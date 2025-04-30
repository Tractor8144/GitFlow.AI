from .openai_client import OpenAIClient
import json


class NLPParser:
    def __init__(self, open_ai_client: OpenAIClient):
        self.openai = open_ai_client
        self.system_prompt = """
You are an intelligent command parser for a Git and Repository management CLI tool.

Your task:
- Convert user natural language input into a structured list of actions.
- Each action must be a dictionary with these keys:
  - "action": One of ["add_all", "commit", "get_branch", "create_branch", "checkout_branch", "pull", "push", "add_repo", "switch_repo"]
  - "params": Dictionary of parameters required for that action.
  - "raw_input": The original user text.

Format to strictly follow:
[
  {
    "action": "<action_name>",
    "params": { "<parameter_key>": "<parameter_value>" },
    "raw_input": "<original user input>"
  },
  ...
]

Specific Action Rules:
- "add_all": No parameters.
- "commit": Requires "message" (commit message).
- "get_branch": No parameters.
- "create_branch": Requires "branch_name" (name of new branch).
- "checkout_branch": Requires "branch_name" (name to checkout).
- "pull" / "push": Requires "remote_name" (default to "origin" if missing).
- "add_repo": Requires "repo_name" (nickname) and "repo_path" (full local path).
- "switch_repo": Requires "repo_name" (nickname to switch to).
- "get_active_repo" : No parameters

General Rules:
- Only use actions from the allowed list.
- Always return a **valid JSON list**, even if there is only one action.
- If user asks for multiple operations, return multiple action dictionaries in the list.
- If information is missing (like repo name/path), you can leave the field empty but keep the key.

Important:
- Do NOT explain anything.
- Do NOT apologize.
- Output ONLY the structured JSON list and nothing else.

"""

    def parse(self, user_input: str) -> list:
        raw_response = self.openai.chat(user_message=user_input,
                                        system_prompt=self.system_prompt)
        try:
            actions_list = json.loads(raw_response)
            return actions_list
        except json.JSONDecodeError:
            raise ValueError("Failed to parse GPT response!")
