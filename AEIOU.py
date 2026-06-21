import sys
import math
import string

for i in range(int(input())):
    count = 0
    phrase = list(input())
    for r in range(len(phrase)):
        if phrase[r] in ("a", "e", "i", "o", "u"):
            count+=1
    print(count)