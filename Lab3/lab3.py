from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "My Secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
  return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error=None

	if request.method == 'POST':
		if request.form['name'] != 'admin' or request.form['pass'] != 'root':
			error = 'Invalid Credentials'
		else:
			flash("Successful Login")
			return redirect(url_for('admin'))	
	
	return render_template('login.html' , error = error)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	if request.method == 'POST':
		return redirect(url_for('admin'))	
	
	return render_template('register.html')

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if 'data' not in session:
        session['data'] = []

    if request.method == 'POST':
        if request.form['songname'] == '' and request.form['moviename'] == '' and request.form['releaseyear'] == '':
            error = 'Invalid Input'
        else:
            session['data'].append([request.form['songname'], request.form['moviename'], request.form['releaseyear']])

    return render_template('admin.html', datas=session['data'])


if __name__ == '__main__':
	app.run()