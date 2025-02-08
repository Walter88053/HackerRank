import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    # Write your code here

    if (m + s - 1) % n != 0:
        return (m + s - 1) % n
    else:
        return n

#    return (m + s - 1) % n if (m + s - 1) % n != 0 else n

print()
print(saveThePrisoner(4, 6, 2))
print(saveThePrisoner(5, 2, 1))
print(saveThePrisoner(5, 2, 2))
print(saveThePrisoner(7, 19, 2))
print(saveThePrisoner(3, 7, 3))

