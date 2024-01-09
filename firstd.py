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
    cursor.execute("UPDATE first SET score = 1000 WHERE name LIKE 'Н%'")
    cursor.execute("SELECT * FROM first")
    result = cursor.fetchall()
    print(result)
    

