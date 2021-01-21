from . import options
from slackbot import message


def message_wrapper():
    message.send_message(options["MES"])
