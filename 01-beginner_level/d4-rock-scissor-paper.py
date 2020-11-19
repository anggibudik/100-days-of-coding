###########################################################
#
#    Rock-Scissor-Paper VS Computer (by AnggiBK)
#    
#    Final Goal of "Day 4" Lesson
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
###########################################################

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

print("Welcome to Rock-Paper-Scissors Game! Are you ready to beat this computer? :D \n")

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
weapon = [rock,paper,scissors]

choice_player = weapon[choose]

# lesson-wise for cpu choice:
choice_cpu = weapon[random.randint(0,2)]

# alternative way for cpu choice:
# choice_cpu = random.choice(weapon)


if choose > 2 or choose < 0:
    print("You chose an invalid number. This computer laughs at you. You lose.")
else:
    if choice_player == choice_cpu:
        result = "It's a draw."
    else:
        if (choice_player == rock and choice_cpu == scissors) or (choice_player == paper and choice_cpu == rock) or (choice_player == scissors and choice_cpu == paper):
            result = "You win!"
        else:
            result = "You lose"
    print(choice_player + "\nComputer chose: \n" + choice_cpu)
    print(result)