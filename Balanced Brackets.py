def isBalanced(s):
    # Write your code here
    # Stack to track open brackets
    stack = []

    # Dictionary to map closing brackets to corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    # Iterate over each character in the string
    for char in s:
        # If it's a closing bracket
        if char in mapping:
            # Pop the top of the stack if it matches the expected opening bracket
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return 'NO'
        else:
            # It's an opening bracket, so add it to the stack
            stack.append(char)

    # If the stack is empty, all brackets matched properly
    return 'YES' if not stack else 'NO'


print()
print(isBalanced("()"))  # Yes
print(isBalanced("()[]{}"))  # Yes
print(isBalanced("(])"))  # No
print(isBalanced("([)])"))  # No
print(isBalanced("({[]})"))  # Yes


