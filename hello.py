import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

dirname, filename = os.path.split(os.path.abspath(__file__))
UPLOAD_FOLDER = dirname + '/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# РЕШЕНИЕ ЗАДАЧИ 1
@app.route('/form/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        return render_template('user.html', name=request.form['name'])
    else:
        return render_template('form.html')


# РЕШЕНИЕ ЗАДАЧИ 2
@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename, fextension = secure_filename(file.filename).split('.')
            filename2 = len([name for name in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, name))])
            fullname2 = filename2.__str__() + '.' + fextension;
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], fullname2))
            return render_template('success.html', name=filename, name2=fullname2)
    else:
        return render_template('upload.html')

app.run(debug=True)
