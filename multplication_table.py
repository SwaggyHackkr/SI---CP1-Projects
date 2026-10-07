# SI - Period 1 - Multiplication Table Assignment

# Print the header row (the numbers 1-12 across the top)
# range(1, 13) gives 1 through 12, and :>4 right-aligns each number
# in a space 4 characters wide so the columns line up
print("     " + " ".join(f"{i:>4}" for i in range(1, 13)))

# Print a divider line under the header (60 dashes)
print("     " + "-" * 60)

# This for loop runs once for each row, with "row" being 1, then 2, ... up to 12
for row in range(1, 13):
    # Build the cells for this row:
    # the inner part multiplies the row number by each column number (1-12),
    # right-aligning each answer in a 4-character space, joined with spaces
    cells = " ".join(f"{row * col:>4}" for col in range(1, 13))
    # Print the row number (right-aligned, 3 wide), a vertical bar
    # as a separator, then the cells we just built!
    print(f"{row:>3} |{cells}")