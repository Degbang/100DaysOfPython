import random
names_string = input("give me everybody's name, separated by a comma\n")

name = names_string.split(", ")
person = random.choice(name)
print(f"{person} is going to pay today")

# or

Numberofitems = len(name)
random_numberTobeAssignedToNames = random.randint(0,Numberofitems - 1)
print(name[random_numberTobeAssignedToNames])