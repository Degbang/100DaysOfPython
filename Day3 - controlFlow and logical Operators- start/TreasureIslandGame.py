#cross_road == 'left':

stream = input("you arrive at a stream, will you wait or swim?\n ").lower
if stream == "swim":
  print("Game Over, swallowed by Jonah's whale")
elif stream == "wait":
  door = input("You arrive at 3 doors, which colour do you choose? \n").lower()

print("  welcome to Treasure Island \nYour mission is to find the treasure.")
cross_road = input(
    " you are at a cross road, where do you go? left or Right\n").lower()
if cross_road == 'left':
    stream = input("you arrive at a stream, will you wait or swim?\n ").lower()
    if stream == "wait":
        door = input(
            "You arrive at 3 doors, which colour do you choose? \n").lower()
        if door == "red":
            print("Game Over,Ayigbe fo colours dier saaa")
        elif door == "blue":
            print(
                "Sorry I dont make the rules, blue balls hurt and its Game Over"
            )
        elif door == "yellow":
            print(
                "Found my favourite colour so you win, cheers to you, send me momo!"
            )
    elif stream == "swim":
        print("Game Over, swallowed by Jonah's whale")
else:
    print("Game Over,Killed by a car")
