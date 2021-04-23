# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:19:35 2020

@author: Josh
"""

class Income:
    def __init__(self,amount):
        self.__amount = amount
        
    def set_amount(self, amount):
        self.__amount = amount
        
    def set_tax_amount(self):
        if self.__amount > 220000:
            self.__tax_amount = ((self.__amount - 220000) * 0.5353) + 82296.7276
        elif self.__amount > 210371:
            self.__tax_amount = ((self.__amount - 210371) * 0.5197) + 77292.5363
        elif self.__amount > 150000:
            self.__tax_amount = ((self.__amount - 150000) * 0.4797) + 48332.5676
        elif self.__amount > 147667:
            self.__tax_amount = ((self.__amount - 147667) * 0.4641) + 47249.8223
        elif self.__amount > 95259:
            self.__tax_amount = ((self.__amount - 95259) * 0.4341) + 24499.5095
        elif self.__amount > 91101:
            self.__tax_amount = ((self.__amount - 91101) * 0.3791) + 22923.2117
        elif self.__amount > 87813:
            self.__tax_amount = ((self.__amount - 87813) * 0.3389) + 21808.9085
        elif self.__amount > 77313:
            self.__tax_amount = ((self.__amount - 77313) * 0.3148) + 18503.5085
        elif self.__amount > 47630:
            self.__tax_amount = ((self.__amount - 47630) * 0.2965) + 9702.499
        elif self.__amount > 43906:
            self.__tax_amount = ((self.__amount - 43906) * 0.2415) + 8803.153
        elif self.__amount > 0:
            self.__tax_amount = self.__amount * 0.2005
        else:
            self.__tax_amount = 0
        
    def get_amount(self):
        return self.__amount
    
    def get_tax_amount(self):
        return self.__tax_amount
    
class Employment(Income):
    def __init__(self, amount):
        Income.__init__(self, amount)
        
class Comission(Income):
    def __init__(self, amount):
        Income.__init__(self, amount)
        
class Pension(Income):
    def __init__(self, amount):
        Income.__init__(self, amount)
    
class Benefit(Income):
    def __init__(self, amount):
        Income.__init__(self, amount)
        
class Investment(Income):
    def __init__(self, gains, f_div, uf_div):
        self.__gains = gains
        self.__f_div = f_div
        self.__uf_div = uf_div
    
    def set_gains(self, gains):
        self.__gains = gains
    
    def set_f_div(self, f_div):
        self.__f_div = f_div
        
    def set_uf_div(self, uf_div):
        self.__uf_div = uf_div
        
    def set_gains_tax(self):
        if self.__gains > 220000:
            self.__gains_tax = ((self.__gains - 220000) * 0.2676) + 82296.7276
        elif self.__gains > 210371:
            self.__gains_tax = ((self.__gains - 210371) * 0.2598) + 77292.5363
        elif self.__gains > 150000:
            self.__gains_tax = ((self.__gains - 150000) * 0.2398) + 48332.5676
        elif self.__gains > 147667:
            self.__gains_tax = ((self.__gains - 147667) * 0.2320) + 47249.8223
        elif self.__gains > 95259:
            self.__gains_tax = ((self.__gains - 95259) * 0.2170) + 24499.5095
        elif self.__gains > 91101:
            self.__gains_tax = ((self.__gains - 91101) * 0.1895) + 22923.2117
        elif self.__gains > 87813:
            self.__gains_tax = ((self.__gains - 87813) * 0.1695) + 21808.9085
        elif self.__gains > 77313:
            self.__gains_tax = ((self.__gains - 77313) * 0.1574) + 18503.5085
        elif self.__gains > 47630:
            self.__gains_tax = ((self.__gains - 47630) * 0.1483) + 9702.499
        elif self.__gains > 43906:
            self.__gains_tax = ((self.__gains - 43906) * 0.1208) + 8803.153
        elif self.__gains > 0:
            self.__gains_tax = self.__gains * 0.1003
        else:
            self.__gains_tax = 0
            
    def set_f_div_tax(self):
        if self.__f_div > 220000:
            self.__f_div_tax = ((self.__f_div - 220000) * 0.3934) + 82296.7276
        elif self.__f_div > 210371:
            self.__f_div_tax = ((self.__f_div - 210371) * 0.3719) + 77292.5363
        elif self.__f_div > 150000:
            self.__f_div_tax = ((self.__f_div - 150000) * 0.3167) + 48332.5676
        elif self.__f_div > 147667:
            self.__f_div_tax = ((self.__f_div - 147667) * 0.2952) + 47249.8223
        elif self.__f_div > 95259:
            self.__f_div_tax = ((self.__f_div - 95259) * 0.2538) + 24499.5095
        elif self.__f_div > 91101:
            self.__f_div_tax = ((self.__f_div - 91101) * 0.1779) + 22923.2117
        elif self.__f_div > 87813:
            self.__f_div_tax = ((self.__f_div - 87813) * 0.1224) + 21808.9085
        elif self.__f_div > 77313:
            self.__f_div_tax = ((self.__f_div - 77313) * 0.0892) + 18503.5085
        elif self.__f_div > 47630:
            self.__f_div_tax = ((self.__f_div - 47630) * 0.0639) + 9702.499
        elif self.__f_div > 0:
            self.__f_div_tax = self.__f_div
        else:
            self.__f_div_tax = 0
            
    def set_uf_div_tax(self):
        if self.__uf_div > 220000:
            self.__uf_div_tax = ((self.__uf_div - 220000) * 0.4740) + 82296.7276
        elif self.__uf_div > 210371:
            self.__uf_div_tax = ((self.__uf_div - 210371) * 0.4560) + 77292.5363
        elif self.__uf_div > 150000:
            self.__uf_div_tax = ((self.__uf_div - 150000) * 0.4100) + 48332.5676
        elif self.__uf_div > 147667:
            self.__uf_div_tax = ((self.__uf_div - 147667) * 0.3921) + 47249.8223
        elif self.__uf_div > 95259:
            self.__uf_div_tax = ((self.__uf_div - 95259) * 0.3576) + 24499.5095
        elif self.__uf_div > 91101:
            self.__uf_div_tax = ((self.__uf_div - 91101) * 0.2943) + 22923.2117
        elif self.__uf_div > 87813:
            self.__uf_div_tax = ((self.__uf_div - 87813) * 0.2481) + 21808.9085
        elif self.__uf_div > 77313:
            self.__uf_div_tax = ((self.__uf_div - 77313) * 0.2204) + 18503.5085
        elif self.__uf_div > 47630:
            self.__uf_div_tax = ((self.__uf_div - 47630) * 0.1993) + 9702.499
        elif self.__uf_div > 43906:
            self.__uf_div_tax = ((self.__uf_div - 43906) * 0.1361) + 8803.153
        elif self.__uf_div > 0:
            self.__uf_div_tax = self.__uf_div * 0.089
        else:
            self.__uf_div_tax = 0
    
    def get_gains(self):
        return self.__gains    
        
    def get_gains_tax(self):
        return self.__gains_tax
    
    def get_f_div(self):
        return self.__f_div
    
    def get_uf_div(self):
        return self.__uf_div
    
    def get_f_div_tax(self):
        return self.__f_div_tax
    
    def get_uf_div_tax(self):
        return self.__uf_div_tax
    
class Other(Income):
    def __init__(self, amount):
        Income.__init__(self, amount)    
    
class Taxable_Income(Income):
    def __init__(self, amount):
        Income.__init__(self, amount)
    

        
        