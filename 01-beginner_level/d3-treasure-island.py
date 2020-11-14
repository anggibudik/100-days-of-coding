###########################################################
#
#    Treasure Island Game (by AnggiBK)
#    
#    Final Goal of "Day 3" Lesson
#    100 Days of Code - Udemy Lecture by Dr. Angela Yu
#
#    Note:
#       1. This code uses random library in some case, which haven't taught in the lesson
#       2. I normally create functions and more variables for this kind of project,
#           especially since I created the same scenario under some choices.
#           But for now I write them in a very "basic" way to make it easier for any
#           beginner who wants to read this code, if any.
#
###########################################################

print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\
 \_/__________________________________________________________________/
 ''')

print("Welcome to AnggiBK's Treasure Island!")
print("Your mission is to find the treasure based on the map above.") 
choice1 = input('You\'re at a cross road. Where do you want to go? Type "Left", "Right", or "Straight" \n').lower()

long_road = 'It seems quite a long haul and you get exhausted. You look at the map and it seems the treasure is only a halfway left. \nThen you saw a small hut across the road, although it looks quite suspicious. What do you want to do? \nType "hut" to walk to the hut and take a rest there. Type "walk" to continue walking despite of your tireness.\n'
robbered = "You fall asleep in the hut, but then a robber gang snatches your foods and belongings. You can't continue your journey without them. \nGame Over."
recharge = "You successfully recharge your stamina without any problem and continue your journey. Finally, you found the treasure right in front of you! \nYou Win. Congratulations!!"
robbered2 = "You're too tired but continue your journey, only to find out that there's a robber gang in front of you.\n They snatches everything from you. You can't continue your journey anymore. \nGame Over."

if choice1 == "left":
    choice2 = input('You arrive at the entrance of a wild, uncharted jungle. You might encounter some dangerous animals inside. \nWhat do you want to do now? \nType "enter" to walk across the jungle. Type "walk" to walk around using longer route.\n').lower()
    if choice2 == "enter":
        from random import randint
        predator_chance = randint(0,100)
        if predator_chance > 55:
            print("You successfully avoid predator animals and cross the jungle. Then you found the treasure location in front of you. \n You Win. Congratulations!!")
        else:
            print("You encounter an unknown predator animal. You tried to fight but you lose. \nGame Over.")
    elif choice2 == "walk":
        choice3 = input(long_road).lower()
        if choice3 == "hut":
            from random import randint
            robber_chance = randint(0,100)
            if robber_chance > 50:
                print(robbered)
            else:
                print(recharge)
        else:
            print(robbered2)
elif choice1 == "right":
    choice2 = input(long_road).lower()
    if choice2 == "hut":
        from random import randint
        robber_chance = randint(0,100)
        if robber_chance > 50:
            print(robbered)
        else:
            print(recharge)
    else:
        print(robbered2)
elif choice1 == "straight":
    choice2 = input('It seems like you take a wrong route. A volcanic mountain is in front of you. The only way for you is to go forward or swim into the river next to you. \nType "charge" to go towards the volcano. Type "swim" to proceed to the river instead.\n').lower()
    if choice2 == "charge":
        print("You fell into the volcano. Game Over.")
    else:
        choice3 = input(long_road).lower()
        if choice3 == "hut":
            from random import randint
            robber_chance = randint(0,100)
            if robber_chance > 50:
                print(robbered)
            else:
                print(recharge)
        else:
            print(robbered2)        
else:
    print('You choose to do nothing for days, then a tiger approaches you. What will happen?\nGame Over.')