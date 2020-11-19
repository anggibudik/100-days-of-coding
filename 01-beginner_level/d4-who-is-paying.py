########################################################
#
#    Banker Roulette: Who's Going to Pay for the Dinner Bills? (by AnggiBK)
#    
#    One Exercise Topic of "Day 4" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

random_number = random.randint(0,len(names)-1)
print(f"{names[random_number]} is going to buy the meal today!")

# or use choice()
# random_choice = random.choice(names)
# print(f"{random_choice} is going to buy the meal today!")