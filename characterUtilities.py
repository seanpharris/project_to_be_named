from weapons import weaponList
from move import moveList

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

def getTheatric(weapon, move):
    if move == 'Exhausted':
        theatric = moveList['Shared']['Exhausted'].theatric
    elif move == 'Block':
        theatric = moveList['Shared']['Block'].theatric
    else:
        theatric = moveList[weapon][move].theatric
    return theatric
