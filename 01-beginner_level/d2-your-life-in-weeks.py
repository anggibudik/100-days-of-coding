'''
    "Your Life in Weeks"
    How many days, weeks, or months do you have before turning to 90?
    
    One Exercise Topic of "Day 2" Lesson
    100 Days of Code - Udemy Lecture by Dr. Angela Yu
'''

age = int(input("What is your current age? "))
age_90 = 90 - age

day = age_90 * 365
week = age_90 * 52
month = age_90 * 12

result = f"You have {day} days, {week} weeks, or {month} months left before turning to 90."
print(result)