from agents.hermes.planner import Planner
from agents.hermes.dispatcher import Dispatcher

class HermesOrchestrator:
    def __init__(self):
        self.planner = Planner()
        self.dispatcher = Dispatcher()
        print("Hermes initialized")
    
    def process_task(self, task: str):
        print(f"Received Task: {task}")
        plan = self.planner.create_plan(task)
        self.dispatcher.dispatch(plan)
        return plan