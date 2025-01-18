def plusMinus(arr):
    # Write your code here
    countp = 0.000000
    countn = 0.000000
    countz = 0.000000

    n = len(arr)
    if n == 0:
        print("\nThe array is empty.  Therefore:")
        print("\npositive ratio = 0.000000\nnegative ratio = 0.000000\nzero ratio = 0.000000")
        return

    for num in arr:
        if num > 0:
            countp += 1
        elif num < 0:
            countn += 1
        else:
            countz += 1

    ratiop = countp / n
    ration = countn / n
    ratioz = countz / n

    print("\nThe ratio of positive integers in the array =",f"{ratiop:.6f}")
    print("The ratio of negative integers in the array =",f"{ration:.6f}")
    print("The ratio of zero instances in the array =",f"{ratioz:.6f}")

arr = [] # for testing an empty array
#arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)


