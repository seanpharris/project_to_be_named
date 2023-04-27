class Action:
    def __init__(self, name, attackModifier, defenseModifier, critChance, theatric):
        self.name = str(name)
        self.attackModifier = float(attackModifier)
        self.defenseModifier = float(defenseModifier)
        self.critChance = float(critChance)
        self.theatric = str(theatric)
                                   
# Fist
jab = Action("Jab", 0, 0, 0.01, "POW!")
haymaker = Action("Haymaker", 0, 0, 0.1, "BAM!")

fistActions = { 
    jab.name: jab,
    haymaker.name: haymaker
}

# Axe
verticalSwing = Action("Vertical Swing", 0.15, 0.1, 0.1, "SCHICK!")
horizontalSwing = Action("Horizontal Swing", 0.1, 0.15, 0.1, "SCHINK!")

axeActions = { 
    verticalSwing.name: verticalSwing,
    horizontalSwing.name: horizontalSwing
}

# Sword/dagger
hack = Action("Hack", 0.2, 0.05, 0.2, "SCHWACK!")
stab = Action("Stab", 0.15, 0.1, 0.2, "SHINK!")

bladeActions = {
    hack.name: hack,
    stab.name: stab
}

# Bow
quickshot = Action("Quickshot", 0.2, 0.15, 0.2, "WIZZZ!")
powershot = Action("Powershot", 0.25, 0.05, 0.25, "FLOOP!")

bowActions = {
    quickshot.name: quickshot,
    powershot.name: powershot
}

# Actions shared by all weapons
block = Action("Block", 0, 0.5, 0, "UGHHH!")
exhausted = Action("Exhausted", 0, 0, 0, "Whimpers")

sharedActions = {
    block.name: block,
    exhausted.name: exhausted
}


# Access Actions with dictionary - "actionList[<weapon>][<action>].<Attribute>"
# Example: actionList["Sword"]["Hack"].critChance
actionList = {
    "Fist": fistActions,
    "Axe": axeActions,
    "Sword": bladeActions,
    "Poison Dagger": bladeActions,
    "Bow": bowActions,
    "Shared": sharedActions
}

# Call function with dictionary index
# Example: getActionStats(actionList["Sword"]["Hack"])
def printActionStats(weaponAction):
    stats = "%s stats\n" \
            "Attack modifier: %s\n" \
            "Defense modifier: %s\n" \
            "Crit chance: %s\n" % (weaponAction.name, weaponAction.attackModifier,
                                  weaponAction.defenseModifier, weaponAction.critChance)
    print(stats)

def getActionStats(characterAction, characterWeapon):
    if characterAction == 'Block' or characterAction == 'Exhausted':
        characterWeapon = 'Shared'
    characterActionAttackStat = actionList[characterWeapon][characterAction].attackModifier
    characterActionDefenseStat = actionList[characterWeapon][characterAction].defenseModifier
    characterActionCritChance = actionList[characterWeapon][characterAction].critChance
    return [characterActionAttackStat, characterActionDefenseStat, characterActionCritChance]

def getActionList(weapon):
    actionOptions = {}
    # retrieve weapons for the character's weapon
    allActions = [action for action in actionList[weapon].keys()]
    # then add the action list shared by all weapons
    [allActions.append(action) for action in actionList["Shared"].keys()]
    # build a dictionary action list for the character of the combined actions
    for i, action in enumerate(allActions):
        i += 1
        actionOptions[i]=action
    return actionOptions

# Print all actions for weapon
# print(actionList["Sword"].keys())

