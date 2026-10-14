#SI, Peirod1, While Loops
#Else will only happen when our loop ends naturally if we break the code before else then it won't run
import random
import time

goose = random.randint(1,100)
duck = 1

while goose > duck:
    print("duck. . .")
    time.sleep(0.1)
    duck += 1
    if duck == 15:
        print("Game over")
        break
else:
    print("GOOSE!")

number = random.randint(1,101)

while True:
    while True:
