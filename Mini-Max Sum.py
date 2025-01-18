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

    arr.sort()
    minisum = sum(arr[:-1])  # Exclude the last element
    maxsum = sum(arr[1:])  # Exclude the first element
    print()
    print(arr)
    print(minisum, maxsum)  # Print the results

arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)

#if __name__ == '__main__':
#    arr = list(map(int, input().rstrip().split()))
#
#    miniMaxSum(arr)
#