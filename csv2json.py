""" 
	Title:			CSV to JSON converter.
	Author: 		Matthew Cohen
	Stdnt number:		763090
	Class:			INFO20001, Foundations of Informatics
	Date: 			14/05/17
"""

import csv
import json

csvfile = open('data.csv', 'r')
jsonfile = open('jsondata.json', 'w')

fieldnames = ("YEAR", "CAUSE_NAME", "STATE", "DEATHS", "AADR")
reader = csv.DictReader(csvfile, fieldnames)

i = 0
jsonfile.write("{")
for row in reader:
	jsonfile.write('"{:04d}":'.format(i))
	json.dump(row, jsonfile)
	jsonfile.write(',\n')
	i += 1
jsonfile.write("}")
