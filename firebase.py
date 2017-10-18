from news import News
import os
import pyrebase
import requests

API_KEY = os.environ['SNAKE_API_KEY']


def exists(child):
    return child.get().val() is not None


def database_push(items: [], is_debug: bool, no_notification=False):
    if API_KEY is None or API_KEY is "":
        print("Define a valid SNAKE_API_KEY environment variable")
        return

    config = {
        "apiKey": API_KEY,
        "authDomain": "liceobold.firebaseapp.com",
        "databaseURL": "https://liceobold.firebaseio.com/",
        "storageBucket": "liceobold.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    for item in reversed(items):
        data = {
            "id": item.number,
            "title": item.title,
            "message": item.message,
            "url": item.url,
            "isPrivate": item.is_private
        }

        child = db.child("news").child(str(item.number) + "-" + item.date).shallow()

        if not exists(child):
            print("Creating /news/{}...".format(str(item.number) + "-" + item.date))
            db.child("news").child(str(item.number) + "-" + item.date).set(data)
            if not no_notification:
                fcm(item, is_debug)


def fcm(item: News, is_debug: bool):
    if API_KEY is None or API_KEY is "":
        print("Define a valid SNAKE_API_KEY environment variable")
        return

    headers = {
        "content-type": "application/json",
        "Authorization": "key=" + API_KEY
    }

    data = {
        is_debug and "d_title" or "title": "\"{}\"".format(item.title),
        is_debug and "d_message" or "message": "\"{}\"".format(item.message),
        "url": "\"{}\"".format(item.url),
        "isPrivate": item.is_private and "\"true\"" or "\"false\""
    }

    message = {
        "to": "/topics/global",
        "priority": "high",
        "notification": data,
        "data": data,
    }

    print("Pushing an item to " + (is_debug and "debug" or "production") + " builds ({})".format(item.number))

    r = requests.post("https://fcm.googleapis.com/fcm/send", json=message, headers=headers)
    code = r.status_code
    if code < 100 or code > 300:
        print("Error {}".format(code))
        print(r.reason)
        print(r.text)
        print(r.content)
