# pizza challenge

print("welcome to python pizza deliveries")
size = input("what size of pizza do you want? s m or l ")
add_pepperoni = input("do you want pepperoni? y or n ")
extra_cheese =input("do you want extra cheese? y or n ")
bill = 0
if size == "s":
  bill = 15
  if add_pepperoni == 'y':
     bill += 2
  if extra_cheese == 'y':
      bill += 1
elif size == "m":
  bill += 20
  if add_pepperoni == 'y':
     bill += 3
  if extra_cheese == 'y':
      bill += 1
else:
  bill = 25
  if add_pepperoni == 'y':
    bill += 3
  if extra_cheese == 'y':
      bill += 1
  else:
      bill

print(bill)