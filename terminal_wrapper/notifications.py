from . import options
from slackbot import message


def start_notif_wrapper():
    if options["MES"] is None:
        message.send_message("Process is started! 🏎 💨")
    else:
        message.send_message("Process with name: {} is started! 🏎 💨".format(options["MES"]))


def end_notif_wrapper():
    if options["MES"] is None:
        message.send_message("Process is finished! 🏁 ✅")
    else:
        message.send_message("Process with name: {} is finished! 🏁 ✅".format(options["MES"]))
