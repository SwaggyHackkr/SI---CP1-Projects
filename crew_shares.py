#Salesi Ilaoa, Period 1, Crew shares assignment.

#Pseudocode of the crew shares 

#GET number of pirates including Yondu and Quill
#GET random number between 500 and 5000
#SET total units TO random number
#SET other crew TO number of pirates minus 2
#SET sent away units TO other crew Mulitiplied by 3
#SET remaining units TO total units - sent away units

#SET Yondu share TO ROUND remaining units  0.13, 2
#Yondu share is rounding the remaining units to 0,13
#UPDATE remaining units TO remaining units minus Yondu share

#SET Peter share TO ROUND remaining units multiplied 0.11, 2
#UPDATE remaining units TO remaining units minus Peter share

#SET crew share TO ROUND remaining units divided by number of pirates, 2

#OUTPUT "Units found: " total units
#OUTPUT "Yondu's share: " Yondu share
#OUTPUT "Peter's share: " Peter share
#OUTPUT "Crew's share: " crew share
#END

import random

while True:
    try:
        pirates = int(input("How many pirates besides yondu and quill: ")) 
    except ValueError:
        print("Enter a valid number!")
    else:
        break

total_units = random.randint(500, 5000)

other_crew = pirates + 2

yondu_share = round(total_units * 0.13, 2)
remaining_units = total_units - yondu_share

peter_share = round(remaining_units * 0.11, 2)
remaining_units = remaining_units - peter_share

crew_share = round(remaining_units / other_crew, 2)

print(f"Units found: {total_units}")
print(f"Yondu's share: {yondu_share + crew_share:.2f}")
print(f"Peter's share: {peter_share+crew_share:.2f}")
print(f"Crew's share: {crew_share:.2f}")