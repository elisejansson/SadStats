import pandas as pd
import csv

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
                    row[item] = 0
                elif row[item] == '*':
                    row[item] = 0
                else:
                    row[item] = float(row[item])
    return raw_data



#def pivot(pt_index, pt_values, pt_filtering, csv_list):
def pivot(pt_index, pt_values):
#def pivot():
    raw_data = get_csv()
    data = correct_types(raw_data)
    #data = correct_types(csv_list)
    df = pd.DataFrame(data, columns = ['YEAR', 'CAUSE_NAME', 'STATE', 'DEATHS', 'AADR'])

    #read in data
    #read in filters and filter
    #read in index and values


    pivot_table = pd.pivot_table(df,index=pt_index,values=pt_values) #to json
    print pivot_table
    #return pivot_table

pivot(["CAUSE_NAME","YEAR"],["DEATHS"])
