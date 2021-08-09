import sqlite3
from __main__ import *

conn = sqlite3.connect("database.db")
db = conn.cursor()

pwdAttemptsAllowed = 3

import resources as res


def login():
    try:
        db.execute("SELECT * FROM Users")
        userList = db.fetchall()
        usernameList = [user[3] for user in userList]
        enteredUsername = res.validentry(usernameList, "username")
        print("Logging in as '%s'..." % enteredUsername)
        userIndex = usernameList.index(enteredUsername)
        correctPassword = userList[userIndex][4]
        for i in range(1, pwdAttemptsAllowed+1):
            userInput = input("Attempt #%d: Enter Password.\n> " % i)
            if userInput != correctPassword:
                print("Password incorrect. %d Attempts remaining." % (pwdAttemptsAllowed - i))
            else:
                print("Welcome, %s %s." % (userList[userIndex][1], userList[userIndex][2]))
                break
        return userList[userIndex][0]

    except KeyboardInterrupt:
        print("Cancelling login...")
        return None
