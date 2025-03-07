import os
import sqlite3

os.remove("new.db") if os.path.exists("new.db") else None

conn = sqlite3.connect("new.db")

c = conn.cursor()

c.execute("CREATE TABLE bois (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name STRING, age REAL)")

students = [("Joe", 103),
            ("James", 15),
            ("Owen", 103),
            ("Amy", 1)]

c.executemany("INSERT INTO bois VALUES (NULL, ?, ?)", students)

for thing in c.execute("SELECT * FROM bois WHERE age = ?", (103,)):
    print(thing)

print()

c.execute("SELECT * FROM bois")
thing = c.fetchall()
print(thing)

conn.commit()
conn.close()
