from flask import Flask, render_template, request
app = Flask(__name__)
 
 
@app.route('/')
def index():
<<<<<<< HEAD
    return render_template ('index html')
=======
    return render_template('index.html')

@app.route('/formhello', methods=['POST', 'GET'])
def formhello():
	if request.method == 'GET':
		return render_template('form.html')
	else:
		return "Hello"
>>>>>>> master

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name) 

@app.route('/formhello',methods=['POST','GET'])
def formhello():
    if request.method=='GET':
        return render_template('form.html')
    else:
        text = request.form['name']
        return "HELLO,{}!".format(text)

<<<<<<< HEAD
app.run(debug=True)
=======
@app.route('/form', methods=['POST', 'GET'])
def form():
	if request.method == 'POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

app.run(debug=True)
>>>>>>> master
