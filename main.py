"""
Be a werewolf. Arrrrwwooooo!
Max Ferguson
"""

from random import *
from day import *
from night import *

def month(day):
    """
    Given a the number of days experienced in the current year it returns a month
    :param day: Current number of days in the year
    :return: str, month
    """
    if 1 >= day <= 31:
        return "January"
    elif 31 >= day <= 59:
        return "February"
    elif 60 >= day <= 90:
        return "March"
    elif 91 >= day <= 120:
        return "April"
    elif 121 >= day <= 151:
        return "May"
    elif 152 >= day <= 181:
        return "June"
    elif 182 >= day <= 212:
        return "July"
    elif 213 >= day <= 243:
        return "August"
    elif 244 >= day <= 273:
        return "September"
    elif 274 >= day <= 304:
        return "October"
    elif 305 >= day <= 334:
        return "November"
    else:
        return "December"

def matchPat(pat, str):
    """
    Searches through a string, str, to find a pattern based on the substring, pat, and
    returns True or False if it is found or not.
    """
    if pat == "":
        return True
    elif str == "":
        return False
    elif pat[0] == str[0]:
        return matchPat(pat[1:], str[1:])
    elif pat[-1] == "*":
        return matchPat(pat[0:-1], str)
    elif pat[0] == "*":
        if pat[1] == "*":
            return matchPat(pat[1:], str)
        elif pat[1] != str[0]:
            return matchPat(pat, str[1:])
        else:
            return matchPat(pat[2:], str[1:])
    else:
        return False

def searchPat(pat, str):
    """
    Searches through a string, str, to find a pattern based on the substring, pat, and
    returns True or False if it is found or not.
    """
    if pat == "":
        return True
    elif str == "":
        return False
    elif pat[0] == str[0]:
        if matchPat(pat, str) is True:
            return True
        else:
            return searchPat(pat[1:], str[1:])
    elif pat[-1] == "*":
        return searchPat(pat[0:-1], str)
    elif pat[0] == "*":
        if pat[1] == "*":
            return searchPat(pat[1:], str)
        elif pat[1] != str[0]:
            return searchPat(pat, str[1:])
        else:
            return searchPat(pat[2:], str[1:])
    else:
        return searchPat(pat, str[1:])

def main():
    # stats will be changeable in final
    dev = randint(1, 100)  # For testing purposes
    seed(dev)  # For testing purposes
    print("Hey Max! This is the seed for the run: ", dev)  # For testing purposes
    stats = {"Strength": randint(4, 9), "Intelligence": randint(3, 9), "Constitution": randint(4, 9),
             "Control": 0, "Hunger": 0, "Karma": 0, "Masquerade": 0}
    stats["Health"] = (stats["Strength"] * stats["Constitution"]) * 10
    howl = {"janHowl": False, "febHowl": False, "marHowl": False, "aprHowl": False, "mayHowl": False, "juneHowl": False,
            "julyHowl": False, "augHowl": False, "septHowl": False, "octHowl": False, "novHowl": False, "decHowl": False}
    print("Welcome to the wonderful world of wolfing! Werewolfing that is. As in being a werewolf, you are one now.")
    while True:
        wonderful = input("I don't know is it wonderful? (1: Yes, 2: No): ")
        if wonderful.isdigit() is True:
            if int(wonderful) == 1:
                input("Great! That puppy that bit you must be a blessing in disguise.")
                break
            elif int(wonderful) == 2:
                input("I'm sorry to here that, I guess you must think that you're a monster now.")
                break
            else:
                print("How dare you think that the programmer didn't put in error checking!")
                stats["Karma"] += 10
        else:
            print("How dare you think that the programmer didn't put in error checking!")
            stats["Karma"] += 10

    input("What puppy you ask? Oh, well that's a long story, well you were walking and you saw this puppy.")
    input("Like any human would you went to pet it, now it's a puppy you probably thought nothing of it "
          "when it bit you.")
    input("But thankfully the puppies 'owner' was there. And tipped us off to your location.")
    input("What? You don't remember any of this? Well... I guess Clayton did knock you over the head pretty hard.")
    input("Which is so great, because he's come so far and this year he may go to regionals!")
    input("Then he can beat those bloody, blood suckers! But, um, ahem... I guess that's not good for you.")
    input("Well look on the bright side the accelerated healing will clear any damage up in no time!")
    input("Anywho, after that Clayton bonked you over the head and now your here, with me...")
    while True:
        prank = input("Where is here? Well we'll get to that. But I just need to know, do you think this ia a prank? "
                      "(1: Yes, 2: No): ")
        if prank.isdigit() is True:
            if int(prank) == 1:
                print("Then let me take off your blindfold...")
                break
            elif int(prank) == 2:
                print("Then I guess this will be a less cool reveal..")
                break
            else:
                print("What? Are you pranking me now?")
                stats["Karma"] += 1
        else:
            print("What? Are you pranking me now?")
            stats["Karma"] += 1
    input("*He takes off your blindfold")
    input("*As your eyes adjust to the light you see a large figure")
    input("*You see that this figure is in fact a large werewolf!")
    input("Yeah, no pranks and no 'Fursuits' either.")
    input("*He turned around allowing you to pet him")
    while True:
        pet = input("*Do you pet him? (1: Yes, 2: No): ")
        if pet.isdigit() is True:
            if int(pet) == 1:
                print("See?")
                break
            else:
                print("What? You don't wanna pat me? Pot me? Wait, what? No it's pet. Pet me please?")
        else:
            print("What? You don't wanna pat me? Pot me? Wait, what? No it's pet. Pet me please?")

    input("Well let's see here I told you why you're here, I made sure that you didn't doubt me...")
    if int(prank) == 1:
        input("...which may or may not be done yet. But whatever..")

    input("Mmmm, how about you introduce yourself and we can continue.")
    while True:
        while True:
            name = input("What's your name? ")
            if name == "":
                print("What?")
            else:
                break

        while True:
            pronouns = input("What are your pronouns? (Format: he/him/his, they/them/their, she,her,hers) ")
            if searchPat("*/*/*", pronouns) is True:
                break
            else:
                print("What?")

        print("So your name is ", name, " and your pronouns are ", pronouns, "?", sep="")
        confirm = input("Right? (1: Yes, 2: No): ")
        if confirm.isdigit() is True:
            if int(confirm) == 1:
                print("Then it's great to meet you, ", name, "!", sep="")
                pronouns = pronouns.split("/")  # Creates a pronouns list!
                break
            elif int(confirm) == 2:
                print("Okay then tell me again.")
            else:
                pass
        else:
            pass

    input("Well, I'm Max, and I use he/him/his pronouns, and now that we got that outta the way...")
    input("I can explain the Masquerade, and it doesn't have anything to do with masks!")
    input("Well, not this time. Well actually it sort of does...")
    input("Think of a Masquerade party as two opposing teams, there are us with masks and then them without masks.")
    input("We must live our lives without letting them know what's under our masks, big muzzles and stuff...")
    input("...")
    input("Because we're wolves.")
    input("But, yeah, that's the gist. Don't let humans see you, you score one for our team, boom, you win the game.")
    input("Otherwise... Well let's not talk about otherwise, you probably wanna go home.")
    input("Let me change back and I'll take you, wait outside by the car.")
    input("*You do what he tells you, you head outside of what was a barn and on to a paved driveway.")
    input("*In that driveway there is what you can only assume is his car.")
    input("*He comes out quickly.")
    input("If you have anymore questions you can come to the next howl, they're held here.")
    input("Come when you turn in 29 days.")
    input("Where is here? Oh, yeah I forgot to tell you...")
    input("*He smiled.")
    input("101 Moon Ave. I know because I named the road...")
    input("Anyway, let's go.")

    dayTotal = 1  # Total days in the game session
    dayinYear = 1  # Total days past in the current game year
    dayofMonth = 1  # Total days past in the current month
    year = 2015

    while True:  # Choose your difficulty
        house = input("Where's home for you? "
                      "(1: Log Cabin(Easy), 2: Suburban House (Normal), 3: Highrise apartment(Hard)): ")
        if house.isdigit() is True:
            if int(house) == 1:
                difficulty = "Easy"
                break
            elif int(house) == 2:
                difficulty = "Normal"
                break
            elif int(house) == 3:
                difficulty = "Hard"
                break
            else:
                print("Where the hell is that?")
        else:
            print("Where the hell is that")

    if difficulty == "Easy":
        input("*You arrive shortly, it didn't take long to get from the barn to your log cabin.")

        while stats["Health"] > 0:
            pass

    elif difficulty == "Normal":
        input("*It takes a bit, but you get there eventually. To your suburban home that your parents left you.")
        input("*Thinking about it made you sad...")
        input("*Sad that they were in the Caribbean and that you were here!")
        input("*But you supposed that it was good that they weren't here now...")
        while True:
            WWYD = input("But for now you it's getting late should you 1: Sleep or 2: Stay up.")

            if WWYD.isdigit() is True:
                if int(WWYD) == 1:
                    if int(wonderful) == 1:  # Sweet dreams
                        input("*Your dreams are filled with roaming through sunkist plains and canopy dimmed forests.")
                        input("*You feel free.")
                        stats["Control"] += 10
                        break

                    elif int(wonderful) == 2:  # Nightmare
                        input("*You see nothing but red, as your newly formed claws tear through person after person.")
                        input("*After the last screams fall into the eternal silence of death")

                        if int(prank) == 1:
                            input("*This can't be real")
                            stats["Hunger"] += 75
                            stats["Control"] -= 5
                            break
                        else:
                            input("I'm a monster...")
                            stats["Karma"] += 1
                            stats["Control"] -= 10
                            stats["Hunger"] += 100
                            break
                elif int(WWYD) == 2:
                    if int(wonderful) == 1:  # Excited for wolfin'
                        input("*You are busting with questions")
                        if int(prank) == 1:
                            input("*You're not so sure if you'll 'wolf out' in 29 days, but it couldn't"
                                  " hurt to go to that place, again.")
                            input("*Even if they're just going to laugh at me.")
                            break
                        else:
                            input("*You can't wait to go to the next howl")
                            break
                    else:  # NO. NO. NO WOLF
                        input("*You can't sleep, you can't stop thinking about the people you could hurt...")
                        if int(prank) == 1:
                            input("*You still hoped that this was a prank")
                        else:
                            input("*You feel like a monster...")
                            stats["Control"] -= 5
                            stats["Karma"] += 1
                else:
                    input("Wait, what should I do?")
                    stats["Karma"] += 5
            else:
                input("Wait, what should I do?")
                stats["Karma"] += 5

        while stats["Health"] > 0:
            print(month(dayinYear), ", ", dayofMonth, ", ", year, sep="") # Prints the current month/day/year
            day()
            night(dayTotal)

            dayTotal += 1
            dayofMonth += 1
            dayinYear += 1

            # Advances year
            if dayinYear > 365:
                dayinYear = 0
                year += 1

            # Resets the days in the months so it prints all pretty.
            if month(dayinYear) == "January" and dayofMonth > 31:
                dayofMonth = 0
            elif month(dayinYear) == "February" and dayofMonth > 28:
                dayofMonth = 0
            elif month(dayinYear) == "March" and dayofMonth > 31:
                dayofMonth = 0
            elif month(dayinYear) == "April" and dayofMonth > 30:
                dayofMonth = 0
            elif month(dayinYear) == "May" and dayofMonth > 31:
                dayofMonth = 0
            elif month(dayinYear) == "June" and dayofMonth > 30:
                dayofMonth = 0
            elif month(dayinYear) == "July" and dayofMonth > 31:
                dayofMonth = 0
            elif month(dayinYear) == "August" and dayofMonth > 31:
                dayofMonth = 0
            elif month(dayinYear) == "September" and dayofMonth > 30:
                dayofMonth = 0
            elif month(dayinYear) == "October" and dayofMonth > 31:
                dayofMonth = 0
            elif month(dayinYear) == "November" and dayofMonth > 30:
                dayofMonth = 0
            elif month(dayinYear) == "December" and dayofMonth > 31:
                dayofMonth = 0
    else:
        while stats["Health"] > 0:
            pass

main()





