#detect markdwon code, identify the language, extract only the code, ignore explanations

import re

class CodeExtractor:
    def extract(self, response: str):
        pattern = r"```(?:python)?\n(.*?)```"
        match = re.search(pattern, response, re.DOTALL)

        if match:
            return match.group(1).strip()
        return None
    