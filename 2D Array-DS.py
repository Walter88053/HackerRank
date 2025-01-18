#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
import math


#def hourglassSum(arr):
#    # Write your code here
#    result = -math.inf
#    for row in range(4):
#        for col in range(4):
#            HGSum = \
#                arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + \
#                arr[row + 1][col + 1] + \
#                arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
#            result = max((result, HGSum))
#    return result
#
#
#arr = [
#    [1, 1, 1, 0, 0, 0],
#    [0, 1, 0, 0, 0, 0],
#    [1, 1, 1, 0, 0, 0],
#    [0, 0, 2, 4, 4, 0],
#    [0, 0, 0, 2, 0, 0],
#    [0, 0, 1, 2, 4, 0]
#]
#
#result, HGSum = hourglassSum(arr)
#print()
#print(result)
#

def hourglassSum(arr):
    max_sum = float('-inf')
    max_hourglass = None
    max_position = None

    for row in range(4):
        for col in range(4):
            current_sum = (
                arr[row][col] + arr[row][col + 1] + arr[row][col + 2] +
                arr[row + 1][col + 1] +
                arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
            )
            if current_sum > max_sum:
                max_sum = current_sum
                max_hourglass = [
                    [arr[row][col], arr[row][col + 1], arr[row][col + 2]],
                    [arr[row + 1][col + 1]],
                    [arr[row + 2][col], arr[row + 2][col + 1], arr[row + 2][col + 2]]
                ]
                max_position = (row, col)

    return max_sum, max_hourglass, max_position

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

max_sum, max_hourglass, max_position = hourglassSum(arr)

print(f"Maximum sum: {max_sum}")
print(f"Position of top-left cell: {max_position}")
print("Hourglass with maximum sum:")
print(f"{max_hourglass[0][0]} {max_hourglass[0][1]} {max_hourglass[0][2]}")
print(f"  {max_hourglass[1][0]}  ")
print(f"{max_hourglass[2][0]} {max_hourglass[2][1]} {max_hourglass[2][2]}")
#


#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    arr = []
#
#    for _ in range(6):
#        arr.append(list(map(int, input().rstrip().split())))
#
#    result = hourglassSum(arr)
#
#    fptr.write(str(result) + '\n')
#
#    fptr.close()
#
#