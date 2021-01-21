import os

from . import client
from .config import is_env_available


def send_message(message=None):

    if not is_env_available():
        print("Environment was not set up.")
    else:
        if message is None:
            print("Message is None. Please provide message text by calling slackbot-message -m 'Your message'")
        else:
            client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=message)