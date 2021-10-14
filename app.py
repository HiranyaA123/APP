import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("adminControl.html")


@app.route("/items")
def items():
    return render_template("insertItems.html")


@app.route("/new_items", methods=['GET', 'POST'])
def new_items():
    items_new=request.form['item_name']
    connection=sqlite3.connect(app.DB_FILE)
    cursor=connection.cursor()
    cursor.execute("""INSERT INTO items (name, barcode, description)VALUES(?,?,?)""", (items_new))

    return render_template("insertItems.html")


if __name__ == "__main__":
    app.run(debug=True)






