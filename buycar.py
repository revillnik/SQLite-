import sqlite3

with sqlite3.connect("buycar.bd") as base:
    cur = base.cursor()
    cur.executescript(
        """CREATE TABLE IF NOT EXISTS idcar (car_id INTEGER, model STR, price INTEGER); CREATE TABLE IF NOT EXISTS buyer (name STR, id_in INTEGER, id_buy INTEGER)"""
    )
    car = (1, "AUDI", 1000), (2, "BMW", 15000), (3, "VOLVO", 5000), (4, "VAS", 200)
    # cur.executemany("INSERT INTO idcar VALUES (?, ?, ?)", car)
    # cur.execute("INSERT INTO buyer VALUES ('Федор', NULL, NULL)")
    cur.execute("SELECT max(rowid) FROM idcar")
    f = cur.fetchone()
    k = int(f[0])
    id_buy = 2
    cur.execute("UPDATE buyer SET 'id_in' = :id_in, 'id_buy' = :id_buy", {"id_in": k, "id_buy": id_buy})
    #cur.execute("DELETE FROM idcar WHERE car_id = :id_buy", {'id_buy': id_buy})
