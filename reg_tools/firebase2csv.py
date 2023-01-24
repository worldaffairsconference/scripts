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
