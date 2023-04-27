import random
import time

class NPC:
    def __init__(self, alive, rosterNumber, name, health, attack, defense, critChance, stamina, weapon):
        self.alive = bool(alive)
        self.rosterNumber = int(rosterNumber)
        self.name = str(name)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.critChance = float(critChance)
        self.stamina = str(stamina)
        self.weapon = str(weapon)

# TO DO: Make more NPCs and add to oppenents list
# NPC List
Henchman = NPC(True, 0, "The Henchman", 70, 10, 10, 0, "Medium", "Fist")


# Access NPCs with dictionary - "opponents[<name>.name].<Attribute>"
# Example: opponents[Henchman.name].health
opponents = {
    Henchman.rosterNumber : Henchman
    }

# To do:
#  - Remove oppenent from list after fought in getOpponent

# Returns opponent for player to fight randomly
def getOpponent():
    print("Your opponent will be..")
    time.sleep(1.5)
    randomize = random.uniform(0, len(opponents)-1)
    opponent = opponents[int(randomize)].name
    rosterNumber = opponents[int(randomize)].rosterNumber
    print(opponent + "!")
    return opponent, rosterNumber

def getRandomMove(list):
    randomize = int(random.uniform(0, len(list)))
    randomize += 1
    randomMove = list[randomize]
    return randomMove

def getNPCRoundMoves(actionOptions, actionCount):
    npcRoundMoves = []
    for i in range(actionCount):
        randomMove = getRandomMove(actionOptions)
        while randomMove == "Exhausted":
            randomMove = getRandomMove(actionOptions)
        npcRoundMoves.append(randomMove)
    return npcRoundMoves
