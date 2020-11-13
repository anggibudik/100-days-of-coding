'''
    BMI Calculator
    
    One Exercise Topic of "Day 2" Lesson
    100 Days of Code - Udemy Lecture by Dr. Angela Yu
'''
print("Welcome to BMI Calculator (by AnggiBK). Follow the instructions below to find yours!")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight) / (float(height) ** 2)

if BMI > 30:
    status = "obese"
elif BMI > 25 and BMI <= 30:
    status = "overweight"
elif BMI > 18.5 and BMI <= 25:
    status = "normal weight"
else:
    status = "underweight"

print("Your BMI is " + str(round(BMI,1)) + " and you have " + status + ".")


# Although I'm no beginner, some points taught in the beginner lessons might be useful and refreshing.
# Below this point is my personal takeaway note during this lesson (if any):
######
"""
Note 1:
    Programmers [is better to] always start with 0 to avoid confusion,
    because we also work with binary data which starts from 0.
    (true enough! Surely challenging at the beginning for MATLAB or R user like me)
Note 2:
    It turns out python can use underscore in between the thousands as if it's a comma/point separator,
    so human be able to visualize it easily (for God's sake, I just know this thing after all these years!)
Note 3:
    Function is something like a fancy machine in a factory to take potato into chips.
    So if you give the same machine a rock, it won't work and give you an error instead.
    (love this analogical explanation!)
Note 4:
    The order of math operator priority in python follows PEMDAS+LR rule:
        Parentheses (),
        Exponential **,
        Multiplication *
        Division /,
        Addition +
        Substraction -
        Left
        Right
    Note that * / and + - has the same priority level. Also, the priority takes from the most left position on 
    the writen code, hence Left first then Right.
Note 5:
    Double slash in math operator (//) will return the division to integer type automatically. e.g: 8 / 3 -> 8 // 3
Note 6:
    F-string is very handy to convert many data types into string (just like in MATLAB dude. Don't you remember?)
"""