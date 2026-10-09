# SI, Period 1, Mapping notes

#We use map for our data.
#The purpose for a map is to alter data and leaves data alone so our orignal data safe
#it will happen with every item on list


def times(number):
    return number *2

numbers = range(1,6)

multiplied_numbers = map(times,numbers)

print(*list(multiplied_numbers))
new_numbers = []
for number in numbers:
    new_numbers.append(number*2)

    print(*new_numbers)

siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

length = list(map(len, siblings))
print(length)

def product(number):
    return