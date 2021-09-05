# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:44:06 2021

@author: baran

Problem 13 - Large sum
"""

file = open('numbers.txt','r')
numbers = file.readlines()
for i in range(len(numbers)):
    numbers[i] = numbers[i].rstrip()

res = ''
rem = 0
maxDigits = len(max(numbers, key = len))

#Compute via addition with remainder, digit by digit
for d in range(-1,-maxDigits-1,-1):
    #Add up the digit d of each number into 'rem'
    for n in range(len(numbers)):
        #In case the numbers have unequal numbers of digits
        if (-d <= len(numbers[n])):
            rem+=int(numbers[n][d])
    #The current digit d is the last element of the remainder- hence append to result
    res = str(rem)[-1] + res
    #Keep the remainder digits except the last one
    rem = int(str(rem)[:-1])
res = str(rem) + res

print('The first 10 digits of the sum are: {i}'.format(i=res[:10]))