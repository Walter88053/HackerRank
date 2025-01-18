def MarsExploration(s):
    # Write your code here

    message = "SOS"  # Defines the repeating pattern
    if not s:  # Handles empty list
        return 0
    changes = 0  # Initializes a counter for potential changes
    for i, char in enumerate(s):  # Iterate through the returned test message
        if char != message[i % 3]:  # Use modulo to cycle through "SOS"
            changes += 1  # Total the counted changes
    return changes

s = "SOSSOTSOUSOV"
print()
print("The number of changes to the original message =", MarsExploration(s))


