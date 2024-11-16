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

choice = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 0 and user_input <= 2:
    print(choice[user_input])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(choice[computer_choice])

if user_input >= 3 or user_input < 0:
    print("Please type a valid number")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_input == 2:
    print("You lose!")
elif computer_choice > user_input:
    print("You lose!")
elif user_input > computer_choice:
    print("You win!")
elif computer_choice == user_input:
    print("It's a draw!")
