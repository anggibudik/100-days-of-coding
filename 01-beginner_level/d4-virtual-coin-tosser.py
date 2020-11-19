########################################################
#
#    Virtual Coin Toss using Random Generator
#    
#    One Exercise Topic of "Day 4" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

if random.randint(0,1) == 1:
    print("Heads")
else:
    print("Tails")