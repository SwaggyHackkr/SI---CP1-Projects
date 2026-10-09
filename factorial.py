#SI , Period 1, Factorial Calculator Assignment
#Ms. LaRose, I made pseudocode so I can understand the code more because it is confusing until I practiced and went through my notes and I wrote comments for most of the lines so I don’t forget what each thing does like converting a map into a list.


"""
PSEUDOCODE:
1. Prompt the user: "What number do you want the factorial of: "
2. Read the user's input and convert it to an integer (n).
3. If n is 0, print "0 = 1" and stop.
4. Otherwise, pass math.factorial to map() applied to [n] and convert
   the result to a list, e.g. list(map(math.factorial, [n]))[0].
5. Build a string showing the multiplication: n × (n-1) × ... × 1.
6. Print: [multiplication string] = [factorial result].
"""

import math


def main():
    # Ask the user for a non-negative integer
    n = int(input("What number do you want the factorial of: "))

    # Factorial of 0 is 1 by definition
    if n == 0:
        print("0 = 1")
        return

    # Use map() to apply math.factorial to our number, then convert to a list
    results = list(map(math.factorial, [n]))
    result = results[0]

    # Build the multiplication string, e.g. "5 × 4 × 3 × 2 × 1"
    factors = " × ".join(str(i) for i in range(n, 0, -1))

    # Display the full equation
    print(f"{factors} = {result}")


main()

