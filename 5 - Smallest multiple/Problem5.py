# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:38:03 2021

@author: baran

Problem 5 - What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

num = 20
notDivisible = True

while (notDivisible):
    num += 1
    #Enough to check 11 to 20
    notDivisible = (num % 20 != 0) or (num % 19 != 0)\
        or (num % 18 != 0) or (num % 17 != 0) or (num % 16 != 0)\
        or (num % 15 != 0) or (num % 14 != 0) or (num % 13 != 0)\
        or (num % 12 != 0) or (num % 11 != 0)
        
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: {n}".format(n=num))