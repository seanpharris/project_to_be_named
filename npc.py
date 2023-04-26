import random
import time

class NPC:
    def __init__(self, rosterNumber, name, health, attack, defense, stamina, weapon):
        self.rosterNumber = int(rosterNumber)
        self.name = str(name)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.stamina = str(stamina)
        self.weapon = str(weapon)

# TO DO: Make more NPCs and add to oppenents list
# NPC List
Henchman = NPC(0, "The Henchman", 70, 10, 10, "Medium", "Fist")


# Access NPCs with dictionary - "opponents[<name>.name].<Attribute>"
# Example: opponents[Henchman.name].health
opponents = {
    Henchman.rosterNumber: Henchman
    }

# To do:
#  - Remove oppenent from list after fought in getOpponent

# Returns opponent for player to fight randomly
def getOpponent():
    print("Your opponent will be..")
    time.sleep(1.5)
    randomize = random.uniform(0, len(opponents)-1)
    opponent = opponents[int(randomize)].name
    print(opponent + "!")
    return opponent
