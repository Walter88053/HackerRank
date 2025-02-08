import math


def squares(a, b):
    # Calculate the number of perfect squares between a and b
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1


# Ask the user for input
print()
a = int(input("Enter the first number to define the beginning of the range: "))
b = int(input("Enter the last number to define the end of the range: "))

# Ensure the start of the range is less than or equal to the end
if a > b:
    print("The start of the range must be less than or equal to the end.")
else:
    # Assign the result of squares function to x
    x = squares(a, b)

    # Print the result with proper string formatting
    print()
    print(f"There are {x} square numbers between {a} and {b}.")

