import sqlite3

conn = sqlite3.connect("app.db")
c = conn.cursor()

c.execute("INSERT INTO items (name, barcode, description)VALUES('brain','1345678','hi')")
c.execute("INSERT INTO items (name, barcode, description)VALUES('battery','19876','hello')")
c.execute("INSERT INTO items (name, barcode, description)VALUES('sensor','1343338','check')")




conn.commit()
conn.close()
