import sqlite3
with sqlite3.connect("new.bd") as base:
	cursor = base.cursor()
	cursor.execute('DROP TABLE IF EXISTS user')
	cursor.execute("""CREATE TABLE IF NOT EXISTS user (
					 user_id INTEGER PRIMARY KEY,
					 name TEXT NOT NULL,
					 password INTEGER NOT NULL,
					 score INTEGER DEFAULT 0

	)""")