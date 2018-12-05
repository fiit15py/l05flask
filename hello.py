from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/formhello',methods=['POST','GET'])
def formhello():
	if request.method =='GET':
		return render_template('form.html')
	else:
		text = request.form['name']
		return "<H1>Hello, {}!<H1>".format(text)

app.run(debug=True)