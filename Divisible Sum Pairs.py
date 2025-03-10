def divisiblesumpairs(n, k, ar):
    sum = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                sum += 1
    return sum


print()
print(divisiblesumpairs(6, 5, [1, 2, 3, 4, 5, 6]))
print(divisiblesumpairs(6, 3, [1, 3, 2, 6, 1, 2]))


