# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:49:47 2021

@author: baran

Problem 2 - Project Euler - Sum of even-valued Fibonacci terms whose values is <= 4mio
"""

fib1 = 1
fib2 = 2
sumEven = 2
while (fib2 <= 4000000):
    fib1, fib2 = fib2, fib1 + fib2
    if (fib2 % 2 == 0):
        sumEven += fib2
print("Sum of even-valued Fibonacci terms whose value is below 4mio: {summation}".format(summation = sumEven))
    