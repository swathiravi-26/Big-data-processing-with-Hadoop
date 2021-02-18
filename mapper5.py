#!/usr/bin/env python

import pandas as pd 
import numpy as np
lis=[]
data = pd.read_csv("Test.csv")

nptest = data.values




for line in data:
    temp = line.strip()
    print(temp)
    temp1 = temp.split(',')
    label = temp[-1]
    train = temp[0:-1]
    nptrain = np.asarray(train,dtype=np.float64)
    nptrain = nptrain.T
    num_test = nptest.shape[0]
    for i in range(num_test):
        row = nptest[i]
        dist = np.linalg.norm(row-nptrain)
        print("%s&&%s&&%s"%(i,dist,label))
 
