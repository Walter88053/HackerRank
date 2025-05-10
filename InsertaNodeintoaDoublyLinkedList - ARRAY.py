def sorted_insert(arr, x):
    # Find the correct index to insert x
    index = 0
    while index < len(arr) and arr[index] < x:
        index += 1
    arr.insert(index, x)
    return arr


def print_list(arr):
    for item in arr:
        print(item, end=" ")
    print()


if __name__ == "__main__":
    head = [3, 5, 8, 10, 12]
    x = 9
    head = sorted_insert(head, x)
    print()
    print_list(head)
    print(x, "was inserted into this sorted list")
