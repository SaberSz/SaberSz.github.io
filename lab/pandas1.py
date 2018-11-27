# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:38:22 2018

@author: Devaraja
"""
import pandas as pd
#Creating a pandas dataframe
data = {'Gender': ['F', 'M', 'M'],'Emp_ID': ['E01', 'E02','E03'], 'Age': [25, 27, 25]}
# We want the order the columns, so lets specify in columns parameter
df = pd.DataFrame(data, columns=['Emp_ID','Gender', 'Age'])
print(df)