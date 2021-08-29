# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 19:22:38 2021

@author: baran

Problem 74 - Digit factorial chains - naive method. See Problem74.py for a better variant
"""

def fact(n):
    fact = 1
    i = n
    while (i > 1):
        fact *= i
        i -= 1
    return fact

def SumFactorialDigits(n):
    s = str(n)
    summation = 0
    for d in s:
        summation += fact(int(d))
    return summation

def ProduceChain(n):
    chain = [n]
    m = SumFactorialDigits(n)
    while (not m in chain):
        chain.append(m)
        m = SumFactorialDigits(m)
    return chain

n = 1
nonRepTerms_count = 60
numChains = 0
bound = 1000000

import time
t = time.perf_counter()

while (n < bound):
    chain = ProduceChain(n)
    if (len(chain) == nonRepTerms_count):
        numChains +=1
    n += 1
    
print("The number of chains, with starting no. < {b}, containing exactly {r} non-repeating terms is: {num}. This took {t} seconds".format(num=numChains, b=bound, r=nonRepTerms_count, t = time.perf_counter() - t))