import csv
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


app = Flask(__name__)

# Read data from a CSV file
def read_data():
    data = []
    with open('employees.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Data Page
@app.route('/data')
def data():
    data = read_data()
    return render_template('data.html', data=data)

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
