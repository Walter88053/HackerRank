import sys
import math


def jumpingOnClouds(c, k):
    n = len(c)  # Ensure n is always an integer
    cur = int(k % n)  # Ensure cur is always an integer
    energy = 100 - 1 - c[cur] * 2

    while cur != 0:
        cur = int((cur + k) % n)  # Ensure cur remains an integer
        energy -= 1 + c[cur] * 2

    return energy

print()
print(jumpingOnClouds([0, 0, 1, 0], 2))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
print()
print(jumpingOnClouds([0, 0, 1, 0], 1))
print(jumpingOnClouds([0, 0, 1, 0], 2))
print(jumpingOnClouds([0, 0, 1, 0], 3))
print(jumpingOnClouds([0, 0, 1, 0], 4))
print(jumpingOnClouds([0, 0, 1, 0], 5))
print(jumpingOnClouds([0, 0, 1, 0], 6))
print(jumpingOnClouds([0, 0, 1, 0], 7))
print(jumpingOnClouds([0, 0, 1, 0], 8))
print(jumpingOnClouds([0, 0, 1, 0], 9))
print(jumpingOnClouds([0, 0, 1, 0], 10))


#if __name__ == "__main__":
#    n, k = input().strip().split(' ')
#    n, k = [int(n), int(k)]
#    c = list(map(int, input().strip().split(' ')))
#    result = jumpingonclouds(c, k)
#    print(result)