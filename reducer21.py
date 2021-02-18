#!/usr/bin/env python
import sys
import re
from collections import Counter
 
word = {}
 

for line in sys.stdin:
	line = line.strip()
	trigram, count= line.split('\t',1)
	count = int(count)
	word[trigram] = word.get(trigram,0) + count
	
result = Counter(word)
tops = result.most_common(10)
for top in tops:
	print("%s\t%s"%(top[0],top[1]))
print("done")
