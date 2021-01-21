# Personalized Slack Bot (Under Construction)

#### _Version 0.0.2_

-----------
## Installization:
1. Clone The Repository
2. ```pip install <path_to_cloned_dir>/Personalized-Slack-Bot```
3. ```slackbot-config``` For configuring your slackbot token, your user and application settings.

### **The package can be used with 2 different methods. An importable python3 library and as a terminal command.**

## Python Usage:
```import slackbot```

* **edit_env()** ---> Allows you to configure Slack credentials and application settings. (Automaticly called on the first time run.)
* **send_message(message=None)** ---> Allows you to send specified message via bot.
* **start_notif(message = None)** ---> Allows you to send a notification about a task being started.
* **end_notif(message = None)** ---> Allows you to send a notification about a task being finished.
* **set_timed_message()**_(Under Construction)_ ---> Allows you to set a timed message.
* **list_times_messages()**_(Under Construction)_ ---> Allows you to list timed messages.
* **remove_timed_message(tid=None)**_(Under Construction)_ ---> Allows you to remove a timed message.
* **set_reminder()**_(Under Construction)_ ---> Allows you to set a reminder message.
* **list_reminders()**_(Under Construction)_ ---> Allows you to list your reminder messages.
* **remove_reminder(rid=None)**_(Under Construction)_ ---> Allows you to remove a reminder message.

## Terminal Usage:

* **slackbot-config** ---> Allows you to configure Slack credentials and application settings.
* **slackbot-message** ---> Allows you to send specified message via bot.
  
  Ex: ```slackbot-message -m 'Hello World, this is an example message!'```
* **slackbot-task_start_notif** ---> Allows you to send a notification about a task being started.
  
  Ex: ```slackbot-task_start_notif```
* **slackbot-task_end_notif** ---> Allows you to send a notification about a task being finished.
  
  Ex: ```slackbot-task_end_notif -m 'Main_Task'```
* **slackbot-set_timed_message**_(Under Construction)_ ---> Allows you to set a timed message.
  
  Ex: ```slackbot-set_timed_message -d '12/12/2020' -c '18:30' -m 'Did you miss me?'```
* **slackbot-list_times_messages**_(Under Construction)_ ---> Allows you to list timed messages.
  
    Ex: ```slackbot-list_timed_messages```
* **slackbot-remove_timed_message**_(Under Construction)_ ---> Allows you to remove a timed message.
  
    Ex: ```slackbot-remove_timed_message -t 13```
* **slackbot-set_reminder**_(Under Construction)_ ---> Allows you to set a reminder message.
  
    Ex: ```slackbot-set_reminder -m 'Don't forget to remember what you always forget.```
* **slackbot-list_reminders**_(Under Construction)_ ---> Allows you to list your reminder messages.
  
    Ex: ```slackbot-list_reminders```
* **slackbot-remove_reminder**_(Under Construction)_ ---> Allows you to remove a reminder message.
    Ex: ```slackbot-remove_reminder -r 7```
  