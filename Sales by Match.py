def sockMerchant(n, ar):
    sock_count = {}
    pairs = 0

    # Count the occurrences of each sock color
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

    # Count the pairs for each sock color
    for count in sock_count.values():
        pairs += count // 2

    return pairs


n = 7  # Specifying "n" does nothing.  HackerRank wanted it specified in the def function.
ar = [1, 2, 1, 2, 1, 3, 2]
result = sockMerchant(n, ar)
print()
print("There are", result, "complete pairs of socks where the color of each sock is a match.")  # This will output the correct number of pairs

ar = [1, 2, 1, 2, 1, 3, 2, 4, 5, 5, 7, 6, 6, 6, 6, 6]
result = sockMerchant(n, ar)
print()
print("There are", result, "complete pairs of socks where the color of each sock is a match.")



def ssmm(ar):
    pairs = 0
    colors = set(ar)  # Get all unique colors in the list

    for color in colors:
        count = ar.count(color)  # Count occurrences of each color
        pairs += count // 2  # Add the number of pairs for that color

    return pairs

ar = [1, 2, 1, 2, 1, 3, 2]
result = ssmm(ar)
print()
print("There are", result, "complete pairs of socks where the color of each sock is a match.")

ar = [1, 2, 1, 2, 1, 3, 2, 4, 5, 5, 7, 6, 6, 6, 6, 6]
result = ssmm(ar)
print()
print("There are", result, "complete pairs of socks where the color of each sock is a match.")


