class Planner:
    def create_plan(self, task: str):
        return {
            "goal": task,
            "tasks": [
                {
                    "id": 1,
                    "agent": "OpenClaw",
                    "description": task
                }
            ]
        }