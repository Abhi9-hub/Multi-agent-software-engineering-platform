from agents.openclaw.client import OpenClawClient

from utils.file_manager import FileManager
from utils.code_extractor import CodeExtractor
from utils.code_runner import CodeRunner


class Dispatcher:

    def __init__(self):
        self.openclaw = OpenClawClient()
        self.file_manager = FileManager()
        self.code_extractor = CodeExtractor()
        self.code_runner = CodeRunner()

    def dispatch(self, plan):

        for task in plan["tasks"]:

            print(
                f"\n[Dispatcher] Sending task to {task['agent']} : {task['description']}\n"
            )

            # Ask OpenClaw (Qwen via Ollama)
            response = self.openclaw.execute(
                task["description"]
            )

            # Show raw LLM response
            print("\n========== OpenClaw Response ==========\n")
            print(response)
            print("\n=======================================\n")

            # Extract Python code
            code = self.code_extractor.extract(response)

            if code:

                # Save extracted code
                file_path = self.file_manager.save(
                    "generated.py",
                    code
                )

                # Execute generated code
                result = self.code_runner.run(file_path)

                print("\n========== Execution Result ==========\n")

                if result["success"]:
                    print(result["stdout"])
                else:
                    print(result["stderr"])

                print("\n======================================\n")

            else:

                print("[Dispatcher] No Python code found.")

                self.file_manager.save(
                    "output.md",
                    response
                )

        return True