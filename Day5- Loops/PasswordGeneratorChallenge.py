#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# password =""
# for letter in range(0,nr_letters):
#   letterschosen =  random.choice(letters)
#   password += letterschosen
# print(password)
#
# for number in range(0,nr_numbers ):
#     numberchosen = random.choice(numbers)
#     password += numberchosen
# print(password)
#
# for number in range(0, nr_symbols):
#     symbolchosen = random.choice(symbols)
#     password += symbolchosen
# print(password)


#hard_level
passwordlist = []
for letter in range(0,nr_letters):
    letterschosen =  random.choice(letters)
    passwordlist += letterschosen


for number in range(0,nr_numbers ):
    numberchosen = random.choice(numbers)
    passwordlist += numberchosen


for number in range(0, nr_symbols):
    symbolchosen = random.choice(symbols)
    passwordlist += symbolchosen

random.shuffle(passwordlist)

pswd = ""
for char in passwordlist:
    pswd += char

print(pswd)