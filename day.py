"""
Defines the main day rng and the subsequent function that is the random action
day.py
Max Ferguson
"""

from random import *
from main import *
from dialouge import *

def day(stats):
    """
    Returns a random day action function based on your decided day action
    :return: Function tht will give a random day action
    """
    # Later versions should read in numbers/booleans to determine this first statement
    input("As the sun rises it marks a new day. What will you do?")
    while True:
        WWYD = input("1: Eat, 2: Go out, 3: Stay Home")
        if WWYD.isdigit() is True:
            if int(WWYD) == 1:  # Eating, later versions will allow you to have a fridge
                while True:
                    confirm = input("Do I want 1: Fast food or 2: Restaurant food: ")  # Currency will be implemented
                    if confirm.isdigit() is True:
                        if int(confirm) == 1:
                            mall(WWYD, stats)
                            break
                        elif int(confirm) == 2:
                            resturant()
                            break
                        else:
                            print("Where?")
                    else:
                        print("Where?")
            elif int(WWYD) == 2:  # Going out! On the toooooown
                while True:
                    confirm = input("Do I want to 1: go to the gym, 2: the mall or 3: the library: ")
                    if confirm.isdigit() is True:
                        if int(confirm) == 1:
                            gym()
                        elif int(confirm) == 2:
                            mall(WWYD,stats)
                        elif int(confirm) == 3:
                            library()
                        else:
                            print("Where?")
                    else:
                        print("Where?")
            elif int(WWYD) == 3:  # Stay home, be a couch potate, or potato, I guess.
                 while True:
                    confirm = input("Do I want use the 1: computer, 2: phone: ")
                    if confirm.isdigit() is True:
                        if int(confirm) == 1:
                            computer()
                        elif int(confirm) == 2:
                            phone()
                        else:
                            print("Where?")
                    else:
                        print("Where?")
            else:
                print("Wait, what am I thinking?")
        else:
            print("Wait, what am I thinking?")

def mall(WWYD,stats):
    """
    Random actions within the mall
    :param WWYD: What Would You Do, or more simply the action the player choose
    :return:
    """
    rand = randint(1,5)  # Will later lead to different favour text and social interactions
    if WWYD == 1:  # Then you're eating
        #if rand == 1:
        input("It may not be the best joint around, but it'll do.")
        stats["Hunger"] -= 25  # Your hunger is lessened for now.
        WWYD = 2
    else:  # Then you're being purely social, look at you! I'm proud.
        if rand == 1:
            input("*You begin to walk through the mall.")
            input("*")

def resturant():
    pass

def gym(sLink, stats):
    rand = randint(1,100)
    incrs = (((randint(1, stats["Strength"])) % 10) + 2) // 2
    if rand < 33:  # Unlucky you, you get to talk to Douchebro aka Chris
        doucheBro("gym", sLink["Douche"])
        stats["Strength"] += incrs
    elif 33 < rand > 66:  # You get to talk to Freya : D
        diana("gym", sLink["Diana"])
        stats["Strength"] += incrs
    else:  # No one wants to talk to you, you lone wolf.
        # Later versions may read in the day and give you your own gym schedule and effect your stats accordingly
        # Also NPCs will have their own schedules
        input("*No one seems to want to talk to you today...")
        input("*Honestly that could be a blessing or a curse.")
        input("*Nevertheless, you had a good gym day.")
        print("You gained",incrs,"strength")
        stats["Strength"] += incrs

def library():
    pass

def phone():
    pass

def computer():
    pass