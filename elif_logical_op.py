#SI, Period 1, Elif Logical Op notes
    #Conditionals begin with and end with else.
        #we can expand our if statements by adding elif statemet
            #Logic operaters: and or not 
                #and: both must be True
                    #or: one needs to be True
                        #not: it means it isn't true or nothing is true in the statement.
                            #the and means both conditionals must be true both boolean statements must be true
                                #Not means the next statement will be fales
                                    #or just one of the conditions has to be true if both is true then it will also print the only 1 condition.
                                        # We can't use ! when doing a logical operater it is only used for a comparison operator.
                                            #pass is a place holder IT literally does NOTHING. and were in the middle of somehting and we wan't to test things.


age = 17
license: True

if age >= 18:
    print("You are an adult and can vote!")
elif age >= 15 and license:
    print("You can drive! But you are a minor, so go to school!")
elif age >= 15 and not license:
    print("you could drive. . . but ou haven't done the paper work. Also go to school.")
else:
    print("you are too youg to drive.")



win = True
hp = 0

if win or hp < 1:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You lost :O")
else:
    print("The game is still going")