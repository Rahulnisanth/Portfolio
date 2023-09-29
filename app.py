from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        return render_template('thankyou.html', context=data)
    else:
        return 'Something went wrong , Buddy check out !!'
