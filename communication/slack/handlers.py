from agents.hermes.orchestrator import HermesOrchestrator
from communication.slack.app import app

hermes = HermesOrchestrator()

@app.message("")
def handle_message(message, say):
    user_message = message["text"]
    print(f"Slack Message: {user_message}")

    plan = hermes.process_task(user_message)
    say(f"{plan}")