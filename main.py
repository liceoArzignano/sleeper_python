from argparse import ArgumentParser

from apscheduler.schedulers.blocking import BlockingScheduler

import firebase
import webfetcher

IS_DEBUG = False
NO_NOTIFICATIONS = False
ONE_SHOT = False


def main():
    items = webfetcher.fetch(False)
    firebase.database_push(items, IS_DEBUG, NO_NOTIFICATIONS)
    print("Done")


# Parse arguments
parser = ArgumentParser()
parser.add_argument("--debug", help="Send to debug builds instead of production ones", action="store_true")
parser.add_argument("--no-notification", help="Don't send notifications to devices", action="store_true")
parser.add_argument("--one-shot", help="Execute just once", action="store_true")

args = parser.parse_args()
if args.debug:
    IS_DEBUG = True
    print("Debug mode")
if args.no_notification:
    NO_NOTIFICATIONS = True
if args.one_shot:
    ONE_SHOT = True


# Execute
if ONE_SHOT:
    main()
else:
    # Schedule execution
    sched = BlockingScheduler()

    @sched.scheduled_job('cron', day_of_week='mon-fri', minutes=240)
    def timed_job():
          main()

    sched.start()
