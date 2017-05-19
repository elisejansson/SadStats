import csv
import pandas as pd
import numpy as np
from flask import Flask
from flask import abort #error messageing
from flask import render_template #to combine data with html
app = Flask(__name__)

def get_csv():
    csv_path = './data.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj) #to create permanent list
    return csv_list

@app.route("/pivottable")
def pivottable():
    template = 'pivottable.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route("/navbar")
def navbar():
    template = 'navbar.html'
    return render_template(template)

@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)


if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
