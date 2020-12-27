from setuptools import setup
import pandas as pd


setup(
    name='slackbot',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'slackbot-config = src.config:edit_env',
            'slackbot-message = src.message:send_message',
            'slackbot-task_start_notif = src.notifications:start_notif',
            'slackbot-task_end_notif = src.notifications:end_notif',
            'slackbot-set_timed_message = src.timed_message:set_timed_message',
            'slackbot-list_times_messages = src.timed_message:list_timed_message',
            'slackbot-remove_timed_message = src.timed_message:remove_timed_message',
            'slackbot-set_reminder = src.reminders:set_reminder',
            'slackbot-list_reminders = src.reminders:set_reminder',
            'slackbot-remove_reminder = src.reminders:set_reminder',
        ]
    },
    packages=['src']
)

pd.DataFrame(columns=["ID","TYPE","ARGS"]).to_csv("process_records.csv",index=False)
