import sqlite3


conn = sqlite3.connect("app.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS items(
            id INTEGER PRIMARY KEY,
            name TEXT,
            barcode TEXT,
            description TEXT
            )""")


conn.commit()
conn.close()
