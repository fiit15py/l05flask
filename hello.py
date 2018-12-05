from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formhello', methods=['POST', 'GET'])
def formhello():
	if request.method=='GET':
		return render_template('form.html')
	else:
		return "Hello"

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__' :
app.run(debug=True)
