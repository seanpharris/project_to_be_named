import time
import inspect

from player import Player, getStats
from characterTemplate import templates

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
        print("Invalid type! Try again. \n")
        # creates 1.5 second delay before prompting type
        time.sleep(1.5)
        inputCharacterType()

if __name__ == "__main__":
    print("Welcome to the Fight Area!")
    inputCharacterName()
    inputCharacterType()
    getStats()
    
            



