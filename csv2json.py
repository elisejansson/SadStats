""" 
	Title:			CSV to JSON converter.
	Author: 		Matthew Cohen
	Stdnt number:	763090
	Class:			INFO20001, Foundations of Informatics
	Date: 			14/05/17
"""

import csv
import json

csvfile = open('data.csv', 'r')
jsonfile = open('jsondata.json', 'w')

fieldnames = ("YEAR", "CAUSE_NAME", "STATE", "DEATHS", "AADR")	# columns
reader = csv.DictReader(csvfile, fieldnames)

i = 0				# counter for number of data values
jsonfile.write("{")	# starts parent object. Not sure if necessary 

# iterates through every row and writes a new JSON object
for row in reader:
	jsonfile.write('"{:04d}":'.format(i))	# not sure if this step is necessary	
	json.dump(row, jsonfile)
	jsonfile.write(',\n')
	i += 1
	
jsonfile.write("}")	# closes parent object
