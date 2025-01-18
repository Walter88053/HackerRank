#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here

    Alice = 0
    Bob = 0
    for i in range(0, 3):
        if a[i] > b[i]:
            Alice = Alice + 1
        if a[i] < b[i]:
            Bob = Bob + 1

    return [Alice, Bob]


a = [5, 6, 7]
b = [3, 6, 10]
Alice, Bob = compareTriplets(a, b)

print()
print(f"Alice's ratings are {a}, therefore, her score is {Alice}.")
print(f"Bob's ratings are {b}, therefore, his score is {Bob}.")


#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    a = list(map(int, input().rstrip().split()))
#
#    b = list(map(int, input().rstrip().split()))
#
#    result = compareTriplets(a, b)
#
#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')
#
#    fptr.close()
#