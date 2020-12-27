"""
import getpass

from . import options, client

import pandas as pd
from crontab import CronTab


def set_timed_message():
    cron = CronTab(user=getpass.getuser())
    job = cron.new(command="/usr/local/bin/slackbot-message -m 'cron deneme'",comment="this is cron try code")
    job.minute.every(1)
    print("yay")
    cron.write()
    return


def list_timed_message():
    cron = CronTab(user=getpass.getuser())
    # list all cron jobs (including disabled ones)
    for job in cron:
        print(job)

    return


def remove_timed_message():
    cron = CronTab(user=getpass.getuser())

    cron.remove_all()
    print("removed")
    return
"""