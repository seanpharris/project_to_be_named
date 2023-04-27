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

# Modifies player stats based on weapon modifiers
# setattr(obj, attr, value) - set the value for the class attribute
# getattr(ob, attr) - return value for class attribute
def modifyStats(stat, modifier):
    if len(stat) > 1:
        for i, s in enumerate(stat):
            attrValue = getattr(player, s)
            setattr(player, s, attrValue + (attrValue * modifier[i]))
    else:
        attrValue = getattr(player, stat)
        setattr(player, stat, attrValue + (attrValue * modifier))
    
def updateStatsFromWeapon():
    playerStats = ["attack", "defense", "critChance"]
    weaponStats = [
        weaponList[player.weapon].attackModifier,
        weaponList[player.weapon].defenseModifier,
        weaponList[player.weapon].critChance
        ]
    modifyStats(playerStats, weaponStats)
