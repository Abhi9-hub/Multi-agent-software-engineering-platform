
import os

from dotenv import load_dotenv
from slack_bolt import App

loaded=load_dotenv()
print("Dotenv Loaded:", loaded)


app = App(
    token=os.getenv("SLACK_BOT_TOKEN")
)