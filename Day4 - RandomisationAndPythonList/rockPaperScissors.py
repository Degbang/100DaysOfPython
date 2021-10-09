import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

plays = [rock,paper,scissors]
userchoice = int(input(f"type 0 for rock, 1 for paper and 2 for scissors\n\n"))
if userchoice < 0 or userchoice > 3:
    print("invalid number, retry")
else:
    userplays = plays[userchoice]
    print(f"you played\n\n {userplays}")

    compchoice = random.randint(0,2)
    compplays = plays[compchoice]

    print(f"computer played\n\n {compplays}")


    if userchoice == compchoice:
        print("try again, draw game")
    elif userchoice == 0 and compchoice == 1:
        print("you lose")
    elif userchoice == 0 and compchoice == 2:
        print("you win")
    elif userchoice == 1 and compchoice == 0:
        print("you win")
    elif userchoice == 1 and compchoice == 2:
        print("you lose")
    elif userchoice == 2 and compchoice == 0:
        print("you lose")
    elif userchoice == 2 and compchoice == 1:
        print("you win")
