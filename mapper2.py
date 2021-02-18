#!/usr/bin/env python
import sys
import re
from nltk.stem import PorterStemmer

for temp in sys.stdin:
	temp = temp.strip()
	temp = temp.lower()
	ps = PorterStemmer()
	l= ["science","sea","fire"]
	line = re.findall(r"[A-Za-z]+'?[a-z]*",temp)
	for i in range(len(line)):
		temp = ps.stem(line[i])
		if temp in l:
			line[i]="$"
	ls = list()
	for i in range (len(line)-2):
		s=""
		if line[i]=="$" or line[i+1]=="$" or line[i+2]=="$":
			s=line[i]+'_'+line[i+1]+'_'+line[i+2]
			ls.append(s)
	for lsans in ls:
		print("%s\t%s" % (lsans,1))