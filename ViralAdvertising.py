import math
import os
import random
import re
import sys


def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for i in range(1, n+1):
        liked = shared//2
        cumulative += liked
        shared = liked * 3#
    return cumulative

print()
print(viralAdvertising(1))
print(viralAdvertising(2))
print(viralAdvertising(3))
print(viralAdvertising(4))
print(viralAdvertising(5))
print(viralAdvertising(6))
#print(viralAdvertising(7))
#print(viralAdvertising(8))
#print(viralAdvertising(9))
#print(viralAdvertising(10))


