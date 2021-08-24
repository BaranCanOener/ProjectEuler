# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:12:38 2021

@author: baran

Problem 102 - Project Euler - Number of triangles containing the origin
Includes an option to illustrate the triangle containment using matplotlib
"""

class LineSegment:
    
    isVertical = False
    
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x = p1x
        self.p1y = p1y
        self.p2x = p2x
        self.p2y = p2y
        if (p2x == p1x):
            self.isVertical = True
            self.m = 99999
        else:
            self.m = (p2y - p1y) / (p2x - p1x)
        self.b = p1y - p1x * self.m
        
    #Returns True if (px,py) is above or on the line segment
    def IsOnOrBelow(self, px, py):
        if self.isVertical:
            return (px == self.p1x) and ((self.p1y <= py <= self.p2y) or ((self.p2y <= py <= self.p1y)))
        else:
            return ((self.p1x <= px <= self.p2x) or ((self.p2x <= px <= self.p1x))) and (self.m*px + self.b <= py)
        
    #Returns True if (px,py) is below or on the line segment
    def IsOnOrAbove(self, px, py):
        if self.isVertical:
            return (px == self.p1x) and ((self.p1y <= py <= self.p2y) or ((self.p2y <= py <= self.p1y)))
        else:
            return ((self.p1x <= px <= self.p2x) or ((self.p2x <= px <= self.p1x))) and (self.m*px + self.b >= py)
    
class Triangle:
    
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self. ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.line_ab = LineSegment(ax,ay,bx,by)
        self.line_bc = LineSegment(bx,by,cx,cy)
        self.line_ca = LineSegment(cx,cy,ax,ay)
    
    def Contains(self, px, py):
        return ((self.line_ab.IsOnOrAbove(px, py) and self.line_bc.IsOnOrBelow(px, py)))\
                or ((self.line_ab.IsOnOrBelow(px, py) and self.line_bc.IsOnOrAbove(px, py)))\
                or ((self.line_bc.IsOnOrAbove(px, py) and self.line_ca.IsOnOrBelow(px, py)))\
                or ((self.line_bc.IsOnOrBelow(px, py) and self.line_ca.IsOnOrAbove(px, py)))\
                or ((self.line_ca.IsOnOrAbove(px, py) and self.line_ab.IsOnOrBelow(px, py)))\
                or ((self.line_ca.IsOnOrBelow(px, py) and self.line_ab.IsOnOrAbove(px, py)))
                    
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
df = pd.read_csv('p102_triangles.txt', header=None)

draw = False

numContains = 0
for ind in df.index[:]:
    T = Triangle(df[0][ind],df[1][ind],df[2][ind],df[3][ind],df[4][ind],df[5][ind])
    contains = T.Contains(0,0)
    if contains:
        numContains += 1
    if draw:
        X = np.array([[T.ax,T.ay], [T.bx,T.by], [T.cx, T.cy]])
        Y = ['red', 'red', 'red']
        plt.figure()
        plt.scatter(X[:, 0], X[:, 1], s = 1, color = Y[:])
        t1 = plt.Polygon(X[:,:], color=Y[0], fill=None)
        plt.gca().add_patch(t1)
        plt.scatter([0],[0],s = 100, color='black')
        plt.title("Contains origin: " + str(contains))
        plt.show()
print("The number of triangles containing the origin is: {n}".format(n=numContains))