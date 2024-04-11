from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@app.route("/", methods=["GET", "POST"])
def login():
    con = sql.connect("database.db")
    con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

    if request.method == "POST":
        if request.form["submit"] == "Login":
            app.logger.debug(request.form)
            username = request.form["username"]
            password = request.form["password"]

            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cur.fetchone()
            app.logger.debug(f"user: {user}")
            if user:
                return redirect(url_for('main'))
            else:
                return render_template('login.html', msg="Invalid username or password")
        
        if request.form["submit"] == "Register":
            app.logger.debug(request.form)
            username = request.form["username"]
            password = request.form["password"]

            cur = con.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            con.commit()
            return render_template('login.html', msg="Registered successfully! Please login to continue.")

    return render_template('login.html')

@app.route("/main", methods=["GET", "POST"])
def main():
    con = sql.connect("database.db")
    con.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, quantity INTEGER)")

    if request.method == "POST":
        if request.form["submit"] == "Add":
            app.logger.debug(request.form)
            name = request.form["name"]
            price = request.form["price"]
            quantity = request.form["quantity"]

            cur = con.cursor()
            cur.execute("INSERT INTO items (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
            con.commit()
            return redirect(url_for('main'))
        
        if request.form["submit"] == "Delete": 
            app.logger.debug(request.form)
            id = request.form["id"]

            cur = con.cursor()
            cur.execute("DELETE FROM items WHERE id = ?", (id,))
            con.commit()
            return redirect(url_for('main'))
        
        if request.form["submit"] == "Update":
            app.logger.debug(request.form)
            id = request.form["id"]
            name = request.form["name"]
            price = request.form["price"]
            quantity = request.form["quantity"]

            cur = con.cursor()
            cur.execute("UPDATE items SET name = ?, price = ?, quantity = ? WHERE id = ?", (name, price, quantity, id))
            con.commit()
            return redirect(url_for('main'))

    cur = con.cursor()
    cur.execute("select * from items")

    datas = cur.fetchall()
    con.close() 
    return render_template('main.html', datas=datas)

if __name__ == "__main__":
    app.run(debug=True)
