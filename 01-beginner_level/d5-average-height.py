########################################################
#
#    Average Student Height from a List (by AnggiBK)
#    
#    One Exercise Topic of "Day 5" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# The aim of this exercise is to understand the for loop concept.
# So, avoid using len() or sum() functions for now.

height_count = 0
student_count = 0

for height in student_heights:
    height_count += height
    student_count += 1

avg_height = round(height_count / student_count)
print(f"The average height of your student is {avg_height}")