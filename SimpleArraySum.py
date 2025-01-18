def SimpleArraySum():
    total = 0
    ar = [1, 3, 5, 7, 9, 11, 13]
    count = len(ar)
    for num in ar:
        total += num
    return count, total

count, total = SimpleArraySum()


print()
print("The number of elements in the array:", count)
print("The sum of all the elements in the array =", total)


