import sqlite3

conn = sqlite3.Connection("database.db")

with open("createDb.sql","r") as f:
    sql = f.read()
    print(sql)

conn.executescript(sql)
conn.commit()

conn.close()