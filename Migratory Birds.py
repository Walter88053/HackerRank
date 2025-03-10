def migratorybirds(arr):
    total = {}

    # Count occurrences of each number
    for num in arr:
        if num in total:
            total[num] += 1
        else:
            total[num] = 1

    # Find the maximum count
    max_count = max(total.values())

    # Find the smallest number with the maximum count
    most_frequent = None
    for num, count in total.items():
        if count == max_count:
            if most_frequent is None or num < most_frequent:
                most_frequent = num

    return most_frequent

#    total = {}
#    for num in arr:
#        total[num] = total.get(#num, 0) + 1
#
#    max_count = max(total.values())
#    most_frequent = min(num for num, count in total.items() if count == max_count)
#
#    return most_frequent


print()
arr = [1, 4, 4, 4, 5, 3]
print("The bird type with the least numerical amount among the most frequently occurring ones in", arr, "is", migratorybirds(arr))
arr = [1, 2, 2, 2, 2, 2, 4, 4, 4, 5, 3]
print("The bird type with the least numerical amount among the most frequently occurring ones in", arr, "is", migratorybirds(arr))
arr = [1, 2, 2, 2, 4, 4, 4, 5, 3]
print("The bird type with the least numerical amount among the most frequently occurring ones in", arr, "is", migratorybirds(arr))
arr = [1, 2, 2, 4, 4, 4, 5, 3]
print("The bird type with the least numerical amount among the most frequently occurring ones in", arr, "is", migratorybirds(arr))
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
print("The bird type with the least numerical amount among the most frequently occurring ones in", arr, "is", migratorybirds(arr))
arr = [4, 5]
print("The bird type with the least numerical amount among the most frequently occurring ones in", arr, "is", migratorybirds(arr))


