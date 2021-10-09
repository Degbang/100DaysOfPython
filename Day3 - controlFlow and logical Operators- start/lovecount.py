# Love calculator
print("welcome to the love calculator")
name1 = input("what is your name ")
name2 = input("what is their name ")

lowerCaseName1 = name1.lower()
lowerCaseName2 = name2.lower()

combinedname = lowerCaseName1 + lowerCaseName2

t = combinedname.count("t")
r = combinedname.count("r")
u = combinedname.count("u")
e = combinedname.count("e")

truecount = t + r + u + e

l = combinedname.count("l")
o = combinedname.count("o")
v = combinedname.count("v")
e = combinedname.count("e")

lovecount = l + o + v + e

lovecount =int( str(truecount) + str(lovecount))

if lovecount < 10 or lovecount > 90:
  print(f"your score is {lovecount}, you go together like coke and mentos")
elif lovecount >= 40 and lovecount <+ 50:
  print(f"Your score is {lovecount}, you are alright together")
else:
  print(f"your score is {lovecount}")