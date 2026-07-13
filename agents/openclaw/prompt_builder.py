class PromptBuilder:
    def build(self, task: str):
        return f"""
You are an expert software engineer.

Task:
{task}

Rules:
1. Return ONLY PYTHON CODE.
2. Do NOT explain anything.
3. Do NOT use Markdown.
4. Do NOT wrap the code inside ``` blocks.
5. The code must be executable.
6. Do not require user input().
7. Include a small demonstration inside:

if __name__ == "__main__":

so the program can run automatically.

Return only the source code.
"""