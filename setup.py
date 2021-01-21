from setuptools import setup,find_packages
import pandas as pd


setup(
    name='slackbot',
    version='0.0.2',
    entry_points={
        'console_scripts': [
            'slackbot = terminal_wrapper.help:help',
            'slackbot-config = slackbot.config:edit_env',

            'slackbot-message = terminal_wrapper.message:message_wrapper',
            'slackbot-task_start_notif = terminal_wrapper.notifications:start_notif_wrapper',
            'slackbot-task_end_notif = terminal_wrapper.notifications:end_notif_wrapper',
            'slackbot-set_timed_message = terminal_wrapper.timed_message:set_timed_message_wrapper',
            'slackbot-list_times_messages = terminal_wrapper.timed_message:list_timed_message_wrapper',
            'slackbot-remove_timed_message = terminal_wrapper.timed_message:remove_timed_message_wrapper',
            'slackbot-set_reminder = terminal_wrapper.reminders:set_reminder_wrapper',
            'slackbot-list_reminders = terminal_wrapper.reminders:set_reminder_wrapper',
            'slackbot-remove_reminder = terminal_wrapper.reminders:set_reminder_wrapper',
        ]
    },
    packages=find_packages(),
    install_requires=[
        'setuptools',
        "slack-sdk",
        "python-dotenv",
        "pandas"
      ],
)

pd.DataFrame(columns=["ID","TYPE","ARGS"]).to_csv("process_records.csv",index=False)
