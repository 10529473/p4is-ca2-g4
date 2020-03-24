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
    def __init_(self, product_list, discont_list):
        self.product_list = product_list
    

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