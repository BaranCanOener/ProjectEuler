# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:44:21 2021

@author: baran

Problem 6 - Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#Gaussian sum formula
def SumIntegersUpTo(n):
    return n*(n+1)//2

def SumSquaresUpTo(n):
    return sum([i * i for i in range(n+1)])

print("The difference between the square of the sum and the sum of the squares of the first one hundred natural numbers is: {n}".format(n=SumIntegersUpTo(100)**2 - SumSquaresUpTo(100)))