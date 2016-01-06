"""
Defines the main night rng and the subsequent function that is the random action
As well as moon functions and "wolfing out"
night.py
Max Ferguson
"""
from main import *

def moon(day):
    """
    Given the total number of days in the session it works out if their is a full moon or not.
    :param day: Total number of days in the session
    :return: Boolean based on weather the moon is full or not.
    """
    if day % 29 == 0:
        return True
    else:
        return False

def fullMoon(day):
    """
    Based on the month it buffs/debuffs you based on the moon for the month
    :param day: days in the year
    :return: None
    """
    if month(day) == "January":
        print("The Wolf Moon")  # In later version this will change stats
    elif month(day) == "February":
        print("The Snow Moon")
    elif month(day) == "March":
        print("The Worm Moon")
    elif month(day) == "April":
        print("The Pink Moon")
    elif month(day) == "May":
        print("The Flower Moon")
    elif month(day) == "June":
        print("The Strawberry Moon")
    elif month(day) == "July":
        print("The Buck Moon")
    elif month(day) == "August":
        print("The Sturgeon Moon")
    elif month(day) == "September":
        print("The Blood Moon")
    elif month(day) == "October":
        print("The Hunter's Moon")
    elif month(day) == "November":
        print("The Beaver Moon")
    else:
        print("The Cold Moon")


def howlTime(howl):
    """
    Decides if the howls should have normal tutorial dialogue or random events.
    howl = the howl list full of booleans
    :return: None
    """
    if howl["janHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["febHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["marHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["aprHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["mayHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["juneHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["julyHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["augHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["septHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["octHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["novHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass

    if howl["decHowl"] is False:
        # Tutorial Dialogue
        pass
    else:
        # random related event
        pass


def night(day):
    """
    Returns a random night action based on your decided day action
    day = total days in the current session
    :return: Function that will give a random day action
    """
    input("As the sun takes it's daily nap and the moon starts to rise, night approaches. What will you do?")
    while True:
        if moon(day) is False:
            WWYD = input("1: Go clubbing, 2: Stay home, 3: Go to sleep early")
            if WWYD.isdigit() is True:
                if int(WWYD) == 1:
                    pass
                elif int(WWYD) == 2:
                    pass
                elif int(WWYD) == 3:
                    pass
                else:
                    input("Am I tried? Because I have no idea what I'm thinking.")
            else:
                input("Am I tired? Because I have no idea what I'm thinking.")
        else:
            WWYD = input("1: Go clubbing, 2: Stay home, 3: Go to sleep early, 4: Chain yourself up.")
            if WWYD.isdigit() is True:
                if int(WWYD) == 1:
                    pass
                elif int(WWYD) == 2:
                    pass
                elif int(WWYD) == 3:
                    pass
                elif int(WWYD) == 4:
                    pass
                else:
                    input("Am I tried, because I have no idea what I'm thinking")
            else:
                input("Am I tried, because I have no idea what I'm thinking")

def wolfOut():
    pass