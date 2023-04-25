from weapons import weaponList

class Player:
    def __init__(self, name, characterClass, health, attack, defense, weapon, stamina):
        self.name = str(name)
        self.characterClass = str(characterClass)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.weapon = str(weapon)
        self.stamina = str(stamina)

#player = Player("", "", 0, 0, 0, "", "")

player = Player("Sean", "Ranger", 100, 20, 20, "Bow", "High")

# Modifies player stats based on weapon modifiers
def modifyStats():
    player.attack = player.attack + (player.attack * weaponList[player.weapon].attackModifier)
    player.defense = player.defense + (player.defense * weaponList[player.weapon].defenseModifier)

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
