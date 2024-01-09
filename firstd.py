import sqlite3

with sqlite3.connect("first.bd") as base:
    cursor = base.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS first (
					 id INTEGER PRIMARY KEY,
					 name TEXT NOT NULL DEFAULT Вася,
					 score INTEGER DEFAULT 0 
	)"""
    )
    cursor.execute("SELECT * FROM first WHERE score > 500 ORDER BY score ASC")
    result1 = cursor.fetchall()
    for i in result1:
        print(i)
