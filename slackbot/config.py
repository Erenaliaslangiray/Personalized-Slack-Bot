import os


def edit_env():
    first_time_setup = is_env_available()
    vars_questions = {
        "SLACK_TOKEN":"Your Slack Token: ",
        "SLACK_USER":"Your Slack User: @",
        "TIMEZONE":"Your Timezone: ",
        "REMINDER_TIME": "Reminder Time (09:00 by default) input as <HH:MM>: "
                      }
    vars_answers = {}
    if first_time_setup:
        print("Entered edit mode. Please leave blank if you do not wish to update setting.")
        for key in vars_questions:
            answer = input(vars_questions[key])

            if len(answer) == 0:
                answer = None

            if answer is not None and key == "SLACK_USER" and not answer.startswith("@"):
                answer = "@"+answer

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
                    else:
                        print("You can't enter blank entry at first time setup")

    f = open("./.env","w")
    for key in vars_answers:
        if vars_answers[key] is None:
            f.write("{0} = '{1}'\r\n".format(key,os.getenv(key)))
        else:
            f.write("{0} = '{1}'\r\n".format(key,vars_answers[key]))


def is_env_available():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    return os.path.exists('./.env')
