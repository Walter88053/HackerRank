#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here

    n = len(arr)
    d = d % n

    rotated = arr[d:] + arr[:d]
    return rotated


arr = [1, 2, 3, 4, 5]
d = 4
result1 = rotateLeft(d, arr)
result2 = ', '.join(map(str, result1))  # Convert list elements to string and join them with commas
print()
print("array =",arr)
print()
print("result1 =",result1)
print()
print("result2 =",result2)




#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    first_multiple_input = input().rstrip().split()
#
#    n = int(first_multiple_input[0])
#
#    d = int(first_multiple_input[1])
#
#    arr = list(map(int, input().rstrip().split()))
#
#    result = rotateLeft(d, arr)#
#
#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')
#
#    fptr.close()
