import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '.\images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formhello', methods=['POST', 'GET'])
def formhello():
	if request.method=='POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/form', methods=['POST', 'GET'])
def form():
	if request.method == 'POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		if 'pic' not in request.files:
			return "fail"	
		file = request.files['pic']
		if file.filename == '':
			return "fail"
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			if os.path.isdir(app.config['UPLOAD_FOLDER']):
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			else:
				os.makedirs(app.config['UPLOAD_FOLDER'])
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return "success"
	else:
		return render_template('formpic.html')

app.run(debug=True)
