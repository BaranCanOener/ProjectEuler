# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:45:49 2021

@author: Baran

Problem 15 - Lattice paths
"""

"""
Approach: Inductive
On an nxn grid, where each cell (k,l) for k,l = 0,..n-1 contains the number of 
paths from (k+1,l+1) to the bottom right point (ie where (k,l) represents the bottom
right corner of the cell (k,l)), the following holds:
The cell (k,l) is the sum of the adjacent bottom and right cells, see the below example.
(For k > 0 and l > 0. The other cases are trivial, i.e. (k,0) = (0,k) = k + 1)
				   l:
		..	..	5   3
	..	20	10	4   2 
	..	10	6	3   1
	5	4	3	2   0
k:  	3   	2   	1   	0  

This is effectively just rotated Pascal's triangle, and (n-1,n-1) will be 2n choose n.
"""

n = 20
latticePathCounts = [[0 for x in range(n)] for y in range(n)]

for k in range(0,n):
    latticePathCounts[k][0] = k+2;
    latticePathCounts[0][k] = k+2;
    for l in range(1,k+1):
        latticePathCounts[k][l] = latticePathCounts[l][k] = latticePathCounts[k-1][l] + latticePathCounts[k][l-1]

print("The number of paths in an {n}x{n} grid is {c}".format(n = n, c = latticePathCounts[n-1][n-1]))