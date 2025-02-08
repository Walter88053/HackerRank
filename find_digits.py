def find_digits(n):     #use list comprehension
    digits = [int(digit) for digit in str(n)]  # Extract digits
    count = sum(1 for digit in digits if digit != 0 and n % digit == 0)  # Count divisible digits
    return count

print()
n = 10
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 12
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 111
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 124
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 128
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 1012
print(f"The total number of divisible digits in {n} is {find_digits(n)}")


def find_digits(n):     #use simpler code
    digits = str(n)  # Convert number to string
    count = 0  # Initialize count

    for digit in digits:
        digit_int = int(digit)  # Convert character to integer
        if digit_int != 0 and n % digit_int == 0:  # Check divisibility
            count += 1  # Increment count
    return count


print()
n = 10
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 12
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 111
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 124
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 128
print(f"The total number of divisible digits in {n} is {find_digits(n)}")
n = 1012
print(f"The total number of divisible digits in {n} is {find_digits(n)}")




def sum_divisible_digits(n):
    digits = str(n)
    total_sum = 0

    for digit in digits:
        digit_int = int(digit)
        if digit_int != 0 and n % digit_int == 0:
            total_sum += digit_int
    return total_sum

print()
n = 10
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 12
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 111
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 124
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 128
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 1012
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")



def sum_divisible_digits(n):     #use list comprehension
    digits = [int(digit) for digit in str(n)]  # Extract digits
    total_sum = sum(digit for digit in digits if digit != 0 and n % digit == 0)  # Sum digits
    return total_sum

print()
n = 10
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 12
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 111
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 124
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 128
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")
n = 1012
print(f"The sum of the divisible digits in {n} is {sum_divisible_digits(n)}")



def product_divisible_digits(n):
    digits = str(n)
    total_product = 1

    for digit in digits:
        digit_int = int(digit)
        if digit_int != 0 and n % digit_int == 0:
            total_product *= digit_int
    return total_product

print()
n = 10
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 12
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 111
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 124
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 128
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 1012
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")

from math import prod  # Import prod from math module


def product_divisible_digits(n):
    digits = [int(digit) for digit in str(n)]  # Extract digits
    filtered_digits = [digit for digit in digits if digit != 0 and n % digit == 0]  # Filter valid digits
    return prod(filtered_digits) if filtered_digits else 1  # Avoid error on empty list


# Test cases
print()
n = 10
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 12
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 111
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 124
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 128
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")
n = 1012
print(f"The product of the divisible digits in {n} is {product_divisible_digits(n)}")

