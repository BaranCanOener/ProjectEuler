# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:41:36 2021

@author: Baran

Problem 17 - Number Letter Counts
"""

def DigitToWord(d):
    if d == 1:
        return "one"
    elif d == 2:
        return "two"
    elif d == 3:
        return "three"
    elif d == 4:
        return "four"
    elif d == 5:
        return "five"
    elif d == 6:
        return "six"
    elif d == 7:
        return "seven"
    elif d == 8:
        return "eight"
    elif d == 9:
        return "nine"
    else:
        return ""
    
def TwoDigitToWord(d):
    if d < 10:
        return DigitToWord(d)
    if d == 10:
        return "ten"
    if d == 11:
        return "eleven"
    elif d == 12:
        return "twelve"
    elif d == 13:
        return "thirteen"
    elif d == 14:
        return "fourteen"
    elif d == 15:
        return "fifteen"
    elif d == 16:
        return "sixteen"
    elif d == 17:
        return "seventeen"
    elif d == 18:
        return "eighteen"
    elif d == 19:
        return "nineteen"
    elif d == 20:
        return "twenty"
    elif d > 20 and d < 30:
        return "twenty-"+DigitToWord(d % 10)
    elif d == 30:
        return "thirty"
    elif d > 30 and d < 40:
        return "thirty-"+DigitToWord(d % 10)
    elif d == 40:
        return "forty"
    elif d > 40 and d < 50:
        return "forty-"+DigitToWord(d % 10)
    elif d == 50:
        return "fifty"
    elif d > 50 and d < 60:
        return "fifty-"+DigitToWord(d % 10)
    elif d == 60:
        return "sixty"
    elif d > 60 and d < 70:
        return "sixty-"+DigitToWord(d % 10)
    elif d == 70:
        return "seventy"
    elif d > 70 and d < 80:
        return "seventy-"+DigitToWord(d % 10)
    elif d == 80:
        return "eighty"
    elif d > 80 and d < 90:
        return "eighty-"+DigitToWord(d % 10)
    elif d == 90:
        return "ninety"
    elif d > 90 and d < 100:
        return "ninety-"+DigitToWord(d % 10)
    
def ThreeDigitToWord(d):
    s = ""
    if d >= 100:
        s += DigitToWord(d // 100) + " hundred "
        if (d % 100 > 0):
            s += "and "
    if ((d % 100) > 0):
        s += TwoDigitToWord(d % 100)
    return s

totalLetters = 0
for i in range (1, 1001, 1):
    s = ""
    num = i
    if num >= 1000:
        s = ThreeDigitToWord(num // 1000) + " thousand "
    num = num % 1000
    s += ThreeDigitToWord(num)
    totalLetters += len(s.replace(" ","").replace("-",""))

print("The number of letters of all numbers between 1 and 1000, inclusive, written out in the English language is: {n}".format(n = totalLetters))