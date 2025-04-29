from dotenv import load_dotenv
import os
import openai


class OpenAIClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model_name = os.getenv('OPENAI_MODEL')
        openai.api_key = self.api_key
        # openai.project = 'Default'

    def chat(self, user_message: str, system_prompt: str) -> str:
        response = openai.chat.completions.create(
            model=self.model_name,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_message}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content
