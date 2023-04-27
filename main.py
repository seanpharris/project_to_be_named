import time

from player import player, printStats
from characterTemplate import templates, getClassWeapons
from npc import getOpponent
from combat import roundPreparation, roundFight
from characterUtilities import updateStatsFromWeapon

def inputCharacterName():
    # get user input
    player.name = input("What is your characters name? \n")
    print("Welcome " + player.name + "!\n")

def inputCharacterType():
    print("What type of character would you like to be?\n")
    # templates is a dictionary and the astrisks print out all items in it
    print(*templates, sep=", ")
    # get user input
    chosenClass = input()
    # below will try to set the player stats to the template stats 
    # but will fail if the user inputs a non exisiting template type
    try:
        player.characterClass = templates[chosenClass].type
        player.health = templates[chosenClass].health
        player.attack = templates[chosenClass].attack
        player.defense = templates[chosenClass].defense
        player.stamina = templates[chosenClass].stamina
    except KeyError:
        print("Invalid type! Try again.\n")
        # creates 1.5 second delay before prompting type
        time.sleep(1.5)
        inputCharacterType()
    inputWeaponChoice()

def inputWeaponChoice():
    availableWeapons = getClassWeapons()
    print("What weapon would you like to use?\n" \
          "Type the number next to the weapon\n")
    for i, weapon in enumerate(availableWeapons):
        print(i + 1, weapon)
    weaponChoice = int(input())
    weaponChoice -= 1
    try:
        player.weapon = availableWeapons[weaponChoice]
    except KeyError:
        print("Invalid choice! Try again.\n")
        inputWeaponChoice()
    print('Your weapon will be the %s!' % (player.weapon))
        

def inputFight():
    decision = input("Are you ready to fight? (y/n)\n")
    if decision == "y":
        time.sleep(1.5)
    # Could add another option?
    elif decision == "n":
        print("Oh don't be a pansy!\n")
        time.sleep(1.5)
    else:
        print("Invalid input!\n")
        time.sleep(1.5)
        inputFight()

if __name__ == "__main__":
    print("Welcome to the Arena!\n")
    # returns character name by user input accessed with player.name
    inputCharacterName()
    # returns character name by user input accessed with player.characterClass
    inputCharacterType()
    updateStatsFromWeapon(player)
    printStats()
    inputFight()
    opponent = getOpponent()
    chosenMoves = roundPreparation()
    roundFight(opponent, chosenMoves)
    

    
    
            



