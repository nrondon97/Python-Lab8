#Date: 3/15/2017
#Author: Naylene Rondon
#Filename: fish_guest_NayleneRondon.py
#Purpose: Practice With Dictionaries

import random
#Start

#Variables
def main():
    ocean_stuff = {
        "Fish" : ["Salmon", "Red Snapper", "Tuna", "shark"],
        "plants" : ["Sea Cucumber", "Coral", "plankton"],
        "rocks" : ["white", "Pearl"],
        "crab": ["hermit", "king"]
        }
    print(ocean_stuff)
    player_choice = player()
    secretCreature = getRandomWord(ocean_stuff)
    result(secretCreature, player_choice)
    

def getRandomWord(ocean_creature):
    secretCreature = random.choice(list(ocean_creature.keys()))
    print (secretCreature)
    wordIndex = random.randint(0, len(ocean_creature[secretCreature])-1)
    return [ocean_creature[secretCreature][wordIndex], secretCreature]


def player():
    player_choice = input("What is your choice? ")
    return player_choice

def result(secretCreature, player_choice):
        if secretCreature == player_choice:
                print("Congrats!")
        else:
                print("So, sorry. The word was " + str(secretCreature[0].title())+ ".")
    

main()

#End
