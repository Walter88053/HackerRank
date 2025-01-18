#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here

    # Find the maximum value
    max_value = max(candles)

    # Count the instances of the maximum value
    count_max = candles.count(max_value)

    # Count the total of all instances
    total = len(candles)

    # Return the result
    return count_max, total, max_value

# Example usage
candles = [3, 2, 1, 3]
count_max, total, max_value = birthdayCakeCandles(candles)
print()
print("candles = [3, 2, 1, 3]")
print("There are a total of", total, "candles on the cake.")
print("There are",count_max, "candles that are the tallest on the cake and they are",max_value, "units tall.")

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    candles_count = int(input().strip())
#
#    candles = list(map(int, input().rstrip().split()))
#
#    result = birthdayCakeCandles(candles)
#
#    fptr.write(str(result) + '\n')
#
#    fptr.close()
#