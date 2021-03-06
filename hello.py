from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formhello', methods=['POST', 'GET'])
def formhello():
	if request.method == 'GET':
		return render_template('form.html')
	else:
		return "Hello"

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/form', methods=['POST', 'GET'])
def form():
	if request.method == 'POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

app.run(debug=True)
