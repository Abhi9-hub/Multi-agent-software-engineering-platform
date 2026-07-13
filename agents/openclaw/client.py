import ollama
import os
from agents.openclaw.prompt_builder import PromptBuilder

class OpenClawClient:
    def __init__(self):
        self.model = os.getenv("OLLAMA_MODEL")
        self.prompt_builder = PromptBuilder()


    def execute(self, task):
        prompt = self.prompt_builder.build(task)
        #print(f"[OpenClaw] Executing: {prompt}")
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response["message"]["content"]