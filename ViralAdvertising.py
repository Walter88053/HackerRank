import math
import os
import random
import re
import sys


#def viraladvertising(n):
#    l = math.floor(n / 2)
#    for i in range(l, n):
#        s = math.floor(l / 2) * 3
#        l = s + l
#        print(l)  # Prints each result in the loop
#
#print()
#viraladvertising(5)


def generate_matrix(n):
    matrix = [
        [1, 5, 2, 2],
        [2, 6, 3, 5],
        [3, 9, 4, 9],
        [4, 12, 6, 15],
        [5, 18, 9, 24]
    ]

    # Generate additional rows if n > 5
    for i in range(6, n + 1):
        new_row = [i]
        new_row.append(matrix[-1][1] + 6)  # 2nd column: previous value + 6
        new_row.append(matrix[-1][2] + 3)  # 3rd column: previous value + 3
        new_row.append(matrix[-1][3] + 11)  # 4th column: previous value + 11
        matrix.append(new_row)

    # Return the value in the 4th column of the nth row
    return matrix[n - 1][3]


# Example usage:
n = int(input("Enter the value of n: "))
result = generate_matrix(n)
print(f"The value in the 4th column of row {n} is: {result}")




