from setuptools import setup,find_packages

__version__ = "0.1.0"

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='slackbot',
    version=__version__,
    entry_points={
        'console_scripts': [
            'slackbot = terminal_wrapper.wrapper:help',
            'slackbot-config = slackbot.config:edit_env',

            'slackbot-message = terminal_wrapper.wrapper:message_wrapper',

            'slackbot-task_start_notif = terminal_wrapper.wrapper:start_notif_wrapper',
            'slackbot-task_end_notif = terminal_wrapper.wrapper:end_notif_wrapper',

            'slackbot-set_timed_message = terminal_wrapper.wrapper:set_timed_message_wrapper',
            'slackbot-list_timed_message = terminal_wrapper.wrapper:list_timed_message_wrapper',
            'slackbot-remove_timed_message = terminal_wrapper.wrapper:remove_timed_message_wrapper',

            'slackbot-set_reminder = terminal_wrapper.wrapper:set_reminder_wrapper',
            'slackbot-list_reminder = terminal_wrapper.wrapper:set_reminder_wrapper',
            'slackbot-remove_reminder = terminal_wrapper.wrapper:set_reminder_wrapper',
        ]
    },
    packages=find_packages(),
    install_requires=required,
)