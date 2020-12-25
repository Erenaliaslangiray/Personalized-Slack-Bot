import os

from src import options, client


def send_message(message=None):
    if message is not None:
        client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=message)
    else:
        if options["MES"] is None:
            print("Message is None. Please provide message text by calling slackbot-message -m 'Your message'")
        else:
            client.chat_postMessage(channel=os.getenv("SLACK_USER"), text=options["MES"])
