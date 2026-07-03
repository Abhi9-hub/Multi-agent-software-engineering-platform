from agents.hermes.planner import Planner

class HermesOrchestrator:
    def __init__(self):
        self.planner = Planner()
        print("Hermes initialized")
    
    def process_task(self, task: str):
        print(f"Received Task: {task}")
        plan = self.planner.create_plan(task)

        return plan