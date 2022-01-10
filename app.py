from flask import Flask
from faker import Faker
import requests
import base58
import csv

app = Flask(__name__)
not_good = Faker()

@app.route("/")
def index():
    return'<p><h2>Hillel Task 9 (Flask)</h2></p>'

# ***** 01 *****

filename = 'requirements.txt'

@app.route("/requirements")
def reading_file():
    with open(filename, 'r') as file:
        result = file.read()
        return result

# ***** 02 *****

@app.route("/generate-users/<int:number>")
def create_user(number):
    users = {}
    for _ in range(number):
        name=not_good.name()
        email=not_good.email()
        fields={name: email}
        users.update(fields)
    return users

# ***** 03 *****

@app.route('/mean')
def process_csv():
    try:
        with open("hw05.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            row_count = 0
            all_height = 0
            all_weight = 0
            for row in reader:
                if row:
                    row_count = row_count + 1
                    all_height = all_height + float(row[1])
                    all_weight = all_weight + float(row[-1])
            high = all_height / row_count * 2.54
            weight = all_weight / row_count / 2.2046
            results = f"Parsed file: 'hw05.csv' <br>Total values in file (strings of data): {row_count} \
                      <br>Average height: {high}cm <br> Average weight: {weight}kg "
            return results
    except IOError:
        return "File 'hw05.csv' not found"

# ***** 04 *****

@app.route('/space/')
def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()

# ***** 05 *****

@app.route('/base58encode/<string>')
def encode(string):
    return base58.b58encode(string)

# ***** 06 *****

@app.route('/base58decode/<STRING_IN_BASE58>')
def decode(STRING_IN_BASE58):
    return base58.b58decode(STRING_IN_BASE58)