from flask import Flask
from flask import render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def convert_to_csv(data):
    with open('database.csv',newline='', mode='a') as database:
        username = data['user_name']
        email = data['email']
        subject = data['subject']
        contents = data['contents']
        data_Writer = csv.writer(database, delimiter='|')
        data_Writer.writerow([username, email, subject, contents])

@app.route('/submit_form', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        convert_to_csv(data)
        return render_template('thankyou.html', context=data)
    else:
        return 'Something went wrong , Buddy check out !!'
