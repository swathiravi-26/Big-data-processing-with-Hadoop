#!/usr/bin/env python

import sys


for line in sys.stdin:
    line = line.strip()
    data = line.split(",")

    employeeId = "-1"
    name = "-1"
    salary = "-1"
    passCode = "-1"
    country = "-1"

 

    if len(data) == 4:
        continue

    if len(data) == 2:
        employeeId = data[0]
        name = data[1]

    else:
        employeeId = data[0]
        salary = data[1] + "," + data[2]
        country = data[3]
        passCode = data[4]

    print ('%s\t%s\t%s\t%s\t%s' % (employeeId,name,salary,country,passCode))
    
