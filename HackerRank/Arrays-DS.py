#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

# Write your code here
def reverse_array(a):
    ra = a[::-1]
    return ra


a = [1, 4, 3, 2]
ra = reverse_array(a)
print()
print("Array =", a)
print("Array reversed =", ra)


#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    a_count = int(input().strip())
#
#    a = list(map(int, input().rstrip().split()))
#
#    res = reverse_array(a)
#
#    fptr.write(' '.join(map(str, res)))
#    fptr.write('\n')
#
#    fptr.close()
#
#reverse_array(a)
#
#