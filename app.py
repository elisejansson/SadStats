import csv
import pandas as pd
import numpy as np
from flask import Flask
from flask import abort #error messageing
from flask import render_template #to combine data with html
#import pivot.py

app = Flask(__name__)

def get_csv():
    csv_path = './data.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj) #to create permanent list
    return csv_list   

@app.route("/api/pivottable")
def pivottable_api():
    #csv_list should have been passed as a global variable
    index = request.args.get('index')
    values = request.args.get('values')
    filtering = request.args.get('filtering')
    pivot_data = pivot(index, values, filtering, csv_list)
    #json_pivottable = pivot_data to json
    #set mime type to application/json
    return json_pivottable

@app.route("/api/pivottable")
def pivottable_api():
    #csv_list should have been passed as a global variable
    index = request.args.get('index')
    values = request.args.get('values')
    filtering = request.args.get('filtering')
    pivot_data = pivot(index, values, filtering, csv_list)
    #json_pivottable = pivot_data to json
    #set mime type to application/json
    return json_pivottable

@app.route("/pivottable")
def pivottable():
    template = 'pivottable.html'
    return render_template(template)


@app.route("/navbar")
def navbar():
    template = 'navbar.html'
    return render_template(template)


@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)

@app.route("/about")
def about():
    template = 'about.html'
    return render_template(template)

@app.route("/findings")
def findings():
    template = 'findings.html'
    return render_template(template)


if __name__ == '__main__':
    # Fire up the Flask test server
    csv_list = get_csv()
    print csv_list
    app.run(debug=True, use_reloader=True)
