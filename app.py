from flask import Flask, render_template, methods, request, session, redirect;

app = Flask(__name__)

@app.route('')
def index():
	return render_template('public/index.html')

@app.route('/register', methods=['FORM_REGISTER'])
def register():
	session['name01'] = 	 request.form['name01']
	session['name02'] = 	 request.form['name02']
	session['surname01'] = request.form['surname01']
	session['surname02'] = request.form['surname02']
	session['email'] =		 request.form['email']
	session['password'] =	 request.form['password']
	return render_template('public/register.html')

@app.route('/login', methods=['FORM_LOGIN'])
def login():
	return render_template('public/login.html')