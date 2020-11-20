########################################################
#
#    Highest Score in Your Classroom (by AnggiBK)
#    
#    One Exercise Topic of "Day 5" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# The aim of this exercise is to understand the for loop concept.
# So, avoid using max() function for now.

high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")