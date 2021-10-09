height = float(input("what is your height "))

bill = 0
if height >= 120:
  print("welcome to the ride")
age = int(input("what is your age "))
if age <= 12:
  bill = 5
  print("you pay 5$")

elif age <= 18:
  bill = 12
  print("you pay 12$")

elif age> 45 and age<55:
  bill = 0
else:
  bill = 20
  print("you pay 20$")
photo = input("do you want a photo taken, press y or n ")
if photo == "y":
  print("you pay an additional 3$")
  bill += 3
  print(f"your total bill is {bill} ")
else:
  print("nigga you short")