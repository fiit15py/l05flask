import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

from PIL import Image

import json
labels=json.load(open('labels.json'))
import numpy as np
fiit15=np.load('facevec.npy') 
import requests
addr = 'http://10.14.129.242:5000/upload'

app = Flask(__name__)

def justsave(picture):
    picture.save('./images/result_image.jpg')
    return picture

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('login.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/upload', methods=['GET', 'POST'])
def  upload():
	if request.method=='POST':
		file = request.files['photo']
		result = justsave(Image.open(file))
		files = {'image':open('./images/result_image.jpg','rb')}
		response = requests.post(addr, files=files)
		vec = np.array(json.loads(response.content))
		A = [np.dot(fiit15[i],vec) for i in range(fiit15.shape[0])]
		npA = np.array(A)
		j = npA.argmax()
		if A[j] > 0.6:
			return render_template('result.html', value= 'Я думаю это ' + labels[j] + ' похожесть '+ '%.2f' % (A[j]*100) + '%')
		else:
			return render_template('result.html', value= 'Нет совпадений, больше всего похоже на ' + labels[j] + ' похожесть '+ '%.2f' % (A[j]*100) + '%')
	else:
		return render_template('upload.html')
	
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

app.run(debug=True)