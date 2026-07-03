class Planner:
    def create_plan(self, task: str):
        return {
            "goal": task,
            "task": [
                {
                    "id": 1,
                    "agent": "OpenClaw",
                    "description": task
                }
            ]
        }