'''
Script used to automatically register UCC students.
---
Created Date: Sunday November 20th 2022
Author: Jefferson Ding
-----
Last Modified: Sunday November 20th 2022 11:08:20 pm
Modified By: Jefferson Ding at <jefferson.ding@ucc.on.ca>
-----
Copyright (c) 2023 Jefferson Ding
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

import uuid
import csv
import json

from firebase import Firebase
with open("api.json", "r") as f:
    config = json.load(f)
    firebase = Firebase(config)

# initialize firebase
cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://worldaffairscon-8fdc5-default-rtdb.firebaseio.com"})
# initialize realtime database
db = firebase_admin.db
# initialize firebase authentication
auth = firebase_admin.auth

# registration constants
access_code = "THOZYirJHLYj9UXKnypCs9vbeTw1"


# get students from csv
def get_students(csv_path):
    students = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students


# register student to firebase auth
def firebase_auth_register(email):
    temp_password = str(uuid.uuid4().hex)
    try:
        user = auth.create_user(
            email=email,
            email_verified=False,
            password=temp_password,
            disabled=False
        )
        print(f"Successfully created new user: {user.uid} with email: {email} and temporary password: {temp_password}")
    except Exception as e:
        print(f"Error creating new user: {e}")
        return None
    return user.uid

def add_user(email,name,grade,access_code,ucc_advisor,id):
    uid = firebase_auth_register(email)
    if uid is not None:
        # set student reference
        ref = "teachers/" + access_code + "/students/" + uid
        db.reference(ref).set({
            "email": email,
            "name": name,
            "grade": grade,
            "p1": "",
            "p2": "",
            "p3": "",
            "ucc_advisor": ucc_advisor,
            "note": "",
            "uccid": id
        })

        # set teacher link
        ref = "students/" + uid
        db.reference(ref).set({
            "teacherID": access_code
        })
        reset_password(email)
    else:
        print("Failed to register user due to firebase auth error")

def reset_password(email):
    firebase.auth().send_password_reset_email(email)
    print("Password reset email sent to " + email)

if __name__=="__main__":
    students = get_students("./students2.csv")
    for student in students:
        email = student["email"]
        name = student["pre_first_name"] + " " + student["last_name"]
        grade = student["grade"].replace("Year ", "")
        ucc_advisor = student["advisor"]
        studentnum = student["id"]
        add_user(email,name,grade,access_code,ucc_advisor,studentnum)

    