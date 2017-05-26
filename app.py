import csv
from flask import Flask
from flask import request
from flask import abort #error messageing
from flask import render_template #to combine data with htmls
from pivot import pivot #pivot table function


app = Flask(__name__)


@app.route("/pivottable_results", methods=['GET'])
def pivottable_api():

    #get index values from user interface
    index_y = request.args.get('index_y')
    index_c = request.args.get('index_c')
    index_s = request.args.get('index_s')
    index = [str(index_y), str(index_c), str(index_s)]

    #get value values from user interface
    value_a = request.args.get('value_a')
    value_d = request.args.get('value_d')
    values = [str(value_a), str(value_d)]

    #get column values from user interface
    column_y = request.args.get('column_y')
    column_c = request.args.get('column_c')
    columns = [str(column_c), str(column_y)]

    #get desired aggfunc from user interface
    aggfunc = str(request.args.get('aggfunc'))

    #get filters from user interface
    filter_y = request.args.get('filter_y')
    filter_s = request.args.get('filter_s')
    filter_c = request.args.get('filter_c')
    filtering = {'YEAR':str(filter_y),'STATE':str(filter_s),'CAUSE_NAME':str(filter_c)}

    #read requirements into pivot() to produce html pivottable and provide template
    pivot_data = pivot(index, columns, values, filtering, aggfunc) #returns as html script
    template = 'pivotTable.html'

    #return the rendered template with the pivot table
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
    app.run(debug=True, use_reloader=True)
