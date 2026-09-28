#SI, P1, find grade assignment

def get_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            return grade
        except ValueError:
            print("Invalid input. Please enter a valid number.")



#Inputs below

grade1 = input("Enter your grade for your first period: ")
grade2 = input("Enter your grade for your second period: ")
grade3 = input("Enter your grade for your third period: ")
grade4 = input("Enter your grade for your fourth period: ")
grade5 = input("Enter your grade for your fifth period:")
grade6 = input("Enter your grade for your 6th period: ")

overallgrade = grade1 + grade2 + grade3 + grade4 + grade5 + grade6 
total = overallgrade / 6


if overallgrade >= 90:
    print("You are passing!")
elif overallgrade >=80:
    print("You are barely passing!")
else:
    print("You are failing")

print(f"Your overall grade is {total:.2f}")