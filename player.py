from weapons import weaponClass

class Player:
    def __init__(self, name, characterClass, health, attack, defense, weapon, stamina):
        self.name = str(name)
        self.characterClass = str(characterClass)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.weapon = str(weapon)
        self.stamina = str(stamina)

player = Player("", "", 0, 0, 0, "", "")

# Modifies player stats based on weapon modifiers
def modifyStats():
    player.attack = player.attack + (player.attack * weaponClass[player.weapon].attackModifier)
    player.defense = player.defense + (player.defense * weaponClass[player.weapon].defenseModifier)

# Display stats to user
def getStats():
    stats = "%s's Stats: \n" \
            "   Health:  %s  \n"\
            "   Attack:  %s  \n"\
            "   Defense: %s  \n" % (player.name, 
                                    player.health, 
                                    player.attack, 
                                    player.defense)
    print(stats)


# To do:
# - Personalize moves each class per weapon
def buildMoveList():
    # Barbarian
    if player.characterClass == "Barbarian":
        if player.weapon == "Fist":
            moveList = ["Jab", "Haymaker", "Block"]
        elif player.weapon == "Axe":
            moveList = ["Vertical Swing", "Horizontal Swing", "Block"]
        elif player.weapon == "Sword":
            moveList = ["Stab", "Hack", "Block"]
    # Assasin
    elif player.characterClass == "Assasin":
        if player.weapon == "Fist":
            moveList = ["Jab", "Haymaker", "Block"]
        elif player.weapon == "Poison Dagger":
            moveList = ["Stab", "Hack", "Block"]
        elif player.weapon == "Bow":
            moveList = ["Quickshot", "Powershot", "Block"]
    # Ranger
    elif player.characterClass == "Ranger":
        if player.weapon == "Fist":
            moveList = ["Jab", "Haymaker", "Block"]
        elif player.weapon == "Sword":
            moveList = ["Stab", "Hack", "Block"]
        elif player.weapon == "Bow":
            moveList = ["Quickshot", "Powershot", "Block"]
    return moveList
