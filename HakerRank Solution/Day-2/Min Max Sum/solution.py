#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maxi = max(arr)
    mini = min(arr)
    MaxiSum = sum(arr) - maxi
    MiniSum = sum(arr) - mini
    
    print(MaxiSum, MiniSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)