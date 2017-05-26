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

# close files
csvfile.close()
