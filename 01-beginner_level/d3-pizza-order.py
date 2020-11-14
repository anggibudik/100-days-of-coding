########################################################
#
#    Pizza Order Bill Calculator
#    
#    One Exercise Topic of "Day 3" Lesson
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
########################################################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Note:
# - The customer won't get any info of final bill if they input the wrong string (i.e. other than those instructed)
# - upper() is used in the statement to prevent a "bug" if the customer input a lowercase letter

price_size = 0
cheese_price = 0

if size.upper() == "L":
  price_size += 25
  if add_pepperoni.upper() == "Y": price_size += 3
elif size.upper() == "M":
  price_size += 20
  if add_pepperoni.upper() == "Y": price_size += 3
elif size._upper() == "S":
  price_size += 15
  if add_pepperoni.upper() == "Y": price_size += 2

if extra_cheese.upper() == "Y":
  cheese_price += 1

print(f"Your final bill is: ${price_size + cheese_price}")