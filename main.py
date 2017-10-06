from argparse import ArgumentParser
from threading import Timer
import firebase
import webfetcher


IS_DEBUG = False
NO_NOTIFICATIONS = False


def main():
    items = webfetcher.fetch(False)
    if not NO_NOTIFICATIONS:
        firebase.database_push(items, IS_DEBUG)
    print("Done")
    # Schedule next execution
    Timer(60 * 60, main).start()


# Parse arguments
parser = ArgumentParser()
parser.add_argument("--debug", help="Send to debug builds instead of production ones", action="store_true")
parser.add_argument("--no-notification", help="Don't send notifications to devices", action="store_true")

args = parser.parse_args()
if args.debug:
    IS_DEBUG = True
    print("Debug mode")
if args.no_notification:
    NO_NOTIFICATIONS = True

# Execute
main()
