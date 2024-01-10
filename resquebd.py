import sqlite3

with sqlite3.connect("car.sqlite3") as con:
	cur = con.cursor()
	with open('sql.sql', 'w') as f:
		for i in con.iterdump():
			f.write(i)

		
        
