def HackerRankInString(s):
    # Write your code here
    string = "hackerrank"
    current_l = 0

    for char in s:
        if current_l < len(string) and char == string[current_l]:
            current_l += 1
        if current_l == len(string):
            return "YES"
    return "NO"


print()
print(HackerRankInString("hereiamstackerrank"))
print(HackerRankInString("hackerworld"))
print(HackerRankInString("hackerwalter"))
