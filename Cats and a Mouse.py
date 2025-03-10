def catAndMouse(x, y, z):
    # Check if both cats are at position 0
    if x == 0 and y == 0:
        return "No Cats, Mouse C Wins"

    # Check which cat is closer to the mouse
    if abs(z - x) < abs(z - y):
        return "Cat A Wins"
    if abs(z - y) < abs(z - x):
        return "Cat B Wins"

    # If both cats are equidistant, Mouse C wins
    if abs(z - x) == abs(z - y):
        return "Mouse C Wins"

print()
print("TEST 1 =", catAndMouse(1, 2, 3))
print("TEST 2 =", catAndMouse(1, 3, 2))
print("TEST 3 =", catAndMouse(2, 5, 4))
print("TEST 4 =", catAndMouse(4, 5, 2))
print("TEST 5 =", catAndMouse(2, 12, 7))
print("TEST 6 =", catAndMouse(1, 0, 3))
print("TEST 7 =", catAndMouse(0, 2, 3))
print("TEST 8 =", catAndMouse(0, 0, 3))
print("TEST 9 =", catAndMouse(49, 48, 31))

