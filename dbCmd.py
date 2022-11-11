import sqlite3


def createAuth():
    con = sqlite3.connect("auth.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE user(id INTEGER PRIMARY KEY,userName TEXT,password TEXT)")
    con.commit()
    con.close()
