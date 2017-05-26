"""
	Title:			Pie Chart Script
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

deaths = defaultdict(int)


fieldnames = ("YEAR", "CAUSE_NAME", "STATE", "DEATHS", "AADR")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    if row["CAUSE_NAME"] == "All c"





# close files
csvfile.close()
