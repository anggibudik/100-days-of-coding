########################################################
#
#    Roller Coaster Checker and Ticket Price
#    
#    This code is the summary of "Day 3" Lessons
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
ticket = 0

if height > 120:
  print("You can ride the rollercoaster! Enjoy!")
  age = int(input("What is your age? "))
  if age < 12 and age > 0:
    ticket += 5
    ticket_print = f"Child tickets are ${ticket}"
  elif age >= 12 and age <= 18:
    ticket += 7
    ticket_print = f"Youth tickets are ${ticket}"
  elif age > 18:
    if not (age >= 45 and age <= 55):
        ticket += 12
        ticket_print = f"Adult tickets are ${ticket}"
    else:
        ticket_print = f"You are under midlife crisis category, so your ride ticket is free!"

  print(ticket_print)

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo.upper() == "Y":
    ticket += 3
  
  print(f"Your final bill is ${ticket}")

else:
  print("You cannot ride the rollercoaster, sorry.")