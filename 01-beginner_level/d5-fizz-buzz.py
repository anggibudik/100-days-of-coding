########################################################
#
#    Fizz Buzz - a Classic Childhood Game (by AnggiBK)
# 
#    "One of the simplest yet the most asked question at interview for programmer!"
#    
#    One Exercise Topic of "Day 5" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

# Rules:
# 1. Each kid say the number from 1 to 100 in round turns
# 2. If the number is divisible by 3, the kid should say "Fizz" instead
# 3. If the number is divisible by 5, the kid should say "Buzz" instead
# 4. If the number is divisible by 3 and 5, the kid should say "FizzBuzz"

for kid in range(1,101):
    if (kid % 3 == 0) and (kid % 5 == 0):
        print("FizzBuzz")
    elif kid % 3 == 0:
        print("Fizz")
    elif kid % 5 == 0:
        print("Buzz")
    else:
        print(kid)