from flask import Flask, render_template, request
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template ('index html')

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

app.run(debug=True)