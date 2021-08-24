# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:29:42 2021

@author: baran

Problem 3 - Project Euler - Largest palindrome made from the product of two 3-digit numbers
"""

def isPalindromic(num):
    numStr = str(num)
    for i in range(len(numStr)//2):
        if numStr[i] != numStr[-i-1]:
            return False
    return True

largestPalindromic = -1
for num1 in range(100,999):
    for num2 in range(100,999):
        prod = num1*num2
        if (isPalindromic(prod) and (prod > largestPalindromic)):
            largestPalindromic = prod
            
print("The largest palindromic number as the product of two 3-digit numbers is: {n}".format(n=largestPalindromic))