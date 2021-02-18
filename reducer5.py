#!/usr/bin/env python
import sys
import re
K=13
d={}
predictions={}
for line in sys.stdin:
	line = line.strip()
	testno,dist,label= line.split('&&')
	testno=int(testno)
	label=int(label)
	dist=float(dist)
	try:
		d[testno].append((dist,label))
	except:
		d[testno]=[]
		d[testno].append((dist,label))
for key, val in sorted(d.items()):
	temp=sorted(val,key=lambda x:x[0])[:K]
	l=[]
	for i in range(K):
		l.append(temp[i][1])
	pred = max(set(l),key=l.count)
	print("%s\t%s"%(key,pred))


	