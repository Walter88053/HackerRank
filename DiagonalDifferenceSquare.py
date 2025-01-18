import math
import os
import random
import re
import sys

def diag_difference(matrix):
    global diff
    n = len(matrix)
    left_to_right_sum = 0
    right_to_left_sum = 0

    for i in range(n):
        left_to_right_sum += matrix[i][i]  # Left to right diagonal
        right_to_left_sum += matrix[i][n-1-i]  # Right to left diagonal
        diff = abs(left_to_right_sum - right_to_left_sum)

    return left_to_right_sum, right_to_left_sum, diff

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

left_sum, right_sum, diff = diag_difference(matrix)
print()
print(f"The sum of left-to-right diagonal elements = {left_sum}")
print(f"The sum of right-to-left diagonal elements = {right_sum}")
print(f"The difference of the diagonals = {diff}")


