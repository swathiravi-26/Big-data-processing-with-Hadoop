#!/usr/bin/env python

import sys

input_1 = {}
input_2 = {}

for line in sys.stdin:
    line = line.strip()
    employeeID, name, salary, country, passcode = line.split('\t')

    if salary == "0":
        input_1[employeeID] = name
    else:
        input_2[employeeID] = [salary,country,passcode]

for employeeID in input_2.keys():
    name = input_1[employeeID]
    salary = input_2[employeeID][0]
    country = input_2[employeeID][1]
    passcode = input_2[employeeID][2]

    print ('%s\t%s\t%s\t%s\t%s'% (employeeID,name,salary,country,passcode))
