import pandas as pd
import csv

def get_csv():
    csv_path = './data.csv'
    csv_file = open(csv_path, 'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj) #to create permanent list
    #print csv_list
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
                    row[item] = 0
                elif row[item] == '*':
                    row[item] = 0
                else:
                    row[item] = float(row[item])
    return raw_data

def filter_data(data, filtering):
    filtered_data = []
    for row in data:
        is_appropriate = 0
        num_conditions = 3
        for condition in filtering:
            if filtering[condition] == None:
                num_conditions -= 1
            else:
                for item in row:
                    if item == condition:
                        if filtering[condition] == row[item]:
                            is_appropriate += 1
        if is_appropriate == num_conditions:
            filtered_data.append(row)

    return filtered_data

#def pivot(pt_index, pt_values, pt_filtering, csv_list):
def pivot(pt_index, pt_columns, pt_values, pt_filtering):
#def pivot():
    raw_data = get_csv()
    #data = correct_types(csv_list)
    data = correct_types(raw_data)
    filtered_data = filter_data(data, pt_filtering)
    df = pd.DataFrame(filtered_data, columns = ['YEAR', 'CAUSE_NAME', 'STATE', 'DEATHS', 'AADR'])

    #read in data
    #read in filters and filter
    #read in index, columns and values


    pivot_table = pd.pivot_table(df, index=pt_index, columns=pt_columns,
    values=pt_values, margins=True)
    #json_pt = pivot_table.to_json(double_precision=2,orient='columns')
    print pivot_table
    #print json_pt
    #return json_pt

pivot(["CAUSE_NAME", "STATE"], ["YEAR"], ["DEATHS"], {'YEAR':'2003','STATE':None,'CAUSE_NAME':'Homicide'})
