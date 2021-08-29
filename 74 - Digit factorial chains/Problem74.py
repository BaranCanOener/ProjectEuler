# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 19:41:03 2021

@author: baran

Problem 74 - Digit factorial chains - more efficient method: ~4.2s vs ~65s on my computer
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


#n is the number for which the digit factorial chain length should be computed
#This levers the chains for numbers <n that were computed: previousChain[m] contains the length of the chain that starts with m. 
#Now, if the chain for n ever ends up at m, then we just need to add previousChain[m] to the current length to get the resultant chain length
def ProduceChainLength(n, previousChains):
    chain = [n]
    m = SumFactorialDigits(n)
    if (m < len(previousChains)):
        if (previousChains[m] != 0):
            return previousChains[m]+1
    while (not m in chain):
        chain.append(m)
        m = SumFactorialDigits(m)
        if (m < len(previousChains)):
            if (previousChains[m] != 0):
                return previousChains[m]+len(chain)
    return len(chain)

n = 1
nonRepTerms_count = 60
numChains = 0
bound = 1000000
previousChains=[0]*bound

import time
t = time.perf_counter()

while (n < bound):
    chainLen = ProduceChainLength(n, previousChains)
    #Store the just-computed chain length to be used for the next numbers n
    previousChains[n] = chainLen
    if (chainLen == nonRepTerms_count):
        numChains +=1
    n += 1

print("The number of chains, with starting no. < {b}, containing exactly {r} non-repeating terms is: {num}. This took {t} seconds".format(num=numChains, b=bound, r=nonRepTerms_count, t = time.perf_counter() - t))