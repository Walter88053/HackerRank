import math
import os
import random
import re
import sys


def diag_difference(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    left_to_right_sum = 0
    right_to_left_sum = 0
    min_dim = min(rows, cols)

    for i in range(min_dim):
        left_to_right_sum += matrix[i][i]  # Left to right diagonal
        right_to_left_sum += matrix[i][cols - 1 - i]  # Right to left diagonal

    diff = abs(left_to_right_sum - right_to_left_sum)
    return left_to_right_sum, right_to_left_sum, diff


# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for idx, matrix in enumerate([matrix1, matrix2], 1):
    left_sum, right_sum, diff = diag_difference(matrix)
    print(f"\nMatrix {idx}:")
    print(f"The sum of the left-to-right diagonal elements = {left_sum}")
    print(f"The sum of the right-to-left diagonal elements = {right_sum}")
    print(f"The difference of the diagonals = {diff}")
