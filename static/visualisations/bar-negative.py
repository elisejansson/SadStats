"""
	Title:			Bar chart negative stack visualiser
	Author: 		Matthew Cohen
	Stdnt number:	763090
	Class:			INFO20001, Foundations of Informatics
	Date: 			20/05/17
"""
# translates value to a percentage
HUNDRED = 100

import csv
import json
from collections import defaultdict

csvfile = open('data.csv', 'r')
#jsonfile = open('bar_chart_negative.json')

# dictionaries for counting the number of deaths for each causes in a given year
deaths2003 = defaultdict(int)
deaths2013 = defaultdict(int)
causes = []
percentages = []

# reading values into a single dictionary
fieldnames = ("YEAR", "CAUSE_NAME", "STATE", "DEATHS", "AADR")
reader = csv.DictReader(csvfile, fieldnames)
# transferring only the values we need to other dictionaries
for row in reader:

    if row["YEAR"] == "2003":
        if row["STATE"] == "United States":
            cause = row["CAUSE_NAME"]
            deaths2003[cause] = float(row["DEATHS"])

            causes.append(cause) # creating list of all causes

    if row["YEAR"] == "2013":
        if row["STATE"] == "United States":
            cause = row["CAUSE_NAME"]
            deaths2013[cause] = float(row["DEATHS"])

# computation
for cause in causes:
    percent = (1 - deaths2003[cause]/deaths2013[cause]) * HUNDRED
    percentages.append(float("{:.2f}".format(percent))

# writing to a file
print(causes)
print(percentages)

# close files
csvfile.close()
#jsonfile.close()
