# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:39:00 2021

@author: baran

Problem 91 - Right triangles with integer coordinates
"""

def IsTriangle(x1, y1, x2, y2):
    return (x1 != 0 or y1 != 0) and (x1 != x2 or y1 != y2) and (x2 != 0 or y2 != 0)

#Test the converse of Pythagoras' theorem. A triangle is right angled if a^2+b^2=c^2
def IsRightTriangle(x1, y1, x2, y2):
    s1 = (x1 - x2)**2 + (y1 - y2)**2
    s2 = x1**2 + y1**2
    s3 = x2**2 + y2**2
    return ((s1 + s2 == s3) or (s1 + s3 == s2) or (s2 + s3 == s1)) 

bound = 50
x1 = 0
n = 0
#Loop over coordinates without double counting
while (x1 <= bound):
    y1 = 0
    while(y1 <= bound):
        x2 = x1
        while (x2 <= bound):
            y2 = 0
            while(y2 <= bound):
                #Condition (y1 >= y2 or x2 > x1) is there to avoid double counting. If y1 >= y2, then y1 and y2 were hit before in opposite roles
                #(due to the order of loops), hence count them only once. If y1<y2, ensure that x2 > x1
                if (y1 >= y2 or x2 > x1) and (IsTriangle(x1,y1,x2,y2) and IsRightTriangle(x1,y1,x2,y2)):
                    n += 1
                y2 += 1
            x2 += 1
        y1 += 1
    x1 += 1

print("The number of right-angled triangles with integer coordinates between 0 and {b} is: {n}".format(n=n, b=bound))