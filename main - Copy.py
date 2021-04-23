# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:59:10 2020

@author: Josh
"""

import income
import deductions

def main():
    
    print('I will calculate your tax return (or loss ) for 2019.')
    print()
    print('First, I will calculate your income tax paid for the 2019 year.')
    print()
    print('Please enter the amount of income before tax (or enter 0) that you earned of:')
    
    employment = float(input('Employment income: '))
    comission = float(input('Commisions income: '))
    pension = float(input('Pension income: '))
    benefit = float(input('Benefit income: '))
    investment = float(input('Investment income: '))
    fed_div = float(input('Federally eligible dividend income: '))
    uf_div = float(input('Other dividend income: '))
    other = float(input('Any other forms of income: '))
    
    e = income.Employment(employment)
    e.set_tax_amount()
    emp = e.get_amount()
    taxed_employment = e.get_tax_amount()
    
    c = income.Comission(comission)
    c.set_tax_amount()
    com = c.get_amount()
    taxed_comission = c.get_tax_amount()
    
    p = income.Pension(pension)
    p.set_tax_amount()
    pen = p.get_amount()
    taxed_pension = p.get_tax_amount()
    
    b = income.Benefit(benefit)
    b.set_tax_amount()
    ben = b.get_amount()
    taxed_benefit = b.get_tax_amount()

    i = income.Investment(investment, fed_div, uf_div)
    i.set_gains_tax()
    gains = i.get_gains()
    i.set_f_div_tax()
    fed = i.get_f_div()
    i.set_uf_div_tax()
    ufed = i.get_uf_div()
    gains_tax = i.get_gains_tax()
    f = i.get_f_div_tax()
    uf = i.get_uf_div_tax()
    
    ot = income.Other(other)
    ot.set_tax_amount()
    oth = ot.get_tax_amount()
    taxed_other = ot.get_tax_amount()
    
    total_income = emp + com + pen + ben + gains + fed + ufed + oth
    print()
    print('The total amount of income is $', format(total_income,',.2f'), sep= '')
    
    income_tax_paid = taxed_employment + taxed_comission + taxed_pension + taxed_benefit + gains_tax + f + uf + taxed_other
    print('Income tax paid is $', format(income_tax_paid,',.2f'), sep= '')
    
    confirm = input('Is this the amount you paid? Enter Y or N: ')
    if confirm.upper() == 'Y':
        print()
        print("Now, let's calculate your deductions from 2019")
    elif confirm.upper() == 'N':
        income_tax_paid = float(input('Enter the amount of income tax you paid: '))
    
    print()
    print('Please enter the amount of each of the following taxable income deductions that you earned: ')
    
    rrsp = float(input('RRSP deduction: '))
    if rrsp > total_income*0.18:
        rrsp = float(input('RRSP deduction cannot exceed 18% of income. Please re-enter a valid amount :'))
        
    other = float(input('Other deduction amounts: '))
    
    r = deductions.RRSP(rrsp)
    rd = r.get_amount()
    o = deductions.Other(other)
    od = o.get_amount()
    total_deductions = rd + od
    print()
    print('The total amount deducted from your taxable income is $', format(total_deductions,',.2f'), sep= '')
    
    taxable_income = total_income - total_deductions
    ti = income.Taxable_Income(taxable_income)
    ti.set_tax_amount()
    income_tax = ti.get_tax_amount()
    print()
    print('That would make your taxable income $', format(taxable_income,',.2f'), ' and your new income tax is $', format(income_tax,',.2f'), sep= '')
    
    tax_return = income_tax_paid - income_tax
    print()
    if tax_return >= 0:
        print('Your tax return is $', format(tax_return,',.2f'), sep= '')
    elif tax_return < 0:
        print('For the 2019 tax year, you owe $', format(abs(tax_return),',.2f'), sep= '')
        print('There are various provincial and federal tax-credits you may be eligible for that could reduce the amount you owe.')
    
    print('Thank you.')
    
main()