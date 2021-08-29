# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:52:58 2021

@author: baran

Problem 9 - Special Pythagorean triplet
"""

s = 1000
found = False
n = 1

while (n < s and not found):
    m = n + 1
    while (m < s and not found):
        #Use Euclid's formula to generate Pythagorean triplet a, b, c given n > m
        k = 1
        abc_sum = 0
        while (abc_sum <= s and not found):
            a = k*(m*m - n*n)
            b = k*(2*m*n)
            c = k*(m*m + n*n)
            #The triplet is primitive iff m and n are coprime & not both odd, and all primitive triplets arise that way
            #Looping over k generates nonprimitive triplets
            #There is some redundancy as the coprime&odd condition is not taken into account
            abc_sum = a+b+c
            if (abc_sum == s):
                found = True
            k += 1
        m += 1
    n += 1

print("The triplet (a,b,c) for which a+b+c={s} is ({a},{b},{c}). The product is: {prod}".format(a=a, b=b, c=c, s=s, prod=a*b*c))