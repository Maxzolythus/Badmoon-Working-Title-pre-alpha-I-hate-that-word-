"""
Full of social stuff with the other characters
Up ur social links
dialogue.py
Max Ferguson
"""

from main import *

sLink = {"Steve": 0, "Zara": 0, "Aeyden": 0, "Emil": 0, "Douche": 0, "Diana": 0, "Cheryl": 0, "Hiram": 0, "Eduardo": 0}

def steve(place, sLink, stats, name, pronouns):
    """
    "Dykey" cis Werewolf biker girl named Steve
    This is her character dialogue
    place = where you are talking to Steve
    sLink = your level of friendship with Steve
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    pass

def zara(place, sLink, stats, name, pronouns):
    """
    Bi trans girl with actual invisibility powers named Zara
    Puns ensue
    This is her character dialogue
    :param place: where you are talking to Zara
    :param sLink: your level of friendship with Zara
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    pass

def aeyden(place, sLink, stats, name, pronouns):
    """
    Gay trans man mage, club promoter for club Magicka
    :param place: where you are talking to Aeyden
    :param sLink: your level of friendship with Aeyden
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    pass

def emil(place, sLink, stats, name, pronouns):
    """
    NB, Ace, nerd face. They love comics, and ghost.
    :param place: where you are talking to Emil
    :param sLink: your level of friendship with Emil
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    pass

def doucheBro(place, sLink, stats, name, pronouns):
    """
    Token white cis str8 dude. The most oppressed minority.
    Just a human, that likes you no matter what, he's weird.
    :param place: where you are talking to Chris
    :param sLink: your level of friendly friendship with Chris, this will be pretty large, sorry.
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    if place == "gym":
        if sLink["Douche"] == 0:
            input("*So far your gym day has been going well.")
            if stats["Strength"] < 6:  # Stat based dialogue
                input("*In fact you're surprised considering you almost never go to the gym")
            else:
                input("*It's not surprising due to how often you used to come to the gym.")
            input("*You just needed to finish your last set on the bench...")
            print("???:")
            input("Hey! Need a spot?!")
            input("Are they talking to me?")
            print("Chris:")
            input("Hey dude! I'm Chris...")
            print("Douchebro:")
            input("But everyone calls me by my loving nickname! Douchebro.")
            while True:
                WWYD = input("But as I was saying do you need a spot? (y/n): ")  # Using y/n for dialogue trees
                if WWYD.upper() == "Y":
                    input("Sweet, then let's get to work, bruh.")
                    input("*He helped you with you set, making it go by rather fast.")
                    break
                elif WWYD.upper() == "N":
                    input("Oh, kay, that's cool, I respect that, you can hold your own weight.")
                    if pronouns[0].upper() == "HE":
                        input("No homo.")
                    input("*He watched you complete your set, while he cheered you on.")
                    break
                else:
                    print("Say again, dude?")

            print("Douchebro:")
            input("Hey, bro, that was fun!")
            print("We should do this again some time.")
            sLink["Douche"] += 1
        elif sLink["Douche"] == 1:
            pass


def diana(place, sLink, stats, name, pronouns):
    """
    Werewolf trans girl powerlifter pan, "friends" with douche bro
    Call her Freya, at least at the gym
    :param place: where you are talking to Freya
    :param sLink: your level of friendship with Freya
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    if place == "gym":
        if sLink["Diana"] == -1:  # You can never be friends
            pass  # Add dialogue for assholes that offended Freya
        if sLink["Diana"] == 0:
            input("*You just entered the gym and you already feel tired")
            input("*You begin to move toward the free weights, when bump into someone.")
            input("*You fall back and they extend a hand")
            print("???:")
            input("Are you okay? I'm so sorry.")
            input("*This person is huge, basically an Amazonian.")
            while True:
                WWYD = input("*You realise that you are staring. Say something? (y/n): ")
                if WWYD.upper() == "Y":
                    print("???: ")
                    input("That's good to hear")
                    break
                elif WWYD.upper() == "N":
                    print("???: ")
                    input("Oh shit, I'm sorry, I've been in a rush lately, I guess I should slow down.")
                    break
                else:
                    input("*You spouted gibberish")
                    print("???: ")
                    input("Umm, I hope I didn't make you hit your head too hard.")
                    break
            print("Freya:")
            input("I'm Freya by the way.")
            if WWYD == "Y":
                input("Sorry to bump into you like this.")
                input("*She winks and waves finger guns at you.")
                input("But puns aside...")
            input("Is there anything I can do for you?")
            while True:
                WWYD = input("1: Give me your number, 2: Be my friend, 3: Leave me alone")
                if WWYD.isdigit():
                    WWYD = int(WWYD)
                    if WWYD == 1:
                        input("Wow, that's really forward!")
                        input("*She blushes.")
                        input("But um I suppose it's the least I could do")
                        sLink["Diana"] += 1
                        break
                        #  Should unlock Freya as a phone contact in later versions
                    elif WWYD == 2:
                        pass
                    elif WWYD == 3:
                        pass
                    else:
                        pass
                else:
                    print("*Wait what do I want from her?")

def cheryl(place, sLink, stats, name, pronouns):
    """
    Cis girl next door, probably hetroflexible.
    Half-vampire "daywalker"
    :param place: where you are talking to Cheryl
    :param sLink: your level of friendship with Cheryl
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    pass

def hiram(place, sLink, stats, name, pronouns):
    """
    Agender scientist studying a "secret" project
    "I'm a scientist"
    :param place: where you are talking to Hiram
    :param sLink: your level of friendship with Hiram
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    pass

def eduardo(place, sLink, stats, name, pronouns):
    """
    Cis bear prof. Actual bear, like a werebear.
    :param place: where you are talking to
    :param sLink:
    :param name: str, your name
    :param pronouns: list of your pronouns in the format she/her/hers, he/him/his, ect
    :return: None
    """
    pass
