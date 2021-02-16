# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:48:06 2021

@author: HS
"""

import csv
import matplotlib.pyplot as plt


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
result = []
for row in raw_data:
    if "신도림" in row[0]:
        for row2 in row[3:104]:
            result.append(int(row2.replace(",", ""))) 
            

min 
result2 = []

for idx0, row2 in enumerate(raw_data[1:]):
    if "신도림" not in row[0]:
        for idx1, row3 in enumerate(row2[3:104]):
            result2.append(abs(result[idx1] - int(row3.replace(",",""))))
            
        min = sum(result2)
    
        if min < sum(result2):
            min = sum(result2)
            
        result2 = []
        
        
        

plt.plot(result2)
        

for idx0, row2 in enumerate(raw_data[1:]):
    for()
'''      

#신도림 그 외의
result2 = []
for row in raw_data:
    if "신도림" in row[0]:
        for row2 in row[3:104]:
            result2.append( int(row2.replace(",", "")) / int(row[2].replace(",", "")) )


total_list = []
result3 = []
min = 9999



for idx0, row in enumerate(raw_data[1:]):
    if "신도림" not in row[0]:
        if "출장" not in row[0]:
            for idx1, row2 in enumerate(row[3:104]):
                result3.append( abs(result2[idx1] - (int(row2.replace(",","")) / int(row[2].replace(",", ""))) ) )
                
            if(sum(result3)<min):
                min=sum(result3)
                final_idx = idx0
                
            result3 = []



for idx2 in raw_data:
    if "경기도하남" in row[0]:
        for row3 in row[3:104]:
            ab.append (int(row3.replace(",","")))
        
        
print(ab)        
#print(final_idx)    

plt.plot(ab)
#plt.plot(result2)
#plt.plot(result2)

               
print(raw_data[final_idx+1][0])       

    
                    
                    
                        
# 비율로 계산하여 그래프 그리기




          