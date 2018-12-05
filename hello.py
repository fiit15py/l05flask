from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		return render_template('user.html', name = request.form['name'])
	else:
		return render_template('login.html');

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

app.run(debug = True)
