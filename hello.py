import os
from flask import Flask, request, render_template, url_for, redirect, send_from_directory
from werkzeug.utils import secure_filename

upload_folder = "./images/"
Allowed_extensions = set(['png','jpg','jpeg','gif'])

app = Flask(__name__)
app.config['Upload_folder'] = upload_folder 
app.config['Max_content_length'] = 16 * 1024 * 1024 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formhello', methods=['POST', 'GET'])
def formhello():
	if request.method == 'POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

def allowed_file(filename):
	return '.' in filename and \
	filename.rsplit('.', 1)[1].lower() in Allowed_extensions

@app.route('/upload', methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		if 'image' not in request.files:
			return render_template('upload.html', message='No file part')
		file = request.files['image']
		if file.filename == '':
			return render_template('upload.html', message='No file selected')
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['Upload_folder'],filename))
			return redirect(url_for('upload_file', filename=filename))
		return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

app.run(debug=True)
