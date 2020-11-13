'''
    Tip Calculator
    
    Final Goal of "Day 2" Lesson
    100 Days of Code - Udemy Lecture by Dr. Angela Yu
'''

print("Welcome to the tip calculator! (by AnggiBK)")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? (without percent) ")
people = int(input("How many people to split the bill? "))

total_bill = float(bill) * (1 + float(tip)/100)

final_bill = round(total_bill / people,2)

print(f"Each person should pay: ${final_bill}")
