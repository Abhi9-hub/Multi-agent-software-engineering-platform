import os

from slack_bolt.adapter.socket_mode import SocketModeHandler

from communication.slack.app import app

import communication.slack.handlers


def start_bot():
    handler = SocketModeHandler(
        app,
        app_token=os.getenv("SLACK_APP_TOKEN")
    )

    handler.start()