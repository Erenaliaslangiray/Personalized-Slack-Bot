import os

from . import options, client
from .config import is_env_available


def send_message(message=None):

    if not is_env_available:
        print("Environment was not set up.")
        return

    if message is not None:
        client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=message)
    else:
        if options["MES"] is None:
            print("Message is None. Please provide message text by calling slackbot-message -m 'Your message'")
        else:
            client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=options["MES"])
