import sqlite3
import config
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("adminControl.html")


@app.route("/items")
def items():
    connection=sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM items")
    rows=cursor.fetchall()
    return render_template("item_list.html", rows=rows)


@app.route("/new_item", methods=['GET', 'POST'])
def new_items():
    if request.form == 'POST':
        name = request.form['name']
        barcode = request.form['barcode']
        description = request.form['description']
        sku = request.form['sku']
        exgst = request.form['exgst']
        print(name)

        connection = sqlite3.connect(app.DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO items (name, barcode, description, sku, exgst )VALUES(?,?,?,?,?)""",
                       (name, barcode, description, sku, exgst))
    else:
        print("It didnt work")

    return render_template("insertItems.html")



@app.route("/items/<item>")
def items(item):
    connection=sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM items")
    rows=cursor.fetchall()
    return render_template("item_list.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)






