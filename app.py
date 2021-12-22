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

@app.route("/users")
def users():
    connection=sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows=cursor.fetchall()
    return render_template("user_list.html", rows=rows)


@app.route("/new_items", methods=['GET', 'POST'])
def new_items():
    if request.method == 'POST':
        name1 = request.form['name']
        barcode1 = request.form['barcode']
        description1 = request.form['description']
        sku1 = request.form['sku']
        exgst1 = request.form['exgst']
        print(name1)

        connection = sqlite3.connect(config.DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO items (name, barcode, description, sku, exgst )VALUES(?,?,?,?,?)""",
                       (name1, barcode1, description1, sku1, exgst1))
        connection.commit()


    else:
        print("")

    return render_template("itemInput.html")

@app.route("/new_user", methods=['GET', 'POST'])
def n():
    if request.method == 'POST':
        # firstname1.users = request.form['firstname']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        yearlevel = request.form['yearlevel']
        team = request.form['team']
        connection = sqlite3.connect(config.DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO users (firstname,lastname,email,yearlevel,team )VALUES(?,?,?,?,?)""",
                       (firstname, lastname, email, yearlevel, team))
        connection.commit()


    else:
        print("")

    return render_template("userInput.html")

@app.route("/test")
def test():
    return render_template("itemInput.html")





if __name__ == "__main__":
    app.run(debug=True)






