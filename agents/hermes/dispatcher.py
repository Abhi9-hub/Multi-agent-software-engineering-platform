class Dispatcher:
    def dispatch(self, plan):
        for task in plan["tasks"]:
            print(
                f"[Dispatcher] Sending task to {task['agent']} : {task['description']}"
            )
            return True