# SI, P1, Random notes

import random 

ducks = random.randint(1,10000)

print(f"There are {ducks} ducks!")


fruits = ["apple", "cherry", "mango", "grapes"]

choice = random.choice(fruits)
print(f"Random fruit:{choice}")

pens = random.randrange(2,100000000000000000000,5)
print(f"I have {pens} pens.")

percent = random.random()

print(f"You have a {percent:.2} grade.")













#Random holds a whole lotta pre built in functions, kinda like a mod, as long i pull in my random library i can use any of the functions
#import lets us access functions that already exist,
#A function is code that has already been built and put together that I can use anywhere.


#randint lets us get a random integer, but to do this we need to give it 2 info, the highest and lowest information possible
#What the code does above tells us the lowest possible number and the second arguement tells us highest number we can get out of it. But we need to set our arguement witha comma
#

#Arguemnts are stuff we give information for it to run, if we don't the code will not run unless we give it the information.
#For a computer ot get a random number it starts out as a number to get a random number, computers do this by getting the number since 1946

#Choice- is when we pick and choose something from the variable and sets it.
#

#randrange- randrange is like randint but instead we clarify what we are trying to find, if we start on a number and we count from 2, we start on 0 counting and adding 2, but if we start on 1 we still do the same but it adds 2 ex: random.randrange(1,10,3)
#

#random.random unlike the others it does not take any arguements, random gives us a float between 1 and 0. Floats in python are that python is notorosiouyly bad at keeping track at floats. Computers are not designed to deal with decimals.pooppoo
#The colon and the number are just for visuals purposes. 
#If we are not highly specific or assigned location, it is very useless