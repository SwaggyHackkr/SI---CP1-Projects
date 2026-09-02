#Salesi Ilaoa, Period 1, Average Grade Assignment

def get_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            return grade
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


#Get grades for all 7 class periods
period1 = get_grade("Enter the grade for Period 1: ")
period2 = get_grade("Enter the grade for Period 2: ")
period3 = get_grade("Enter the grade for Period 3: ")
period4 = get_grade("Enter the grade for Period 4: ")
period5 = get_grade("Enter the grade for Period 5: ")
period6 = get_grade("Enter the grade for Period 6: ")
period7 = get_grade("Enter the grade for Period 7: ")

#Calculate the average grade
total = period1 + period2 + period3 + period4 + period5 + period6 + period7
average = total / 7

#Display the average grade
print(f"The average grade for all 7 periods is: {average:.2f}")