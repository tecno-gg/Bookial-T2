from flask import Flask, render_template, methods, request, session, redirect;

app = Flask(__name__)

@app.route('')
def index():
	return render_template('public/index.html')

@app.route('/register', methods=['POST'])
def register():
	request.form['first_name']
	request.form['first_surname']
	request.form['email']
	request.form['password']
	return render_template('public/register.html')

@app.route('/login')
def login():
	return render_template('public/login.html')