import random
import time

class NPC:
    def __init__(self, rosterNumber, name, health, attack, defense, stamina):
        self.rosterNumber = rosterNumber
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.stamina = stamina

# TO DO: Make more NPCs and add to oppenents list
# NPC List
Henchman = NPC(1, "The Henchman", 70, 10, 10, "low")


# Access NPCs with dictionary - "opponents[<name>.name].<Attribute>"
# Example: opponents[Henchman.name].health
opponents = {
    Henchman.rosterNumber: Henchman
    }

# To do:
#  - Remove oppenent from list after fought in getOpponent

# Returns opponent for player to fight randomly
def getOpponent():
    randomize = random.uniform(0, len(opponents)-1)
    randomize += 1 
    print("Your opponent will be..")
    time.sleep(1.5)
    print(opponents[int(randomize)].name + "!")
