def breakingRecords(scores):
    max_score = min_score = scores[0]
    max_count = min_count = 0
    for score in scores:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    return max_count, min_count



scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
max_count, min_count = breakingRecords(scores)
print()
print(max_count, min_count)
print("Maria broke her best scoring record after", max_count, "games", "and broke her worst scoring record after", min_count, "games.")


scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
max_count, min_count = breakingRecords(scores)
print()
print(max_count, min_count)
print("Maria broke her best scoring record after", max_count, "games", "and broke her worst scoring record after", min_count, "games.")

