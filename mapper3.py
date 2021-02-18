#!/usr/bin/env python

from sys import stdin
import re
import os

for line in stdin:
	doc_id = os.environ["map_input_file"]
	doc_id =re.findall(r'\w+',doc_id)[-2]
	words= re.findall(r'\w+',line.strip())
	for word in words:
		print("%s\t%s:1"%(word.lower(),doc_id))


