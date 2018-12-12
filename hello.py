from flask import Flask
from flask import request, render_template
from PIL import Image
import numpy as np
import requests
import json
app = Flask(__name__)

addr = 'http://10.14.129.242:5000/upload'
fiit15 = np.load('facevec.npy')
labels = json.load(open('labels.json'))

def justsave(picture):
    picture.save('./images/result_image.jpg')
    return picture

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form/', methods=['POST', 'GET'])
def form():
	if request.method == 'POST':
		return render_template('user.html', name=request.form['name'])
	else:
		return render_template('form.html')

@app.route('/upload/', methods=['POST','GET'])
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
			return render_template('result.html', value= 'Я думаю это ' + labels[j] + ' похожесть '+ '%.2f' % (A[j]*100) + '%      '+str(j))
		else:
			return render_template('result.html', value= 'Нет совпадений, больше всего похоже на ' + labels[j] + ' похожесть '+ '%.2f' % (A[j]*100) + '%      '+str(j))
	else:
		return render_template('upload.html')

app.run(debug=True)
