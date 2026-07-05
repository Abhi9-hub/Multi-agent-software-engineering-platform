from agents.hermes.orchestrator import HermesOrchestrator
from communication.slack.bot import start_bot

hermes = HermesOrchestrator()
result = hermes.process_task("Build a calculator")
print(result)

def main():
    start_bot()

if __name__ == "__main__":
    main()
    
