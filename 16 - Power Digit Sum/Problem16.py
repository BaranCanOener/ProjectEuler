# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:33:14 2021

@author: Baran

Problem 16 - Power Digit Sum
"""

n=2**1000
ds = 0

while (n > 0):
    ds += n % 10
    n = n // 10

print("The sum of digits of 2 to the power 1000 is: {ds}".format(ds = ds))