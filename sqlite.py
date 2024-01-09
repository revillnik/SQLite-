import sqlite3
with sqlite3.connect("first.bd") as base:
	cursor = base.cursor()
	cursor.execute("DROP TABLE IF EXISTS first")
	cursor.execute("""CREATE TABLE IF NOT EXISTS first (
					 id INTEGER PRIMARY KEY,
					 name TEXT NOT NULL DEFAULT ВАСЯ,
					 score INTEGER DEFAULT 0 
	)""")