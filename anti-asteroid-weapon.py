import sys
import math
import string

for i in range(int(input())):
    ast = {}
    for r in range(int(input())):
        coord = input().split(" ")
        x, y = int(coord[0]), int(coord[1])
        d = math.sqrt(x**2 + y**2)
        ast[d] = [x,y]
    sortk = sorted(ast.keys())
    for r in range(len(sortk)):
        print(f"{ast[sortk[r]][0]} {ast[sortk[r]][1]}")