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
game = [rock, paper, scissors]

user = int(input("Choose:\n0 = Rock\n1 = Paper\n2 = Scissors\n"))

import random 

if user < 0 or user > 2:
    print("Invalid choice!")
else:
    print("You chose:")
    print(game[user])

    computer = random.randint(0, 2)

    print("Computer chose:")
    print(game[computer])

    if user == computer:
        print("It's a Draw!")
    elif user == 0 and computer == 2:
        print("You Win!")
    elif user == 2 and computer == 0:
        print("You Lose!")
    elif user > computer:
        print("You Win!")
    else:
        print("You Lose!")
