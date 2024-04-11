# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, render_template, request, flash
# from flask_session import Session

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
app.secret_key = "My Secret key"
# Session(app)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def hello_world():
	return 'Hello World <br /><br /> <a href="/about">About Page</a>'

def about():
	return 'About World'
app.add_url_rule("/about", "about", about)

@app.route('/blog/<int:postID>')
def blog(postID):
	return 'Blog num. %d'%postID

@app.route('/admin')
def admin():
	return 'Hello Admin'

@app.route('/guest/<name>')
def guest(name):
	return 'Hello Guest %s'%name

@app.route('/user/<user>')
def hello_user(user):
	if(user == 'admin'):
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('guest', name = user))
	
@app.route('/demo')
def demo():
	return render_template('demo.html', name="Aarav", langs=['C', 'Python', 'Java', 'JS'])

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error=None

	if request.method == 'POST':
		if request.form['name'] != 'admin' or request.form['pass'] != 'root':
			error = 'Invalid Credentials'
		else:
			flash("Successful Login")
			return redirect(url_for('demo'))	
	
	return render_template('login.html' , error = error)



# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()
	#flask --app appName --debug run