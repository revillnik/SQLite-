import sqlite3
def openfile(n):
	try:
		with open(f"{n}.png", 'rb') as file:
			return file.read()
	except:
		raise MemoryError

def writefile(name, f):
	try:
		with open(f"{name}.png", "wb") as file:
			file.write(f)
	except:
		raise TypeError

with sqlite3.connect('png.bd') as base:
	base.row_factory = sqlite3.Row
	cur = base.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS png (name STR, ava BLOB)""")
	img = openfile(1)
	binare = sqlite3.Binary(img)
	cur.execute("INSERT INTO png VALUES ('Никита', ?)", (binare,))
	cur.execute("SELECT * FROM png WHERE name LIKE 'Никита'")
	f = cur.fetchone()['ava']
	writefile('ava1', f)
	
