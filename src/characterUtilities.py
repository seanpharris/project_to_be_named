from objects.weapon import weaponList
from objects.action import actionList

# Modifies player stats based on weapon modifiers
# setattr(obj, attr, value) - set the value for the class attribute
# getattr(ob, attr) - return value for class attribute
def modifyStats(character, stat, modifier):
    if len(stat) > 1:
        for i, s in enumerate(stat):
            attrValue = getattr(character, s)
            setattr(character, s, attrValue + (attrValue * modifier[i]))
    else:
        attrValue = getattr(character, stat)
        setattr(character, stat, attrValue + (attrValue * modifier))
    
def updateStatsFromWeapon(character):
    characterStats = ["attack", "defense", "critChance"]
    weaponStats = [
        weaponList[character.weapon].attackModifier,
        weaponList[character.weapon].defenseModifier,
        weaponList[character.weapon].critChance
        ]
    modifyStats(character, characterStats, weaponStats)

# get theatric for move
def getTheatric(weapon, action):
    if action == 'Exhausted' or action == 'Block':
        weapon = 'Shared'
    theatric = actionList[weapon][action].theatric
    return theatric

def printStats(character):
    stats = "%s's Stats: \n" \
            "   Health:  %s  \n"\
            "   Attack:  %s  \n"\
            "   Defense: %s  \n" \
            "   Defense: %s  \n" \
            "   Crit Chance %s \n" % (character.name, 
                                    character.health, 
                                    character.attack, 
                                    character.defense,
                                    character.defense, 
                                    character.critChance)
    print(stats)
