from optparse import OptionParser

# Parser Build
parser = OptionParser()
parser.add_option("-m", "--message", dest="MES",
                  help="Message text")
parser.add_option("-r", "--reminder_id",  dest="RID",
                  help="Reminder ID")
parser.add_option("-t", "--timed_message_id",  dest="TID",
                  help="Timed Message ID")
parser.add_option("-d", "--date",  dest="DAT",
                  help="Timed Message Date")
parser.add_option("-c", "--hours",  dest="HRS",
                  help="Timed Message Hours")

(options, args) = parser.parse_args()
options = vars(options)
