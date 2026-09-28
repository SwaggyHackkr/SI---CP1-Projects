#Conditional statements are what making decicions on boolean values
    #To start a condition statement we say "if"
        #then we write a boolean statement which will result in a True or False
            #then end the boolean statement with a colon showed below!
                #anytime a line ends with a colon the next line of code must start with a indent if we don't then we get a indentaion error
                    #after we write a if statement we have to write "else:" and it has to line up with "if"
                        #Else statements are for if there are any other possibilites.
                            #Elif statements are for when we need to find or have 2 statements.

grade=0
if grade >=90:
    print("You have an A! Good Job!")
elif grade >= 70:
    print("You are passing!")
else:
    print("You are failing!")