# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:18:53 2018

@author: Devaraja
"""

import numpy as np
import pandas as pd

data=pd.read_csv('finds.csv')

data

def train(concepts,target):
    specific_h=concepts[0]
    for i,h in enumerate(concepts):
        if target[i]=="Yes":
            for x in range(len(specific_h)):
                if h[x]==specific_h[x]:
                    pass
                else:
                    specific_h[x]="?"
    return specific_h
concepts=np.array(data.iloc[:,0:-1])
target=np.array(data.iloc[:,-1])

target

concepts
print(train(concepts,target))
specific_h=train(concepts,target)

indices=np.where(specific_h=="?")

def predict(h,specific_h):
    indices=np.where(specific_h=="?")
    d=list(specific_h)
    for i, val in enumerate(specific_h):
        if val==h[i]:
            d[i]=True
        else:
            d[i]=False
    for i in indices[0]:
        d[i]=True
    return all(d)

print(predict(concepts[2],specific_h))

