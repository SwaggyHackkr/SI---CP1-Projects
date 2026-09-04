# SI, String Methods

sentence = "The quick brown fox jumps over the lazy dog"

# A function would be something like finding the lenght of something ex: len(sentence)

# A method is when we write what we want something to happen with ex: sentence.lower()

# Methods we have available


fixed = sentence.replace("fox", "wolf")

word = input("What word do you want?: ").strip().lower()
new_word = input("what word should be in the sentence: ")

location = sentence.find(word)
new_sentence = sentence.replace(word,new_word)
print(new_sentence)
print(sentence.find("over"))


firt_name = input("what is your name?: ").strip().title()
last_name = input("What is your lsat name?: ").strip().title()
first_seperated = first_name.split()
last_seperated = last_name.split()
print(seperated)
last_fix = "".join(last_seperated)
full_name = fixed.title() + " " + last_fix.title()
print("Hello " + full_name.title())

print(full_name.isalpha())
print(full_name.isupper())
print(full_name.isnumeric())

print(sentence.split('the'))

print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize())
print(sentence.title())
print(fixed)
# It is all about the outputs above because our user is 50% stupid

# Strip - gets rid of any of the whitespace in the beginning and the end

# Whitespace - is any space within your string that doesn't have a character in it

# Methods do not change the variables, they only work at the location where we put them.

#title is when it capiitilizes the rist letter of the sentence
# lower and upper cases the letters of a sentence or something\

# fix - fixes something

# Split