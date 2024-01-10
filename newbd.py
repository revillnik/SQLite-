import sqlite3

with sqlite3.connect("new.bd") as base:
    cursor = base.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user (
					 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
					 name TEXT NOT NULL,
					 password INTEGER NOT NULL)"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS games (
                   user_id INTEGER,
                   score INTEGER DEFAULT 0,
                   row_id INTEGER PRIMARY KEY AUTOINCREMENT
	 )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS data (
                   data INTEGER,
                   user_id INTEGER
	 )"""
    )
    cursor.execute(
        "SELECT user.name, sum(games.score), count(games.user_id), data.data FROM games JOIN user JOIN data ON games.user_id = user.user_id AND games.user_id = data.user_id GROUP BY games.user_id"
    )
    f = cursor.fetchall()
    for i in f:
    	print(i)
