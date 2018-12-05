from flask import Flask
from flask import request, render_template
from PIL import Image
app = Flask(__name__)

def justsave(picture):
    picture.save('./images/result_image.jpg')
    return picture

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form/', methods=['POST','GET'])
def  form():
	if request.method=='POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

@app.route('/upload/', methods=['POST','GET'])
def  upload():
	if request.method=='POST':
		file = request.files['photo']
		result = justsave(Image.open(file))
		return render_template('result.html')
	else:
		return render_template('upload.html')

app.run(debug=True)
