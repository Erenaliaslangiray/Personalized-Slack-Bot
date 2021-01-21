import os

import slack_sdk
from dotenv import load_dotenv

from .config import edit_env,is_env_available
from .help import help


if not is_env_available():
    print("WARNING: Environment is not set.")
    edit_env()
    print("Environment set successfully!")

load_dotenv(dotenv_path=os.path.dirname(os.path.realpath(__file__))+"/.env")

# Slack client initialized.
client = slack_sdk.WebClient(token=os.getenv("SLACK_TOKEN"))

from .message import send_message
from .notifications import start_notif,end_notif
from .reminders import *
from .timed_message import *