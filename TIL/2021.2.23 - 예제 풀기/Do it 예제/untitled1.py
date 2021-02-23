# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:26:13 2021

@author: HS
"""

class Caculator:
    def __init__(self):
        self.value = 0
        
    def add(self,val):
        self.value += val        
    
        
class UpgradeCalculator(Caculator):
    def minus(self,val):
        self.value -= val
        
        
class MaxLimitCalculator()
        
        
cal =  MaxLimitCalculator()         
cal = UpgradeCalculator()       
cal.add(50)
cal.minus(60)

print(cal.value)
