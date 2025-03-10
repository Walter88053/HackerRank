def staircase(n):
    s = n - 1
    for i in range(1, n + 1):
        print(' ' * s + '#' * i)
        s -= 1


staircase(4)
staircase(6)
staircase(12)
