# SI, Period 1, Letter Grade Assignment

# Ask the user for their grade percentage and store it as an integer
percentage = int(input("What is your grade percentage: "))

# Determine the letter grade based on the percentage
if percentage >= 90:
    # 90 or higher earns an A
    letter_grade = "A"
    article = "an"  # Use "an" before vowels
elif percentage >= 80:
    # 80-89 earns a B
    letter_grade = "B"
    article = "a"
elif percentage >= 70:
    # 70-79 earns a C
    letter_grade = "C"
    article = "a"
elif percentage >= 60:
    # 60-69 earns a D
    letter_grade = "D"
    article = "a"
else:
    # Anything below 60 earns an F
    letter_grade = "F"
    article = "an"

# Display the result, including the percentage and letter grade
print(f"Your grade is {percentage}% which is {article} {letter_grade}")