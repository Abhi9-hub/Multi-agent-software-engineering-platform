
import os

from dotenv import load_dotenv
from slack_bolt import App

loaded=load_dotenv()
print("Dotenv Loaded:", loaded)
print("BOT TOKEN:", os.getenv("SLACK_BOT_TOKEN"))
print("APP TOKEN:", os.getenv("SLACK_APP_TOKEN"))


app = App(
    token=os.getenv("SLACK_BOT_TOKEN")
)