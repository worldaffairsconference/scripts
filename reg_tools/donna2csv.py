import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
import csv
import json

# initialize firebase
cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://worldaffairscon-8fdc5-default-rtdb.firebaseio.com"})
# initialize realtime database
db = firebase_admin.db
# initialize firebase authentication
auth = firebase_admin.auth

def getEmails():
    emails = []
    # Start listing users from the beginning, 1000 at a time.
    page = auth.list_users()
    while page:
        for user in page.users:
            print('User: ' + user.uid)
        # Get next batch of users.
        page = page.get_next_page()

    # Iterate through all users. This will still retrieve users in batches,
    # buffering no more than 1000 users in memory at a time.
    for user in auth.list_users().iterate_all():
        email = user.email
        emails.append(email)
    return emails


if __name__ == "__main__":
    #write emails to one column csv
    emails = getEmails()
    with open("emails.csv", "w") as f:
        for email in emails:
            f.write(email + "\n")





