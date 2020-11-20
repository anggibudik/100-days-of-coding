########################################################
#
#    Random Password Generator (by AnggiBK)
#    
#    Final Project of "Day 5" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

# Note: 
# 1. This project has lots of possibilities. Be yourself and be creative!
# 2. Additional function not taught in this lesson: 
#       .join()
#       .shuffle()

import random

# Set of uppercase and lowercase letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Set of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Set of acceptable symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

######################################################
# 1st Solution, my original code: use list method and shuffle it
######################################################

order = []

for char in range(1, nr_letters + 1):
    order.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    order.append(random.choice(symbols))
    
for char in range(1, nr_numbers + 1):
    order.append(random.choice(numbers))

random.shuffle(order)
print("Here is a good password for you:\n" + "".join(order))

# alternatively, based on lesson topic
# password = ""
# for char in order:
#     password += char
# print(f"Here is a password for you: \n{password}")

###########################
# 2nd solution: lesson-wise, step by step
###########################

# Comment out all the codes below to see it

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
    
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_hard = list(password)
# random.shuffle(password_hard)
# print("".join(password_hard))

# However, those hard-level codes above are ineffective and redundant.
# Notice that the password was changed to one type to another to then back to the original type again:
#   string -> list -> string
# It's too much steps to get the same output type, and it's not a good practice in programming.
# 
# Hence, the 1st solution is better.

