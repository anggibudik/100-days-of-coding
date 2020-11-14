########################################################
#
#    Love Calculator (by AnggiBK)
#    
#    One Exercise Topic of "Day 3" Lesson
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Note:
#   This code use sum() and map() functions, which haven't taught in this lesson yet.
#   For beginner, it's better to practice like the solution taught in Angela's lesson to get used on the logical step in coding.

name_check = name1.lower() + name2.lower()
true = sum(map(name_check.count, ['t','r','u','e']))
love = sum(map(name_check.count, ['l','o','v','e']))
true_love_digit = int(str(true) + str(love))

if (true_love_digit < 10) and (true_love_digit > 90):
    result = ", you go together like coke and mentos."
elif (true_love_digit >= 40) and (true_love_digit <= 50):
    result = ", you are alright together."
else:
    result = "."

print(f"Your score is {true_love_digit}{result}")