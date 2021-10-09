import os

from . import client
from .config import is_env_available


def send_message(message=None,from_cron=None):

    if not is_env_available():
        print("Environment was not set up.")
    else:
        if message is None:
            print("ERROR : Message is None. Please provide message text.")
        else:
            client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=message)