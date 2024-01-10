import sqlite3

with sqlite3.connect("st_mark.bd") as base:
    cursor = base.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS students (
					 id INTEGER PRIMARY KEY AUTOINCREMENT,
					 name STR


	)"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS marks (
					 id_student INTEGER,
					 mark INTEGER,
                discipline STR

	)"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS allinformation (
					 id_student INTEGER,
                name STR,
					 mark INTEGER,
                discipline STR
	)"""
    )
