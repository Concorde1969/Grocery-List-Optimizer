# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

grocery = pd.read_csv('C:/Users/Kaleb Neal/Desktop/Grocery Expenses.csv')
nweeks = set(grocery['date'])
frequency = []
n = 0
while n < 103:
    frequency.append(sum(grocery['item'] == grocery['item'][n]))
    n = n + 1
    

k = 0
while k < 103:
    frequency[k] = frequency[k]/len(nweeks)
    k = k + 1

grocery['frequency'] = frequency

grocery_list = grocery[grocery['item'].duplicated()]

grocery[grocery['item'] == 'Sea salt chips']

grocery_list = grocery_list[(grocery['frequency'] == 1) | (grocery['frequency'] == 2/3)]

grocery_list.to_csv('C:/Users/Kaleb Neal/Desktop/Grocery List.csv')
grocery.to_csv('C:/Users/Kaleb Neal/Desktop/Grocery Frequencies.csv')

sum(grocery[grocery['date'] == '1/22/2023']['total cost'])


