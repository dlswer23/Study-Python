# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:38:47 2021

@author: HS
"""

import csv

f = open('D:/leb/현황.csv')

data = csv.reader(f)

raw_data = []
for row in data:
    raw_data.append(row)
    
      
for idx, row in enumerate(raw_data[1:]):
    #if(row):        
    if ('신도림' in row[0]):
        result = row
'''        
max =0   
for idx, row in enumerate(raw_data[8:]):
    if(row):
        if(row):
            if max < int(row)
                max =int(row)'''
                
result = []
for idx, row in enumerate(raw_data[1:]):
    a = row[1].replace(",","")
    if(int(a) > 10000):
        result.append(row)
                
                              
           