# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:57:35 2023

@author: baran

Problem 21 - Amicable Numbers
"""

def D(n):
    if (n < 2):
        return 0 
    divisorSum = 1
    for i in range(2, int(n**0.5)):
        divisorSum = divisorSum + i + n//i if (n % i == 0) else divisorSum
    return divisorSum

#d[n] = sum of proper divisors of n
d = []

#Sum of amicable numbers under 'limit' are sought
limit = 10000

sumOfAmicableNumbers = 0

for i in range(0, limit):
    divisorSum = D(i)
    d.append(divisorSum)
    if (divisorSum < i) and (d[divisorSum] == i):
        sumOfAmicableNumbers = sumOfAmicableNumbers + i + divisorSum
    
        
print("Sum of amicable numbers less than {l} is: {n}".format(l=limit,n=sumOfAmicableNumbers))