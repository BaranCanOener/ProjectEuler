# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 18:35:45 2021

@author: baran

Problem 10 - Summation of primes (below two million)
"""

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

n = 2000000
print("The sum of primes below {n} is: {s}".format(n=n,s=sum(ErathostenesSieve(n))))