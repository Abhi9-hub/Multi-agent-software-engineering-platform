import ollama
import os

class OpenClawClient:
    def execute(self, prompt: str):
        print(f"[OpenClaw] Executing: {prompt}")
        response = ollama.chat(
            model=os.getenv("OLLAMA_MODEL"),
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response["message"]["content"]