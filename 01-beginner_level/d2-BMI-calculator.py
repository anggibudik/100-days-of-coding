########################################################
#
#    BMI Calculator (by AnggiBK)
#    
#    One Exercise Topic of "Day 2" and "Day 3" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

print("Welcome to BMI Calculator (by AnggiBK). Follow the instructions below to find yours!")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight) / (float(height) ** 2)

# Day 3: adding if statement
if BMI >= 35:
    status = "clinically obese"
elif BMI >= 30 and BMI < 35:
    status = "obese"
elif BMI >= 25 and BMI < 30:
    status = "slightly overweight"
elif BMI >= 18.5 and BMI < 25:
    status = "normal weight"
else:
    status = "underweight"

print(f"Your BMI is {round(BMI,1)}, and you are {status}.")