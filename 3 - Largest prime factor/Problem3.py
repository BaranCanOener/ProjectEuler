# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:55:23 2021

@author: baran

Problem 3 - Project Euler - Largest prime factor
"""

num = 600851475143
numTmp = num
for divisor in range (2, numTmp//2, 1):
    while ((numTmp % divisor) == 0):
        numTmp = numTmp // divisor
    if (numTmp == 1):
        break
        
print("The largest prime factor of {number} is: {divisor}".format(number = num, divisor = divisor))