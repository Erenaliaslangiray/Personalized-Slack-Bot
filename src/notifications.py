from src import options
from .message import send_message


def start_notif():
    if options["MES"] is None:
        send_message("Process is started! 🏎 💨")
    else:
        send_message("Process with name: {} is started! 🏎 💨".format(options["MES"]))


def end_notif():
    if options["MES"] is None:
        send_message("Process is finished! 🏁 ✅")
    else:
        send_message("Process with name: {} is finished! 🏁 ✅".format(options["MES"]))
