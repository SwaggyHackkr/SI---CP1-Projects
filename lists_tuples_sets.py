# SI, Period 1, Lists Tuples and Sets
#Each item is seperated by a comma,
    #append adds an item
        #insert inserts a item
            #extend extends a list by adding items or things
                #remove removes tihngs from the list by clarifying first
                    #pop pops/delets things from list
#Lists are [], they are ordered, they are mutable, and duplicates
#Tuples, (), are ordered , are immutable, duplicates.
#Both can have duplicates
#Sets uses curley brackets, They are unorded, it is mutable, no duplicates


#Lists
siblings = ["Johhny", "Joseph",]

print(*siblings)
print(f"My older brother is {siblings [1]}")
print(f"The youngest is {siblings[0]}")
siblings.append("Jayshree")
siblings.insert(3, "Lester")
siblings.extend(["Joe", "Israel", "Zoe"])
siblings.remove("Lester")
siblings.pop(0)
print(*siblings)

#tuples
subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah Studies", "US 1", "US 2", "World Civ", "World Geography", "CCA Buisness")
print(subjects[0])
print(*subjects)


#Sets
visited = {"Texas", "Ohio", "Minnesota", "Virginia", "D.C.", "Utah", "California", "Nevada"}

print(*visited)
print(len(visited))
visited.add("Idaho")
print(*visited)
visited.update({"Montanna", "Arizona", "Oklahoma", "New mexico"})
print(*visited)
visited.remove("Arizona")
print(*visited)