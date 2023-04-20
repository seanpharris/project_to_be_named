import random
import time

class NPC:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

# TO DO: Make more NPCs and add to oppenents list
Henchman = NPC("The Henchman", 70, 10, 10)

opponents = [Henchman.name]

def getOpponent():
    randomize = random.uniform(0, len(opponents)-1)
    print("Your opponent will be..")
    time.sleep(1.5)
    print(opponents[int(randomize)] + "!")
