import sqlite3

conn = sqlite3.connect("app.db")
c = conn.cursor()

c.execute("INSERT INTO items (name, barcode, description,sku,exgst)VALUES('brain',123423,great,12-34,$5")
c.execute("INSERT INTO items (name, barcode, description,sku,exgst)VALUES ('brain',326823,good ,52-54,$7")
c.execute("INSERT INTO items (name, barcode, description,sku,exgst) VALUES('brain',345435,bad,16-31,$6")




conn.commit()
conn.close()
