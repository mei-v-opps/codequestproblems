import sys
import string
import math

for i in range(int(input())):
    words= input().split("|")
    w1 = words[0]
    w2 = words[1]
    YN = False
    if(w1 != w2):
        if(sorted(w1) == sorted(w2)):
            YN = True
    if(YN):
        print(f"{w1}|{w2} = ANAGRAM")
    else:
        print(f"{w1}|{w2} = NOT AN ANAGRAM")