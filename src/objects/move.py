class Move:
    def __init__(self, name, attackModifier, defenseModifier, critChance, theatric):
        self.name = str(name)
        self.attackModifier = float(attackModifier)
        self.defenseModifier = float(defenseModifier)
        self.critChance = float(critChance)
        self.theatric = str(theatric)
                                   
# Fist
jab = Move("Jab", 0, 0, 0.01, "POW!")
haymaker = Move("Haymaker", 0, 0, 0.1, "BAM!")

fistMoves = { 
    jab.name: jab,
    haymaker.name: haymaker
}

# Axe
verticalSwing = Move("Vertical Swing", 0.15, 0.1, 0.1, "SCHICK!")
horizontalSwing = Move("Horizontal Swing", 0.1, 0.15, 0.1, "SCHINK!")

axeMoves = { 
    verticalSwing.name: verticalSwing,
    horizontalSwing.name: horizontalSwing
}

# Sword/dagger
hack = Move("Hack", 0.2, 0.05, 0.2, "SCHWACK!")
stab = Move("Stab", 0.15, 0.1, 0.2, "SHINK!")

bladeMoves = {
    hack.name: hack,
    stab.name: stab
}

# Bow
quickshot = Move("Quickshot", 0.2, 0.15, 0.2, "WIZZZ!")
powershot = Move("Powershot", 0.25, 0.05, 0.25, "FLOOP!")

bowMoves = {
    quickshot.name: quickshot,
    powershot.name: powershot
}

# Moves shared by all weapons
block = Move("Block", 0, 0.5, 0, "UGHHH!")
exhausted = Move("Exhausted", 0, 0, 0, "'Whimpers'")

sharedMoves = {
    block.name: block,
    exhausted.name: exhausted
}


# Access Moves with dictionary - "moveList[<weapon>][<move>].<Attribute>"
# Example: moveList["Sword"]["Hack"].critChance
moveList = {
    "Fist": fistMoves,
    "Axe": axeMoves,
    "Sword" or "Dagger": bladeMoves,
    "Bow": bowMoves,
    "Shared": sharedMoves
}

# Call function with dictionary index
# Example: getMoveStats(moveList["Sword"]["Hack"])
def printMoveStats(weaponMove):
    stats = "%s stats\n" \
            "Attack modifier: %s\n" \
            "Defense modifier: %s\n" \
            "Crit chance: %s\n" % (weaponMove.name, weaponMove.attackModifier,
                                  weaponMove.defenseModifier, weaponMove.critChance)
    print(stats)

def getMoveStats(characterMove, characterWeapon):
    if characterMove == 'Block' or characterMove == 'Exhausted':
        characterWeapon = 'Shared'
    characterMoveAttackStat = moveList[characterWeapon][characterMove].attackModifier
    characterMoveDefenseStat = moveList[characterWeapon][characterMove].defenseModifier
    characterMoveCritChance = moveList[characterWeapon][characterMove].critChance
    return [characterMoveAttackStat, characterMoveDefenseStat, characterMoveCritChance]

def getMoveList(weapon):
    moveOptions = {}
    # retrieve weapons for the character's weapon
    allMoves = [move for move in moveList[weapon].keys()]
    # then add the move list shared by all weapons
    [allMoves.append(move) for move in moveList["Shared"].keys()]
    # build a dictionary move list for the character of the combined moves
    for i, move in enumerate(allMoves):
        i += 1
        moveOptions[i]=move
    return moveOptions

# Print all moves for weapon
# print(moveList["Sword"].keys())

