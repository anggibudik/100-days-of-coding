##################################################################
#
#    Leap Year Checker (Indonesian: Tahun Kabisat)
#       by AnggiBK
#    
#    One Exercise Topic of "Day 3" Lesson
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
#    Note for leap year rules:
#        It is a leap year if it's evenly divisible by 4
#            **except** it is evenly divisible by 100
#                **unless** it is also evenly divisible by 400
#
##################################################################

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            status = "Leap year"
        else:
            status = "Not leap year"
    else:
        status = "Leap year"
else:
    status = "Not leap year"

print(f"{year} is {status}.")