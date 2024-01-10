import sqlite3

with sqlite3.connect("car.bd") as base:
 cur = base.cursor()
 cur.execute( """CREATE TABLE IF NOT EXISTS car (car_id INTEGER PRIMARY KEY AUTOINCREMENT, model STR, price INTEGER)""")
 car = ("AUDI", 1000), ("BMW", 15000),("VOLVO", 5000), ("VAS", 200)
 cur.executemany("INSERT INTO car VALUES(Null, ?, ?)", car)
 cur.execute("UPDATE car SET price = :Price WHERE model LIKE 'VA%'", {'Price': 150})

try:
    con = sqlite3.connect("car.bd")
    cur = con.cursor()
    cur.execute("BEGIN")
    cur.execute("INSERT INTO car VALUES (NULL, 'SHKODA', 1500)")
    cur.execute("UPDATE car2 SET price = price + 1000")
    con.commit()
except:
    if con:
        con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con:
        con.close()
