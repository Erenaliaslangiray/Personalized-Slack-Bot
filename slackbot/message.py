import os

from . import client
from .config import is_env_available

from .timed_message import remove_timed_message


def send_message(message=None,from_timed=None):
    if not is_env_available():
        print("Environment was not set up.")
    else:
        if message is None:
            print("ERROR : Message is None. Please provide message text.")
        else:
            client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=message)

    client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=from_timed)
    if from_timed is not None:
        client.chat_postMessage(channel=os.getenv("SLACK_USER"), text="inside")
        result = remove_timed_message(pid=from_timed)
        client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=result)
