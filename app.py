import csv
import pandas as pd
from flask import Flask
from flask import request
import pivot
from flask import abort #error messageing
from flask import render_template #to combine data with html


app = Flask(__name__)

def get_csv():
    csv_path = './data.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj) #to create permanent list
    return csv_list

@app.route("/api/pivottable", methods=['GET'])
def pivottable_api():

    # #csv_list should have been passed as a global variable
    index_y = request.args.get('index_y')
    index_c = request.args.get('index_c')
    index_s = request.args.get('index_s')
    index = [str(index_y), str(index_c), str(index_s)]

    values_a = request.args.get('values_a')
    values_d = request.args.get('values_d')
    values = [str(values_a), str(values_d)]

    columns_y = request.args.get('columns_y')
    columns_c = request.args.get('columns_c')
    columns = [str(columns_c), str(columns_y)]

    aggfunc_s = request.args.get('aggfunc_s')
    aggfunc_m = request.args.get('aggfunc_m')
    aggfunc = [str(aggfunc_m), str(aggfunc_s)]

    filtering_y = request.args.get('filtering_y')
    filtering_s = request.args.get('filtering_s')
    filtering_c = request.args.get('filtering_c')

    filtering = {'YEAR':filtering_y,'STATE':filtering_s,'CAUSE_NAME':filtering_c}

    return str(values)
    #pivot_data = pivot(index, columns, values, filtering, aggfunc, csv_list) #returns as html script
    #set mime type to application/json

    #return pivot_data

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
    app.run(debug=True, use_reloader=True)
