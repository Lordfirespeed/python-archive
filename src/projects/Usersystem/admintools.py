import sqlite3
import os
import resources as res


def getusers():
    db.execute("SELECT * FROM Users")
    return db.fetchall()


def printusers():
    userlist = getusers()
    [print(", ".join([str(c) for c in user])) for user in userlist]


def delusers(IDs):
    # Delete users with IDs
    intIDs = [IDn[0] if type(IDn) == tuple else IDn for IDn in IDs]
    tupIDs = [(IDn,) if type(IDn) == int else IDn for IDn in IDs]

    for ID in intIDs:
        userFilePath = res.userDirectory + res.getuserfile("ID", ID)
        try:
            os.remove(userFilePath)
        except FileNotFoundError:
            pass

    db.executemany("DELETE FROM Users WHERE ID=?", tupIDs)
    conn.commit()
    # Retrieve user IDs in use
    InUseIDs = [user[0] for user in getusers()]
    InUseIDs.append(0)
    InUseIDs = [(IDn,) if type(IDn) == int else IDn for IDn in InUseIDs]
    # Update the database metadata with the maximum in use ID in the table, to prevent large gaps between IDs
    db.execute("UPDATE sqlite_sequence SET seq = ? WHERE name='Users'", max(InUseIDs))
    conn.commit()


conn = sqlite3.connect("database.db")
db = conn.cursor()

db.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = db.fetchall()
tables = [table for tabletuple in tables for table in tabletuple]


if "Users" not in tables:
    db.execute('''CREATE TABLE Users
              (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
               firstname text,    
               lastname text, 
               username text UNIQUE, 
               password text, 
               creationtimestr text)''')
    tables.append("Users")
