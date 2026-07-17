from agents.hermes.planner import Planner
from agents.hermes.dispatcher import Dispatcher
from memory.manager import MemoryManger

class HermesOrchestrator:
    def __init__(self):
        self.planner = Planner()
        self.dispatcher = Dispatcher()
        self.memory = MemoryManger()
        print("Hermes initialized")
    
    def process_task(self, task: str):
        print(f"Received Task: {task}")
        self.memory.remember(
            "user",
            task
        )
       
        plan = self.planner.create_plan(task)
        self.dispatcher.dispatch(plan)
        self.memory.remember(
            "assistant",
            "Task completed successfully"
        )
        return plan