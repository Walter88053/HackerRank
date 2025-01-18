import math
import os
import random
import re
import sys

def beautifulday(i, j, k):
    count = 0
    for num in range(i, j + 1):
        # Reverse the digits of num
        original_num = num
        r = 0
        while num > 0:
            digit = num % 10
            r = r * 10 + digit
            num //= 10

        # Reset num for next iteration
        num = original_num

        # Check if the division results in a whole number
        if abs(original_num - r) % k == 0:
            count += 1

    return count


result = beautifulday(20, 23, 6)
print("\n", result)
