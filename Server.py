from flask import Flask, render_template, url_for, request, redirect
import csv
import os

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def go_to(page_name):
    return render_template(page_name)

def write_to_csv(data):
    file_exists = os.path.isfile('database2.csv')
    with open('database2.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
        if not file_exists:
            csv_writer.writerow(["email", "subject", "message"])
        csv_writer.writerow([email,subject,message])

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Something wet wrong!'
    else:
        return 'something went wrong.'