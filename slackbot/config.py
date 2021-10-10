import os


def edit_env():
    first_time_setup = is_env_available()
    vars_questions = {
        "SLACK_TOKEN":"Your Slack Token: ",
        "SLACK_USER":"Your Slack User: @",
        "REMINDER_TIME": "Reminder Time (09:00 by default) input as <HH:MM>: ",
        "USED_SHELL": "Please enter your shell that slackbot is configured as 'bin/zsh'(Optional): ",
        "SLACKBOT_PATH": "Please enter executable slackbot location "
                         "(You can use output of 'where slackbot')(Optional): ",
                      }
    vars_answers = {}
    if first_time_setup:
        print("Entered edit mode. Please leave blank if you do not wish to update setting.")
        for key in vars_questions:
            answer = input(vars_questions[key] + "(Current value: "+os.getenv(key)+")")
            if len(answer) == 0:
                answer = None
            if answer is not None and key == "SLACK_USER" and not answer.startswith("@"):
                answer = "@"+answer
            elif key in ["USED_SHELL", "SLACKBOT_PATH"] and answer is None:
                vars_answers[key] = "-"

            vars_answers[key] = answer
    else:
        print("Detected first time setup!")
        for key in vars_questions:
            valid = False
            while valid is False:
                answer = input(vars_questions[key])
                if len(answer) > 0:
                    if key == "SLACK_USER" and not answer.startswith("@"):
                        answer = "@"+answer
                    vars_answers[key] = answer
                    valid = True
                else:
                    if key == "REMINDER_TIME":
                        vars_answers[key] = "09:00"
                        valid = True
                    elif key in ["USED_SHELL","SLACKBOT_PATH"]:
                        vars_answers[key] = "-"
                        valid = True
                    else:
                        print("You can't enter blank entry at first time setup")

    f = open(os.path.dirname(os.path.realpath(__file__)) + "/.env","w")
    for key in vars_answers:
        if vars_answers[key] is None:
            f.write("{0} = '{1}'\r\n".format(key,os.getenv(key)))
        else:
            f.write("{0} = '{1}'\r\n".format(key,vars_answers[key]))


def is_env_available():
    answer = os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/.env')
    return answer
