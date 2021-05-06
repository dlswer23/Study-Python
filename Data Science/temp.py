# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv

f = open("D:/leb/temperature.csv")
data = csv.reader(f)

raw_data = []
    
for row in data:
    raw_data.append(row)
 


max = 0


for idx, row in enumerate(raw_data[8:]):
    if(row):
        if(row[4]):
            if max < float(row[4]):
                max = float(row[4]) 
                #max_flag는 if문이 몇번 돌아갔는지 알려준다
                max_flag = idx
                place = idx
                
         

print(raw_data[max_flag+8][0], max, raw_data[place+8][2])
#첫번째 : 최고기온의 날짜 / 두번째 : 최고기온 / 세번째 : 최고기온의 평균기온


print(raw_data[9])
#9번째 한 줄을 전체적으로 출력한다.

        
    
 
