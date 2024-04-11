from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@app.route("/", methods=["GET", "POST"])
def todos():
    con = sql.connect("database.db")
    con.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title TEXT, description TEXT, done BOOLEAN)")

    if request.method == "POST":
        if request.form["submit"] == "Add Todo":
            app.logger.debug(request.form)
            title = request.form["title"]
            description = request.form["description"]
            done = False

            cur = con.cursor()
            cur.execute("INSERT INTO todos (title, description, done) VALUES (?, ?, ?)", (title, description, done))
            con.commit()

    cur = con.cursor()
    cur.execute("select * from todos")

    datas = cur.fetchall()
    con.close() 
    return render_template('todos.html', datas=datas)

@app.route('/done_undone', methods=['POST'])
def done_undone():
    app.logger.debug(request.form)
    todo_id = request.form['todo_id']
    is_checked = request.form.get('todo') is not None
    app.logger.debug(f"todo_id: {todo_id}, is_checked: {is_checked}")

    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE todos SET done = ? WHERE id = ?", (is_checked, todo_id))
    con.commit()
    con.close()
    return redirect(url_for('todos'))

if __name__ == "__main__":
    app.run(debug=True)