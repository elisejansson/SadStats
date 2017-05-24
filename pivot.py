import pandas as pd
import numpy as np
import csv
import seaborn as sns


def get_csv():
    csv_path = './data.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj) #to create permanent list
    return csv_list


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


def clean_list(pt_list):
    new_list = []
    for item in pt_list:
        if item != 'None':
            new_list.append(item)
    return new_list


def clean_dict(pt_filtering):
    for item in pt_filtering:
        if pt_filtering[item] == 'None':
            pt_filtering[item] = None
    return pt_filtering


def clean_aggfunc(pt_aggfunc):
    if pt_aggfunc == 'np.mean':
        return np.mean
    else:
        return np.sum


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


def get_caption(values_list, filtering_dict, func):
    year = ' '
    cause = ' '
    state = ' '
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

    caption = funct + value + cause + state + year
    return caption





def pivot(pt_index, pt_columns, pt_values, pt_filtering, pt_aggfunc):

    raw_data = get_csv()
    data = correct_types(raw_data)

    pt_index = clean_list(pt_index)
    pt_columns = clean_list(pt_columns)
    pt_values = clean_list(pt_values)
    pt_filtering = clean_dict(pt_filtering)
    pt_aggfunc = clean_aggfunc(pt_aggfunc)

    filtered_data = filter_data(data, pt_filtering)

    df = pd.DataFrame(filtered_data, columns = ['YEAR', 'CAUSE_NAME', 'STATE', 'DEATHS', 'AADR'])

    pivot_table = pd.pivot_table(df, index=pt_index, columns=pt_columns,
    values=pt_values, aggfunc=pt_aggfunc)

    cm = sns.light_palette( '#35CBF4', as_cmap=True)

    caption = get_caption(pt_values, pt_filtering, pt_aggfunc)

    pivot_table_f = pivot_table.round(2).style.set_caption(str(caption)).background_gradient(cmap=cm).set_properties(**{'border': '1px solid black', 'padding': '5px', 'text-align': 'center'})
    pivot_table_final = pivot_table_f.render()

    return pivot_table_final
