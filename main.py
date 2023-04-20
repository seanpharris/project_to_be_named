import time
import inspect
import random

from player import Player, getStats, getCombat
from characterTemplate import  CharacterTemplate, templates
from npc import NPC, getOpponent
from combat import combatOptions

def inputCharacterName():
    # get user input
    Player.name = input("What is your characters name? \n")
    print("Welcome " + Player.name + "!")

def inputCharacterType():
    print("What type of character would you like to be? ")
    # templates is a dictionary and the astrisks print out all items in it
    print(*templates, sep=", ")
    # get user input
    chosenType = input()
    # below will try to set the player stats to the template stats 
    # but will fail if the user inputs a non exisiting template type
    try:
        Player.health = templates[chosenType].health
        Player.attack = templates[chosenType].attack
        Player.defense = templates[chosenType].defense
    except KeyError:
        print("Invalid type! Try again.\n")
        # creates 1.5 second delay before prompting type
        time.sleep(1.5)
        inputCharacterType()
    inputWeaponChoice(chosenType)

def inputWeaponChoice(chosenType):
    weaponChoice = input("What kind of weapon would you like to use?\n")
    getCombat(chosenType, weaponChoice)
    try:
        Player.combat = weaponChoice
    except KeyError:
        print("Invalid choice! Try again.\n")
        inputWeaponChoice(chosenType)
        

def inputFight():
    decision = input("Are you ready to fight? y/n")
    if decision == "y":
        time.sleep(1.5)
        getOpponent()
    # Could add another option?
    elif decision == "n":
        print("Oh don't be a pansy!")
        time.sleep(1.5)
        getOpponent()
    else:
        print("Invalid input!")
        time.sleep(1.5)
        inputFight()

if __name__ == "__main__":
    print("Welcome to the Arena!")
    #print(combatOptions["Fist"].weapon)
    #print(CharacterTemplate.weapons)
    inputCharacterName()
    inputCharacterType()
    getStats()
    inputFight()
    
    

    
    
            



