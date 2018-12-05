from flask import Flask
from flask import request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form/', methods=['POST','GET'])
def  form():
	if request.method=='POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

app.run(debug=True)
