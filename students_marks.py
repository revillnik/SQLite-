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
    cursor.execute("INSERT INTO allinformation SELECT marks.id_student, students.name, marks.mark, marks.discipline FROM marks JOIN students ON students.id = marks.id_student")
    cursor.execute("SELECT students.name, marks.mark, marks.discipline FROM marks JOIN students ON id_student = id WHERE marks.mark > (SELECT mark FROM marks WHERE id_student = 1 and discipline LIKE 'Си') AND discipline LIKE 'Си'")
    f = cursor.fetchall()
    print(f)
