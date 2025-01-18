import math
import os
import random
import re
import sys

#def AngryProfessor(k, a):
#    result = sum(1 for i in a if i <= 0)
#
#    # Check the condition
#    if result < k:
#        return "YES"
#    else:
#        return "NO"#

def AngryProfessor(k, a):
    result = sum(1 for i in a if i <= 0)
    return "YES" if result < k else "NO"

if __name__ == '__main__':
    # Validate the number of arguments
    print(sys.argv)
    if len(sys.argv) != 3:
        print("Usage: AngryProfessor.py <input_file> <output_file>")
        sys.exit(1)  # Exit with an error code

    # Get input and output file names from command-line arguments
    AngryProfessorinput = sys.argv[1]
    AngryProfessoroutput = sys.argv[2]

    # Open the files
    with open(AngryProfessorinput, 'r') as infile, open(AngryProfessoroutput, 'w') as fptr:
        # Read the number of test cases
        t = int(infile.readline().strip())
        for _ in range(t):
            # Read n and k
            first_multiple_input = infile.readline().strip().split()
            n = int(first_multiple_input[0])
            k = int(first_multiple_input[1])

            # Read the array
            a = list(map(int, infile.readline().strip().split()))

            # Get the result
            result = AngryProfessor(k, a)

            # Write the result to the output file
            fptr.write(result + '\n')



