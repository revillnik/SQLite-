import sqlite3

with sqlite3.connect("UNION.bd") as base:
    cursor = base.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS score (
					 name_table STR DEFAULT score,
					 score INTEGER
	)"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user (
					 name_table STR DEFAULT user,
					 score INTEGER
	)"""
    )
    cursor.execute(
        "SELECT score, name_table FROM user UNION SELECT score, name_table FROM score ORDER BY score ASC"
    )
    f = cursor.fetchall()
    print(f)
