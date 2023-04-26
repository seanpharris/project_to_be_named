from weapons import weaponList

class Player:
    def __init__(self, name, characterClass, health, attack, defense, critChance, weapon, stamina):
        self.name = str(name)
        self.characterClass = str(characterClass)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.critChance = float(critChance)
        self.weapon = str(weapon)
        self.stamina = str(stamina)

#player = Player("", "", 0, 0, 0, "", "")

### FOR DEVELOPMENT --- Remove when done
player = Player("Sean", "Ranger", 100, 20, 20, 0, "Bow", "High")

playerStats = ["attack", "defense", "critChance"]

# Modifies player stats based on weapon modifiers
def modifyStats(stat, modifier):
    if len(stat) > 1:
        for i, s in enumerate(stat):
            attrValue = getattr(player, s)
            setattr(player, s, attrValue + (attrValue * modifier[i]))
    else:
        attrValue = getattr(player, stat)
        setattr(player, stat, attrValue + (attrValue * modifier))
    
def updateStatsFromWeapon():
    weaponStats = [
        weaponList[player.weapon].attackModifier,
        weaponList[player.weapon].defenseModifier,
        weaponList[player.weapon].critChance
        ]
    modifyStats(playerStats, weaponStats)

updateStatsFromWeapon()

#modifyStats("attack", weaponList[player.weapon].attackModifier)

print(player.attack)

#updateStatsFromWeapon()

# Display stats to user
def printStats():
    stats = "%s's Stats: \n" \
            "   Health:  %s  \n"\
            "   Attack:  %s  \n"\
            "   Defense: %s  \n" \
            "   Crit Chance %s \n" % (player.name, 
                                    player.health, 
                                    player.attack, 
                                    player.defense, 
                                    player.critChance)
    print(stats)
