import sqlite3


conn = sqlite3.connect("app.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS items(
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           barcode TEXT NOT NULL, 
           description TEXT NOT NULL,
           sku TEXT NOT NULL,
           exgst TEXT NOT NULL
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS loans(
            id INTEGER PRIMARY KEY,
            item_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            date DATE NOT NULL,
            returned TEXT NOT NULL,
            
            FOREIGN KEY(item_id) REFERENCES item(id)
            FOREIGN KEY(user_id) REFERENCES user(id)
    
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS users(
          id INTEGER PRIMARY KEY,
          firstname TEXT NOT NULL,
          lastname TEXT NOT NULL,
          email TEXT NOT NULL,
          yearlevel INTEGER NOT NULL,
          team TEXT
          )""")

c.execute("""CREATE TABLE IF NOT EXISTS inventory(
          id INTEGER PRIMARY KEY,
          item_name TEXT NOT NULL,
          total_qty INTEGER NOT NULL,
          available_qty INTEGER NOT NULL,
          qty_loaned INTEGER NOT NULL,
          qty_broken INTEGER TEXT,
          )""")


conn.commit()
conn.close()
