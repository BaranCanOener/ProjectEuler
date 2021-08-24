# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:36:28 2021

@author: baran

Problem 1 - Project Euler
"""

multiplier_3 = 1
multiplier_5 = 1
multiple_3 = 3 * multiplier_3
multiple_5 = 5 * multiplier_5
lcm = 15
multiple_lcm = 15 * multiplier_3
threshold = 1000
s = 0
while (multiple_3 < threshold or multiple_5 < threshold):
    if (multiple_3 < threshold):
        s += multiple_3 #Add number that is a multiple of 3
    if (multiple_5 < threshold):
        s += multiple_5 #Add number that is a multiple of 3
    if (multiple_lcm < threshold):
        s -= multiple_lcm #Correct for numbers that were double counted- multiples of 15
    multiplier_3 += 1
    multiplier_5 += 1
    multiple_3 = 3 * multiplier_3
    multiple_5 = 5 * multiplier_5
    multiple_lcm = 15 * multiplier_3
    
print("The sum of multiples of 3 or 5 below 1000 is : {summation}".format(summation = s))