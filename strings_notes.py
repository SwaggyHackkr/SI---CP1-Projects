# SI, period 1, String Notes.

#Any characters or symbols that are put together in quotation marks

# Strings are a collection of characters held together by quotation marks

name = "Salesi"

age = "15"

# The computer reads it as a individual character.

# Cancatination, when you put 2 strings together and it puts the second string and it directly to the end of the first string 

print(age + "2")

#It works with any type of string.

print(name + " " + age)

# Cancatination is used for probably gathering information.

# single quotations are preferable but, if you need to add an apostrophe then things change using double quotations would be the best option.

#Escape characters, it tells the computer to ignore the whatever the next character is: \

#\n gives us a new line of printed code

#\t will tab over the line 

#Multiplying a line would help. ex: print(name * 4) generating the name 4 times because it multiplies 

# Cannot divide or substract strings because it will get an error

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)
word = input("what word do you want? ")
print(sentence.find("w"))
print(sentence.[10:15])
print(setntence[start:start+length])
length = len(word)
start = sentence.find(word)

#index is the number associated with each character with each string and list.

#We start counting at 0 when we index also spaces count as characters meaning the computer counts them as a computer

# If they are multiple of letters of the same, when we index it will find the first letter that starts out as the letter we are indexing to find.

# It does not include the end point of after indexing. You can slice a word out without knowing where it is.

# length gives you the lenght of the word.

#Complex datatypes: Holds many pieces of information/data.