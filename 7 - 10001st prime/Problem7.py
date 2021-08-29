# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:52:02 2021

@author: baran

Problem 7 - 10001st prime
"""

import math

#returns a list of all prime numbers below the integer bound
def ErathostenesSieve(bound):
    n = 2
    primes = []
    sieve = [True] * bound
    sieve[0] = sieve[1] = False
    while (n < bound):
        if (sieve[n]):
            #if sieve[n] = True as we loop over n, we know that it can't be a multiple of a previous number, hence it is a prime
            primes.append(n)
            i = 2
            while (i * n < bound):
                #All multiples of n cannot be primes => Sieving step
                sieve[i*n] = False
                i+=1
        n+=1
    return primes

primeIndex = 10001
#Prime number theorem - the n-th prime is asymptotically equal to n*ln(n)
bound = int(primeIndex*math.log2((primeIndex)))
print("The {n}th prime number is: {p}".format(n=primeIndex, p=ErathostenesSieve(bound)[primeIndex]))