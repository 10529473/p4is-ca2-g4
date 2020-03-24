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

class Basket:
    def __init__(self, product_price_arr, discount_arr):
        self.product_price_arr = product_price_arr
        
    def getProductList(self,discount_code=None):
        arr = list(self.product_price_arr)
        
        if discount_code is not None:
            for k,v in arr:
                arr[k]=v*discount_arr['egg20'][k]
            
        return arr

    def sortProductList(self):
        arr = list(self.product_price_arr)
        
        n = len(arr) 
  
        for i in range(n): 
            for j in range(0, n-i-1): 
                if arr[j]['price'] < arr[j+1]['price'] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr

"""
[
    {
        desc: egg,
        price: 10
        discont:
            {
                eggs20: 0.8
                eggs30: 0.7
            }
    },
    {
        desc: rice,
        price: 10
        discont:
            {
                eggs20: 0.8
            }
    }   
]
 """
 
#%%
b1 = Basket([{'desc':'egg','price':10},{'desc':'rice','price':5},{'desc':'flour','price':20}])
test = b1.getProductList()



