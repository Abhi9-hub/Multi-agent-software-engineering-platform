from agents.openclaw.client import OpenClawClient
from utils.file_manager import FileManager
from utils.code_extractor import CodeExtractor



class Dispatcher:

    def __init__(self):
        self.openclaw = OpenClawClient()
        self.file_manager = FileManager()
        self.code_extractor = CodeExtractor()

    def dispatch(self, plan):

        for task in plan["tasks"]:

            response = self.openclaw.execute(
                task["description"]
            )
            code = self.code_extractor.extract(response)
            if code:
                self.file_manager.save(
                    "generated.py",
                    code
                )

            else:
                self.file_manager.save(
                "output.md",
                response
            )

            print("\n========== OpenClaw Response ==========\n")
            print(response)
            print("\n=======================================\n")

        return True