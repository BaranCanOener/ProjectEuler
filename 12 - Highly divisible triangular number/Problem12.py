# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:24:09 2021

@author: baran

Problem 12 - Highly divisible triangular number
"""

import math

#Gaussian sum formula
def TriangleNumber(n):
    return n*(n+1)//2

#Generates a list of prime factors and multiplicities mi corresponding to the i-th prime using the sieve method
#The number of divisors is equal to (m1+1)*(m2+1).. where m1 = multiplicity of 2, m2 = multiplicity of 3 etc
def NumDivisors(n):
    i = 2
    multiplicities = [0]
    primeFactors = [0]
    index = 0
    while (i <= n):
        while (n % i == 0):
            multiplicities[index] += 1
            n = n // i
        if (multiplicities[index] > 0):
            primeFactors[index] = i
            primeFactors.append(0)
            multiplicities.append(0)
            index+=1
        i += 1
    return math.prod([x+1 for x in multiplicities])

minDivisors = 500
n = 1
while (NumDivisors(TriangleNumber(n)) < minDivisors):
    n += 1

print("The first triangle number with over {d} divisors is Triangle no. {n}: {t}".format(d=minDivisors, n=n, t=TriangleNumber(n)))