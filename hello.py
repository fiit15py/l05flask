from flask import Flask
from flask import request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formhello', methods=['POST','GET'])
def formhello():
    if request.method=='GET':
    	return render_template('form.html')
    else:
    	return "HELLO"

app.run(debug=True)
