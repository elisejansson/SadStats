import csv
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
from flask import abort #error messageing
from flask import render_template #to combine data with htmls
from pivot import pivot


app = Flask(__name__)

def get_csv():
    csv_path = './data.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj) #to create permanent list
    return csv_list

@app.route("/pivottable_results", methods=['GET'])
def pivottable_api():

    index_y = request.args.get('index_y')
    index_c = request.args.get('index_c')
    index_s = request.args.get('index_s')
    index = [str(index_y), str(index_c), str(index_s)]

    value_a = request.args.get('value_a')
    value_d = request.args.get('value_d')
    values = [str(value_a), str(value_d)]

    column_y = request.args.get('column_y')
    column_c = request.args.get('column_c')
    columns = [str(column_c), str(column_y)]

    aggfunc = str(request.args.get('aggfunc'))

    filtering_y = request.args.get('filtering_y')
    filtering_s = request.args.get('filtering_s')
    filtering_c = request.args.get('filtering_c')
    filtering = {'YEAR':str(filtering_y),'STATE':str(filtering_s),'CAUSE_NAME':str(filtering_c)}

    pivot_data = pivot(index, columns, values, filtering, aggfunc, csv_list) #returns as html script
    template = 'pivotTable.html'

    return render_template(template, table=pivot_data)


@app.route("/pivottable_form")
def pivottable():
    template = 'pivotForm.html'
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
    app.run(debug=True, use_reloader=True)
