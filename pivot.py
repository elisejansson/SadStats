import pandas as pd
import numpy as np
import csv
import seaborn as sns

#function to create list of dictionaries from csv file
def get_csv():
    csv_path = './data.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

#function to correct the types in the list of data
def correct_types(raw_data):
    for row in raw_data:
        for item in row:
            if item == 'YEAR':
                row[item] = str(row[item])
            elif item == 'CAUSE_NAME':
                row[item] = str(row[item])
            elif item == 'STATE':
                row[item] = str(row[item])
            elif item == 'DEATHS':
                if row[item] == 'x':
                    row[item] = 0
                else:
                    row[item] = int(row[item])
            elif item == 'AADR':
                if row[item] == 'x':
                    row[item] = None
                elif row[item] == '*':
                    row[item] = None
                else:
                    row[item] = float(row[item])
    return raw_data

#function to clean up the user input lists
def clean_list(pt_list):
    new_list = []
    for item in pt_list:
        if item != 'None':
            new_list.append(item)
    return new_list

#function to clean up the user input filter dictionary
def clean_dict(pt_filtering):
    for item in pt_filtering:
        if pt_filtering[item] == 'None':
            pt_filtering[item] = None
    return pt_filtering

#function to clean up aggfunc reques
def clean_aggfunc(pt_aggfunc):
    if pt_aggfunc == 'np.mean':
        return np.mean
    else:
        return np.sum

#function to filter the data based on the filtering specifications
def filter_data(data, filtering):
    filtered_data = []
    for row in data:
        is_appropriate = 0
        num_conditions = 3
        for condition in filtering:
            if filtering[condition] == None:
                num_conditions -= 1
                for item in row:
                    if row[item] == 'All Causes' or row[item] == 'United States':
                        is_appropriate -= 3
            else:
                for item in row:
                    if row[item] == 'All Causes' or row[item] == 'United States':
                        is_appropriate -= 3
                    elif item == condition:
                        if filtering[condition] == row[item]:
                            is_appropriate += 1
        if is_appropriate == num_conditions:
            filtered_data.append(row)
    return filtered_data

#fuction to fetch the caption from the user input
def get_caption(values_list, filtering_dict, func):
    year = ' '
    cause = ' '
    state = ' '

    #find all of the parts of the caption from the user imput
    if filtering_dict['YEAR'] != None:
        year = ' in the year ' + filtering_dict['YEAR']
    if filtering_dict['STATE'] != None:
        state = ' in the state of ' + filtering_dict['STATE']
    if filtering_dict['CAUSE_NAME'] != None:
        cause = ' for ' + filtering_dict['CAUSE_NAME']
    if func == np.mean:
        funct = 'Average '
    elif func == np.sum:
        funct = 'Total '
    if values_list == ['DEATHS']:
        value = 'deaths'
    elif values_list == ['AADR']:
        value = 'AADR'
    else:
        value = 'deaths and AADR'

    #add the caption parts together and return
    caption = funct + value + cause + state + year
    return caption

#fuction that is called by the app, that returns the pivot table in a html form
def pivot(pt_index, pt_columns, pt_values, pt_filtering, pt_aggfunc):

    #get the data list from the csv and correct the types
    raw_data = get_csv()
    data = correct_types(raw_data)

    #do the cleanups on the user input
    pt_index = clean_list(pt_index)
    pt_columns = clean_list(pt_columns)
    pt_values = clean_list(pt_values)
    pt_filtering = clean_dict(pt_filtering)
    pt_aggfunc = clean_aggfunc(pt_aggfunc)

    #filter the data according to the specifications
    filtered_data = filter_data(data, pt_filtering)

    #build the data frame using pandas
    df = pd.DataFrame(filtered_data, columns = ['YEAR', 'CAUSE_NAME', 'STATE',
        'DEATHS', 'AADR'])

    #build the pivot table
    pivot_table = pd.pivot_table(df, index=pt_index, columns=pt_columns,
    values=pt_values, aggfunc=pt_aggfunc)

    #create the colour map and caption
    cm = sns.light_palette( '#35CBF4', as_cmap=True)
    caption = get_caption(pt_values, pt_filtering, pt_aggfunc)

    #style the pivot table using the colour map and caption, render to html
    pivot_table_f = pivot_table.round(2).style\
        .set_caption(str(caption)).background_gradient(cmap=cm)\
        .set_properties(**{'border': '1px solid black', 'padding': '5px', \
        'text-align': 'center'})
    pivot_table_final = pivot_table_f.render()

    #return the coloured and styled pivot table to the app to be rendered
    #in the template
    return pivot_table_final
