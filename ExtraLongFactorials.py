import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n-1)
print()
print(extraLongFactorials(25))


#if __name__ == '__main__':
#    n = int(input().strip())
#    result = extraLongFactorials(n)
#   print(result)