# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:05:33 2020

@author: waraujo

Please code a solution to the following problem, tracking your progress by
commiting to GitHub, and submitting your progress after half an hour and after
an hour to Moodle, as well as the final submission. 

A shopping basket contains a number of line items, for example: eggs, rice,
flour; each with a specific quantity. A basket may also have one discount
code, for example eggs20. 

The shop has a standard price list, as well as a set of currently valid
discount codes, each of which confers a certain percentage discount for a list
 of eligible products.

Produce a method which accepts a list of baskets, and outputs their values
from highest to lowest.

github repository: https://github.com/10529473/p4is-ca1
"""

standard_price = {
    'eggs':10,
    'rice':5,
    'flour':20
    }

discount = {
    'eggs20': {
        'eggs':0.8
        },
    '40off': {
        'eggs':0.6,
        'rice':0.6,
        'flour':0.6
        }
    }

class Basket:
    def __init__(self, product_quantity,discount_code=None):
        self.product_quantity = product_quantity
        self.discount_code = discount_code
        
    def getProductValue(self):
        arr = dict(self.product_quantity)

        for k,v in arr.items():
            arr[k] = v * standard_price.get(k) * discount.get(self.discount_code,{}).get(k,1)

        return arr

    def sortProductList(self):
        arr = [[k,v] for k,v in self.getProductValue().items()]
        n = len(arr)
  
        for i in range(n): 
            for j in range(0, n-i-1): 
                if arr[j][1] < arr[j+1][1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
#%%

b1 = Basket({'eggs':2, 'rice':13, 'flour':1})

print(b1.getProductValue())
print(b1.sortProductList())
print('-' * 20)

b1 = Basket({'eggs':2, 'rice':13, 'flour':1},'eggs20')

print(b1.getProductValue())
print(b1.sortProductList())
print('-' * 20)

b3 = Basket({'rice':7, 'flour':4})

print(b3.getProductValue())
print(b3.sortProductList())
print('-' * 20)

b4 = Basket({'eggs':4, 'rice':2, 'flour':6},'40off')

print(b4.getProductValue())
print(b4.sortProductList())
print('-' * 20)