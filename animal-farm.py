import sys
import math
import string

for i in range(int(input())):
    nums = input().split(" ")
    t, g, h = int(nums[0]), int(nums[1]), int(nums[2])
    sum = t*2 + g*4 + h*4
    print(sum)