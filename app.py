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

@app.route("/item/delete")
def delete():
    connection = sqlite3.connect(config.DB_FILE)
    cursor = connection.cursor()
    id1 =request.args.get('id')
    print(id)
    cursor.execute("""DELETE FROM items WHERE id=(?)""",(id1))


    connection.commit()
    cursor.close()

    return render_template("item_list.html")




@app.route("/users")
def users():
    connection=sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows=cursor.fetchall()
    return render_template("user_list.html", rows=rows)

@app.route("/new_user", methods=['GET', 'POST'])
def new_user():
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

@app.route("/borrow", methods=['GET', 'POST'])
def borrow():
    if request.method == 'POST':

        item_barcode = request.form['item_barcode']
        student_id = request.form['student_id']
        date = request.form['date']
        connection = sqlite3.connect(config.DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO loans (item_id,user_id,date, returned )VALUES(?,?,?,'n')""",
                       (item_barcode, student_id, date))
        connection.commit()



    else:
        print("")

    return render_template("borrow.html")

@app.route("/returns", methods=['GET', 'POST'])
def returns():
    if request.method == 'POST':
        print("check")
        item_barcode = request.form['item_barcode']
        connection = sqlite3.connect(config.DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''UPDATE loans SET returned = ? WHERE item_id = ?''', ('y', item_barcode))
        connection.commit()

    else:
        print("")

    return render_template("return.html")

@app.route("/loans")
def loans():
    connection=sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM loans")
    rows=cursor.fetchall()
    return render_template("loan_list.html", rows=rows)








if __name__ == "__main__":
    app.run(debug=True)






