# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:05:50 2020

@author: Josh
"""

class Deduction:
    def __init__(self,amount):
        self.__amount = amount
        
    def set_amount(self, amount):
        self.__amount = amount
        
    def get_amount(self):
        return self.__amount
    
class RRSP(Deduction):
    def __init__(self, amount):
        Deduction.__init__(self, amount)
        
class Other(Deduction):
    def __init__(self, amount):
        Deduction.__init__(self, amount)