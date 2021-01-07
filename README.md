# Personalized Slack Bot (Not Finished)

-----------
## Installization:
1. Clone The Repository
2. ```pip install -r <path_to_cloned_dir>/Personalized-Slack-Bot/requirements.txt```
3. ```pip install <path_to_cloned_dir>/Personalized-Slack-Bot```
4. ```slackbot-config``` For configuring your slackbot token, your user and application settings.

## Usage:
Here is the list of operations available:

* **slackbot-config**: For configuring your Slack credentials and application settings.

* **slackbot-message**: Lets you send a message to configured user by specifying the message with ```-m 'message'```

    Ex: ```slackbot-message -m 'Hello World, this is an example message!'```

* **slackbot-task_start_notif**: Sending user a notification about a process is being started. (You can optionally put a process name or specialized message by passing -m 'message' argument.)

    Ex: ```slackbot-task_start_notif```
  
* **slackbot-task_end_notif**: Sending user a notification about a process is being finished. (You can optionally put a process name or specialized message by passing -m 'message' argument.)

    Ex: ```slackbot-task_end_notif -m 'Main_Task'```

* **slackbot-set_timed_message**: Lets user to set a timed message.

    Ex: ```slackbot-set_timed_message -d '12/12/2020' -c '18:30' -m 'Did you miss me?'```

* **slackbot-list_times_messages**: Lets user to list all timed messages and their *Timed Message Ids*.

    Ex: ```slackbot-list_times_messages```

* **slackbot-remove_timed_message**: Let user to remove messages in queue by providing *Timed Message Id* with ```-t <TMID>```.

    Ex: ```slackbot-remove_timed_message -t 13```

* **slackbot-set_reminder**: Sets reminders that will be sent to user at every day 09:00 by default.

    Ex: ```slackbot-set_reminder -m 'Don't forget to remember what you always forget.```

* **slackbot-list_reminders**: Lets user to list all reminders and their *Reminder Ids*.

    Ex: ```slackbot-list_reminders```

* **slackbot-remove_reminder**: Let user to remove a reminder from the list by providing *Reminder ID* with ```-r <RID>```.

    Ex: ```slackbot-remove_reminder -r 7```
