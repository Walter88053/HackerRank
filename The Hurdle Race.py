def hurdleRace(k, height):
    tallest = max(height)

    if tallest > k:
        doses = tallest - k
        return doses
    return 0


k = 4
height = [1, 6, 3, 5, 2]

# Call the hurdleRace function and store the result in the doses variable
doses = hurdleRace(k, height)

# Output the results
print()
print("The height of each hurdle =", height)
print(f"The maximum height the hurdler can jump naturally is {k}.")
print("Therefore, there are", doses, "doses of magic potion that the hurdler needs to clear all of the hurdles.")


k = 7
height = [2, 5, 4, 5, 2]
doses = hurdleRace(k, height)
print()
print("The height of each hurdle =", height)
print(f"The maximum height the hurdler can jump naturally is {k}.")
print("Therefore, there are", doses, "doses of magic potion that the hurdler needs to clear all of the hurdles.")


k = 5
height = [2, 5, 4, 5, 2]
doses = hurdleRace(k, height)
print()
print("The height of each hurdle =", height)
print(f"The maximum height the hurdler can jump naturally is {k}.")
print("Therefore, there are", doses, "doses of magic potion that the hurdler needs to clear all of the hurdles.")


k = 7
height = [1, 6, 89, 5, 2]
doses = hurdleRace(k, height)
print()
print("The height of each hurdle =", height)
print(f"The maximum height the hurdler can jump naturally is {k}.")
print("Therefore, there are", doses, "doses of magic potion that the hurdler needs to clear all of the hurdles.")



