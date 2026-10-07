# SI, Period 1, Loops Notes

# Iteration,
# Time is a library with prebuilt funcitons that we can use.
#  
import time

siblings = ["Johhny", "Joseph",]

for sibling in siblings:
    print(f"Good Morning {sibling}!")


grades = [100, 87, 53, 45, 78, 78, 72, 88, 3, 94]
average = 0


for grade in grades:
    average += grades
    print(f"{grade} was added")

average = average/len(grades)
print(f"The average grade is {average:.2f}")

for i in range(2,21,2):
    print(i)
    time.sleep(0.5)

for i in range(20, -1, 0):
    print(i)
    time.sleep(0.5)
print("Here is the multiplication table: ")