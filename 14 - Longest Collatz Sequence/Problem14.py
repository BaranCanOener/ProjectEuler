# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:33:55 2021

@author: baran

Problem 14 - Longest Collatz Sequence - Uses caching of previous results (speedup by a factor of 20 vs. without caching)
Caching may potentially be improved by storing sequence lengths of numbers greater than bound
"""

bound = 1000000
collatzLen = [-1]*(bound+1)

import time
t = time.perf_counter()

for n in range(1,bound+1):
    num = n
    clen = 1
    while True:
        if (num % 2 == 0):
            num = num // 2
        else:
            num = 3*num + 1
        clen+=1
        if (num == 1):
            #Cache result
            collatzLen[n] = clen
            #Move on to next number
            break
        
        if (num < bound) and (collatzLen[num] != -1):
            #Previously cached result can be used
            clen += collatzLen[num] - 1
            if (num < bound):
                collatzLen[n] = clen
            #Move on to next number
            break

timeTaken = time.perf_counter() - t

print('The starting number producing the longest chain is: {i}, at a length of {l} (computed in {s} seconds)'.format(i = collatzLen.index(max(collatzLen)), l = max(collatzLen),s=timeTaken))