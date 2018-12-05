import os
from flask import Flask, request, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = 'C:\\fiit15\\l05flask\\images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'yay'
    return render_template('upload.html')

@app.route('/formhello', methods=['POST', 'GET'])
def formhello():
	if request.method == 'GET':
		return render_template('form.html')
	else:
		return "Helloooooo"

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
