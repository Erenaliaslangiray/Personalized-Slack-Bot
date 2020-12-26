import os

from optparse import OptionParser

import slack_sdk
from dotenv import load_dotenv

# Loading Environment
load_dotenv()

# Parser Build
parser = OptionParser()
parser.add_option("-m", "--message", dest="MES",
                  help="Message text")
parser.add_option("-r", "--reminder_id",  dest="RID",
                  help="Reminder ID")
parser.add_option("-t", "--timed_message_id",  dest="TID",
                  help="Timed Message ID")
parser.add_option("-d", "--date",  dest="DAT",
                  help="Timed Message ID")
parser.add_option("-c", "--hours",  dest="HRS",
                  help="Timed Message ID")

(options, args) = parser.parse_args()
options = vars(options)

# Slack client initialized.
client = slack_sdk.WebClient(token=os.getenv("SLACK_TOKEN"))
